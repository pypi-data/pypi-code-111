import copy

from dataverk.utils.file_functions import remove_special_characters

from dataverk.resources.base_resource import BaseResource


class PDFResource(BaseResource):
    def __init__(
        self,
        resource: bytes,
        datapackage_path: str,
        resource_name: str,
        resource_description: str,
        spec: dict = None,
    ):
        super().__init__(resource, datapackage_path, resource_description, spec)

        self._resource_name = resource_name
        self._compress = self._spec.get("compress", False)
        self._fmt = self._spec.get("format", "pdf")
        self._schema = self._get_schema()

    def formatted_resource_name(self):
        return remove_special_characters(self._resource_name)

    def _resource_path(self):
        return self._create_resource_path(
            self.formatted_resource_name(),
            self._fmt,
            self._compress,
        )

    def _get_schema(self):
        return {
            "name": self._resource_name,
            "description": self._resource_description,
            "path": self._resource_path(),
            "format": self._fmt,
            "mediatype": self._media_type(self._fmt),
            "spec": self._spec,
        }

    def add_to_datapackage(self, dp) -> None:
        """ Adds a pdf resource to the datapackage

        :param dp: Datapackage object to append resources to
        :return: path: str: Path to resource
        """
        dp.datapackage_metadata["resources"].append(self._schema)
        resource = copy.deepcopy(self._schema)
        resource["data"] = self._resource_data
        dp.resources.append(resource)
        return resource.get("path")
