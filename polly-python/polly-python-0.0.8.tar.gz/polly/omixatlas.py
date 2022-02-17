import json
import ssl
import logging
import os
import platform
import tempfile
from pathlib import Path
from typing import Union, Dict
from collections import namedtuple
import pandas as pd
import requests
from retrying import retry

from polly import helpers
from polly.auth import Polly
from polly.constants import DATA_TYPES
from polly.errors import (
    QueryFailedException,
    UnfinishedQueryException,
    InvalidParameterException,
    error_handler,
    is_unfinished_query_error,
    paramException, wrongParamException, apiErrorException
)
from deprecated import deprecated

QUERY_API_V1 = "v1"
QUERY_API_V2 = "v2"


class OmixAtlas:
    def __init__(self, token=None, env="polly") -> None:
        self.session = Polly.get_session(token, env=env)
        self.base_url = f"https://v2.api.{self.session.env}.elucidata.io"
        self.discover_url = f"https://api.discover.{self.session.env}.elucidata.io"
        self.elastic_url = f"https://api.datalake.discover.{self.session.env}.elucidata.io/elastic"
        self.resource_url = f"{self.base_url}/v1/omixatlases"

    def get_all_omixatlas(self):
        url = self.resource_url
        params = {"summarize": "true"}
        response = self.session.get(url, params=params)
        error_handler(response)
        return response.json()

    def omixatlas_summary(self, key: str):
        url = f"{self.resource_url}/{key}"
        params = {"summarize": "true"}
        response = self.session.get(url, params=params)
        error_handler(response)
        return response.json()

    def query_metadata(
        self,
        query: str,
        experimental_features=None,
        query_api_version=QUERY_API_V1,
        page_size=None,  # Note: do not increase page size more than 999
    ):
        max_page_size = 999
        if page_size is not None and page_size > max_page_size:
            raise ValueError(
                f"The maximum permitted value for page_size is {max_page_size}"
            )
        elif page_size is None and query_api_version != QUERY_API_V2:
            page_size = 500

        queries_url = f"{self.resource_url}/queries"
        queries_payload = {
            "data": {
                "type": "queries",
                "attributes": {
                    "query": query,
                    "query_api_version": query_api_version
                }
            }
        }
        if experimental_features is not None:
            queries_payload.update({
                "experimental_features": experimental_features
            })

        response = self.session.post(queries_url, json=queries_payload)
        error_handler(response)

        query_data = response.json().get("data")
        query_id = query_data.get("id")
        return self._process_query_to_completion(
            query_id,
            query_api_version,
            page_size
        )

    @retry(
        retry_on_exception=is_unfinished_query_error,
        wait_exponential_multiplier=500,   # Exponential back-off starting 500ms
        wait_exponential_max=10000,        # After 10s, retry every 10s
        stop_max_delay=300000              # Stop retrying after 300s (5m)
    )
    def _process_query_to_completion(
        self,
        query_id: str,
        query_api_version: str,
        page_size: Union[int, None]
    ):
        queries_url = f"{self.resource_url}/queries/{query_id}"
        response = self.session.get(queries_url)
        error_handler(response)

        query_data = response.json().get("data")
        query_status = query_data.get("attributes", {}).get("status")
        if query_status == "succeeded":
            return self._handle_query_success(
                query_data,
                query_api_version,
                page_size
            )
        elif query_status == "failed":
            self._handle_query_failure(query_data)
        else:
            raise UnfinishedQueryException(query_id)

    def _handle_query_failure(self, query_data: dict):
        fail_msg = query_data.get("attributes").get("failure_reason")
        raise QueryFailedException(fail_msg)

    def _handle_query_success(
        self,
        query_data: dict,
        query_api_version: str,
        page_size: Union[int, None]
    ) -> pd.DataFrame:
        query_id = query_data.get("id")

        details = []
        time_taken_in_ms = query_data.get("attributes").get("exec_time_ms")
        if isinstance(time_taken_in_ms, int):
            details.append(
                "time taken: {:.2f} seconds".format(time_taken_in_ms / 1000)
            )
        data_scanned_in_bytes = query_data.get("attributes").get(
            "data_scanned_bytes"
        )
        if isinstance(data_scanned_in_bytes, int):
            details.append(
                "data scanned: {:.3f} MB".format(
                    data_scanned_in_bytes / (1024 ** 2)
                )
            )

        if details:
            detail_str = ", ".join(details)
            print(
                "Query execution succeeded "
                f"({detail_str})"
            )
        else:
            print("Query execution succeeded")

        if query_api_version != QUERY_API_V2 or page_size is not None:
            return self._fetch_results_as_pages(query_id, page_size)
        else:
            return self._fetch_results_as_file(query_id)

    def _fetch_results_as_pages(self, query_id, page_size):
        first_page_url = (
            f"{self.resource_url}/queries/{query_id}"
            f"/results?page[size]={page_size}"
        )
        response = self.session.get(first_page_url)
        error_handler(response)
        result_data = response.json()
        rows = [
            row_data.get("attributes") for row_data in result_data.get("data")
        ]

        all_rows = rows

        message = "Fetched {} rows"
        print(message.format(len(all_rows)), end="\r")

        while (
            result_data.get("links") is not None
            and result_data.get("links").get("next") is not None
            and result_data.get("links").get("next") != "null"
        ):
            next_page_url = self.base_url + result_data.get("links").get("next")
            response = self.session.get(next_page_url)
            error_handler(response)
            result_data = response.json()
            if result_data.get("data"):
                rows = [
                    row_data.get("attributes")
                    for row_data in result_data.get("data")
                ]
            else:
                rows = []
            all_rows.extend(rows)
            print(message.format(len(all_rows)), end="\r")

        # Blank line resets console line start position
        print()

        return pd.DataFrame(all_rows)

    def _fetch_results_as_file(self, query_id):
        results_file_req_url = (
            f"{self.resource_url}/queries/{query_id}/results?action=download"
        )
        response = self.session.get(results_file_req_url)
        error_handler(response)
        result_data = response.json()

        results_file_download_url = result_data.get("data", {}).get(
            "download_url"
        )
        if (
            results_file_download_url is None
            or results_file_download_url == "Not available"
        ):
            # The user is probably executing SHOW TABLES or DESCRIBE query
            return self._fetch_results_as_pages(query_id, 100)

        def _local_temp_file_path(filename):
            temp_dir = Path(
                "/tmp" if platform.system() == "Darwin"
                else tempfile.gettempdir()
            ).absolute()

            temp_file_path = os.path.join(temp_dir, filename)
            if Path(temp_file_path).exists():
                os.remove(temp_file_path)

            return temp_file_path

        def _download_file_stream(download_url, _local_file_path):
            with requests.get(download_url, stream=True, headers={}) as r:
                r.raise_for_status()
                with open(_local_file_path, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)

        local_file_path = _local_temp_file_path(f"{query_id}.csv")
        _download_file_stream(results_file_download_url, local_file_path)

        data_df = pd.read_csv(local_file_path)
        print(f"Fetched {len(data_df.index)} rows")

        return data_df

    def get_schema_from_api(self, repo_id: str, schema_type_dict: dict) -> dict:
        """
            Gets the schema of a repo id for the given repo_id and
            schema_type definition at the top level
            params:
            repo_id => str
            schema_type_dict => dictionary {schema_level:schema_type}
            example {'dataset': 'files', 'sample': 'gct_metadata'}
            Ouput:
                {
                    "data": {
                        "id": "<REPO_ID>",
                        "type": "schema",
                        "attributes": {
                            "schema_type": "files | gct_metadata | h5ad_metadata",
                            "schema": {
                                ... field definitions
                            }
                        }
                    }
                }
        """
        resp_dict = {}
        schema_base_url = f'{self.discover_url}/repositories'
        summary_query_param = '?response_format=summary'
        if repo_id and schema_type_dict and isinstance(schema_type_dict, Dict):
            for key, val in schema_type_dict.items():
                schema_type = val
                dataset_url = f"{schema_base_url}/{repo_id}/schemas/{schema_type}{summary_query_param}"
                resp = self.session.get(dataset_url)
                error_handler(resp)
                resp_dict[key] = resp.json()
        else:
            raise paramException(
                title="Param Error",
                detail="repo_id and schema_type_dict are either empty or its datatype is not correct"
            )
        return resp_dict

    def get_schema(self, repo_id: str, schema_level=['dataset', 'sample'], data_type="others") -> dict:
        """
            Visualizing the schema of the repository depending on schema_type
            schema_type : gct_metadata or h5ad_metadata i.e Column Fields (Sample)
            metdata schema definition for sample:
                schema:{
                    "<SOURCE>": {
                        "<DATATYPE>": {
                            "<FIELD_NAME>": {
                            "type": "text | integer | object",
                            "description": "string", (Min=1, Max=100)
                            },
                            ... other fields
                        }
                        ... other Data types
                    }
                    ... other Sources
                }
            schema_type : files i.e Global Fields (dataset)
            PS :- ALL, ALL keys is not rigid for dataset level schema also
            There it can be Source and dataset key also
            metadata schema definition for a dataset:
                schema:{
                        "ALL": {
                            "ALL": {
                                "<FIELD_NAME>": {
                                "type": "text | integer | object",
                                "description": "string", (Min=1, Max=100)
                                },
                                ... other fields
                            }
                        }
            As Data Source and Data types segregation is not applicable
            at Dataset Level Information (applicable for sample metadata only)
            schema_type : gct_metadata i.e Row Fields (Feature)
            Not there right now

            Output:
                {
                    'dataset':pd.DataFrame,
                    'sample':pd.DataFrame
                }
        """

        # get schema_type_dict
        schema_type_dict = self.get_schema_type(schema_level, data_type)

        # schema from API calls
        if repo_id and schema_type_dict and isinstance(schema_type_dict, Dict):
            schema = self.get_schema_from_api(repo_id, schema_type_dict)

        if schema and isinstance(schema, Dict):
            for key, val in schema_type_dict.items():
                if 'dataset' in key and schema[key]['data']['attributes']['schema']:
                    schema[key] = schema[key]['data']['attributes']['schema']
                elif 'sample' in key and schema[key]['data']['attributes']['schema']:
                    schema[key] = schema[key]['data']['attributes']['schema']

        df_map = {}
        for key, val in schema.items():
            flatten_dict = self.flatten_nested_schema_dict(schema[key])
            df_map[key] = self.nested_dict_to_df(flatten_dict)

        return self.return_schema_data(df_map)

    def return_schema_data(self, df_map: dict) -> tuple:
        """
            Return schema data as named tuple
        """
        if 'dataset' in df_map and 'sample' in df_map:
            Schema = namedtuple("Schema", ["dataset", "sample"])
            return Schema(df_map['dataset'], df_map['sample'])
        elif 'dataset' in df_map:
            Schema = namedtuple("Schema", "dataset")
            return Schema(df_map['dataset'])
        elif 'sample' in df_map:
            Schema = namedtuple("Schema", "sample")
            return Schema(df_map['sample'])

    @deprecated(reason="use function get_schema")
    def visualize_schema(self, repo_id: str, schema_level=['dataset', 'sample'], data_type="others") -> dict:
        """
            Visualizing the schema of the repository depending on schema_type
            schema_type : gct_metadata or h5ad_metadata i.e Column Fields (Sample)
            metdata schema definition for sample:
                schema:{
                    "<SOURCE>": {
                        "<DATATYPE>": {
                            "<FIELD_NAME>": {
                            "type": "text | integer | object",
                            "description": "string", (Min=1, Max=100)
                            },
                            ... other fields
                        }
                        ... other Data types
                    }
                    ... other Sources
                }
            schema_type : files i.e Global Fields (dataset)
            PS :- ALL, ALL keys is not rigid for dataset level schema also
            There it can be Source and dataset key also
            metadata schema definition for a dataset:
                schema:{
                        "ALL": {
                            "ALL": {
                                "<FIELD_NAME>": {
                                "type": "text | integer | object",
                                "description": "string", (Min=1, Max=100)
                                },
                                ... other fields
                            }
                        }
            As Data Source and Data types segregation is not applicable
            at Dataset Level Information (applicable for sample metadata only)
            schema_type : gct_metadata i.e Row Fields (Feature)
            Not there right now

            Output:
                {
                    'dataset':pd.DataFrame,
                    'sample':pd.DataFrame
                }
        """

        # get schema_type_dict
        schema_type_dict = self.get_schema_type(schema_level, data_type)

        # schema from API calls
        if repo_id and schema_type_dict and isinstance(schema_type_dict, Dict):
            schema = self.get_schema_from_api(repo_id, schema_type_dict)

        if schema and isinstance(schema, Dict):
            for key, val in schema_type_dict.items():
                if 'dataset' in key and schema[key]['data']['attributes']['schema']:
                    schema[key] = schema[key]['data']['attributes']['schema']
                elif 'sample' in key and schema[key]['data']['attributes']['schema']:
                    schema[key] = schema[key]['data']['attributes']['schema']

        df_map = {}
        for key, val in schema.items():
            flatten_dict = self.flatten_nested_schema_dict(schema[key])
            df_map[key] = self.nested_dict_to_df(flatten_dict)

        return self.return_schema_data(df_map)

    def get_schema_type(self, schema_level: list, data_type: str) -> dict:
        """
            Compute schema_type based on repo_id and schema_level
            schema_level         schema_type
            ------------------------------------
            dataset         ==   file
            ----------------------------------
            sample          ==   gct_metadata
            -----------------------------------
            sample and      ==    h5ad_metadata
            single cell
        """
        if schema_level and isinstance(schema_level, list):
            if 'dataset' in schema_level and 'sample' in schema_level:
                if data_type == "others":
                    schema_type_dict = {'dataset': 'files', 'sample': 'gct_metadata'}
                elif data_type == "single_cell":
                    schema_type_dict = {'dataset': 'files', 'sample': 'h5ad_metadata'}
                else:
                    raise wrongParamException(
                        title="Incorrect Param Error",
                        detail="Incorrect value of param passed data_type "
                    )
            elif 'dataset' in schema_level or 'sample' in schema_level:
                if 'dataset' in schema_level:
                    schema_type_dict = {'dataset': 'files'}
                elif 'sample' in schema_level:
                    if data_type == "others":
                        schema_type_dict = {'sample': 'gct_metadata'}
                    elif data_type == "single_cell":
                        schema_type_dict = {'sample': 'h5ad_metadata'}
                    else:
                        raise wrongParamException(
                            title="Incorrect Param Error",
                            detail="Incorrect value of param passed data_type "
                        )
            else:
                raise wrongParamException(
                    title="Incorrect Param Error",
                    detail="Incorrect value of param passed schema_level "
                )
        else:
            raise paramException(
                title="Param Error",
                detail="schema_level is either empty or its datatype is not correct"
            )
        return schema_type_dict

    def flatten_nested_schema_dict(self, nested_schema_dict: dict) -> dict:
        """
         Flatten the nested dict
          Input:
          schema:{
                    "<SOURCE>": {
                        "<DATATYPE>": {
                            "<FIELD_NAME>": {
                            "type": "text | integer | object",
                            "description": "string", (Min=1, Max=100)
                            },
                            ... other fields
                        }
                        ... other Data types
                    }
                    ... other Sources
                }

          Output:
                   {
                       'Source':source_list,
                       'Datatype': datatype_list,
                       'Field Name':field_name_list,
                       'Field Description':field_desc_list,
                       'Field Type': field_type_list
                   }

        """
        reformed_dict = {}
        source_list = []
        data_type_list = []
        field_name_list = []
        field_description_list = []
        field_type_list = []
        for outer_key, inner_dict_datatype in nested_schema_dict.items():
            for middle_key, inner_dict_fields in inner_dict_datatype.items():
                for inner_key, field_values in inner_dict_fields.items():
                    source_list.append(outer_key)
                    data_type_list.append(middle_key)
                    field_name_list.append(inner_key)
                    for key, value in field_values.items():
                        if key == 'description':
                            field_description_list.append(field_values[key])
                        if key == 'type':
                            field_type_list.append(field_values[key])

        reformed_dict['Source'] = source_list
        reformed_dict['Datatype'] = data_type_list
        reformed_dict['Field Name'] = field_name_list
        reformed_dict['Field Description'] = field_description_list
        reformed_dict['Field Type'] = field_type_list
        return reformed_dict

    def nested_dict_to_df(self, schema_dict: dict) -> pd.DataFrame:
        """
          Convert flatten dict into df and print it
          Input:
                {
                       'Source':source_list,
                       'Datatype': datatype_list,
                       'Field Name':field_name_list,
                       'Field Description':field_desc_list,
                       'Field Type': field_type_list
                }
          Output:
                DataFrame
        """
        pd.options.display.max_columns = None
        pd.options.display.width = None
        multiIndex_df = pd.DataFrame.from_dict(schema_dict, orient='columns')
        return multiIndex_df

    def format_type(self, data: dict) -> dict:
        """
            Format the dict data
        """
        if data and isinstance(data, Dict):
            return json.dumps(data, indent=4)

    def insert_schema(self, repo_id: str, body: dict) -> dict:
        """
            Params:
                repo_id => str => ex:- "345652035432"
                body => dict
                {
                    "data": {
                        "id": "<REPO_ID>",
                        "type": "schema",
                        "attributes": {
                        "schema_type": "files | gct_metadata | h5ad_metadata",
                        "schema": {
                            ... field definitions
                        }
                        }
                    }
                }
        """
        if repo_id and body and isinstance(body, dict):
            body = json.dumps(body)
            try:
                schema_base_url = f'{self.discover_url}/repositories'
                url = f"{schema_base_url}/{repo_id}/schemas"
                resp = self.session.post(url, data=body)
                error_handler(resp)
                return resp.text
            except Exception as err:
                raise apiErrorException(
                    title="API exception err",
                    detail=err
                )
        else:
            raise apiErrorException(
                title="Param Error",
                detail="Params are either empty or its datatype is not correct"
            )

    def update_schema(self, repo_id: str, body: dict) -> dict:
        """
        Params:
                repo_id => str => ex:- "345652035432"
                body => dict
                {
                    "data": {
                        "id": "<REPO_ID>",
                        "type": "schema",
                        "attributes": {
                        "schema_type": "files | gct_metadata | h5ad_metadata",
                        "schema": {
                            ... field definitions
                        }
                        }
                    }
                }
        """
        schema_type = body['data']['attributes']['schema_type']
        schema_base_url = f'{self.discover_url}/repositories'
        url = f"{schema_base_url}/{repo_id}/schemas/{schema_type}"
        if repo_id and body and isinstance(body, dict):
            body = json.dumps(body)
            try:
                resp = self.session.patch(url, data=body)
                error_handler(resp)
                return resp.text
            except Exception as err:
                raise apiErrorException(
                    title="API exception err",
                    detail=err
                )
        else:
            raise paramException(
                title="Param Error",
                detail="Params are either empty or its datatype is not correct"
            )

    # ? DEPRECATED
    def search_metadata(self, query: dict):
        url = f"{self.resource_url}/_search"
        payload = query
        response = self.session.get(url, json=payload)
        error_handler(response)
        return response.json()

    def download_data(self, repo_name, _id: str):
        url = f"{self.resource_url}/{repo_name}/download"
        params = {"_id": _id}
        response = self.session.get(url, params=params)
        error_handler(response)
        return response.json()

    def save_to_workspace(self, repo_id: str, dataset_id: str,
                          workspace_id: int,
                          workspace_path: str) -> json:
        '''
            Function for saving data from omixatlas to workspaces.
            Makes a call to v1/omixatlas/workspace_jobs
        '''
        url = f"{self.resource_url}/workspace_jobs"
        params = {"action": "copy"}
        payload = {
            "data": {
                "type": "workspaces",
                "attributes": {
                    "dataset_id": dataset_id,
                    "repo_id": repo_id,
                    "workspace_id": workspace_id,
                    "workspace_path": workspace_path
                }
            }
        }
        response = self.session.post(url,
                                     data=json.dumps(payload),
                                     params=params)
        error_handler(response)
        if response.status_code == 200:
            logging.basicConfig(level=logging.INFO)
            logging.info(f'Data Saved to workspace={workspace_id}')
        return response.json()

    def format_converter(self, repo_key: str, dataset_id: str, to: str) -> None:
        """
        Function to convert a file to maf format.
        """
        if(not (repo_key and isinstance(repo_key, str))):
            raise InvalidParameterException('repo_id/repo_name')
        if(not (dataset_id and isinstance(dataset_id, str))):
            raise InvalidParameterException('dataset_id')
        if(not (to and isinstance(to, str))):
            raise InvalidParameterException('convert_to')
        ssl._create_default_https_context = ssl._create_unverified_context
        response_omixatlas = self.omixatlas_summary(repo_key)
        data = response_omixatlas.get('data')
        repo_name = data.get('repo_name')
        index_name = data.get("indexes", {}).get("files")
        if(index_name is None):
            raise paramException(
                title='Param Error',
                detail='Repo entered is not an omixatlas.'
            )
        elastic_url = f"{self.elastic_url}/{index_name}/_search"
        query = {
            "query": {
                "bool": {
                    "must": [
                        {"term": {"_index": index_name}},
                        {"term": {"dataset_id.keyword": dataset_id}},
                    ]
                }
            }
        }
        data_type = helpers.get_data_type(self, elastic_url, query)
        if(data_type in DATA_TYPES):
            mapped_list = DATA_TYPES[data_type][0]
            if(to in mapped_list['format']):
                supported_repo = mapped_list['supported_repo']
                repo_found = False
                for details in supported_repo:
                    if(repo_name == details['name']):
                        header_mapping = details['header_mapping']
                        repo_found = True
                if(not repo_found):
                    raise paramException(
                        title="Param Error",
                        detail=f"Incompatible repository error: Repository:'{repo_name}' not yet \
                                 incorporated for converter function"
                    )
                helpers.file_conversion(self, repo_name, dataset_id, to, header_mapping)
            else:
                raise paramException(
                    title="Param Error",
                    detail=f"Incompatible dataformat error: data format= {to} not yet incorporated for converter function"
                )
        else:
            raise paramException(
                title="Param Error",
                detail=f"Incompatible dataype error: data_type={data_type} not yet incorporated for converter function"
            )
        logging.basicConfig(level=logging.INFO)
        logging.info("File converted successfully!")


if __name__ == "__main__":
    client = OmixAtlas()
