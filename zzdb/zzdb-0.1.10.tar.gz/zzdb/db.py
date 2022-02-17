#    Copyright (C) 2021 Andrei Puchko
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.


import sys

if __name__ == "__main__":

    sys.path.insert(0, ".")

    # from demo.demo_mysql import demo
    # from demo.demo_postgresql import demo
    from demo.demo_sqlite import demo

    demo()
    # from temp.try_pg_01 import demo

    # from tests.test_db import test_mysql, test_postgresql, test_sqlite
    # test_mysql()
    # test_sqlite()
    # test_postgresql()

import re
import sqlite3 as db_sqlite_connector

# import mysql.connector as db_mysql_connector
# import psycopg2 as db_postgresql_connector

from zzdb.utils import int_, is_sub_list
from zzdb.cursor import ZzMysqlCursor, ZzSqliteCursor, ZzPostgresqlCursor
from zzdb.schema import ZzDbSchema


class ZzDb:
    def __init__(
        self,
        db_engine_name=None,
        user=None,
        password=None,
        host=None,
        database_name=None,
        port=None,
        guest_mode=False,
        url=None,
    ):
        """
        :param url: 'sqlite3|mysql|postgresql://username:password@host:port/database'
            or
        :param db_engine_name: 'sqlite3'|'mysql'|'postgresql', if None - 'sqlite3'
        :param user=''
        :param password=''
        :param host=''
        :param database_name='', if empty and db_engine_name == 'sqlite' - ':memory:'
        :param port:''
        :param guest_mode:, if empty - False
        """
        self.url = url
        self.guest_mode = guest_mode
        if url is not None:
            self._parse_url()
        else:
            if db_engine_name is None:
                db_engine_name = "sqlite3"
                if database_name is None:
                    database_name = ":memory:"
            self.db_engine_name = db_engine_name
            self.user = user
            self.password = password
            self.host = host
            self.database_name = database_name
            self.port = port

            self.connection = None

        if self.db_engine_name not in ["mysql", "sqlite3", "postgresql"]:
            raise Exception(f"Sorry, wrong DBAPI engine - {self.db_engine_name}")

        self.last_sql_error = ""
        self.last_sql = ""
        self.last_error_data = {}
        self.last_record = ""
        self.migrate_error_list = []

        self.db_schema = None
        self.connection = None
        self.escape_char = '"'

        if self.db_engine_name == "mysql":
            try:
                import mysql.connector as db_mysql_connector

                self.db_api_engine = db_mysql_connector
                self.db_cursor_class = ZzMysqlCursor
                self.escape_char = "`"
            except Exception:
                raise Exception(
                    "Sorry, can not import mysql.connector - use: pip install mysql-connector-python"
                )
        elif self.db_engine_name == "postgresql":
            try:
                import psycopg2 as db_postgresql_connector

                self.db_api_engine = db_postgresql_connector
                self.db_cursor_class = ZzPostgresqlCursor
            except Exception:
                raise Exception("Sorry, can not import psycopg2 - use: pip install psycopg2-binary")
        elif self.db_engine_name == "sqlite3":
            self.db_api_engine = db_sqlite_connector
            self.db_cursor_class = ZzSqliteCursor
        try:
            self._connect()
            return
        except Exception:
            pass  # Do nothing - give chance to screate database!
        self.create()
        self._connect()

    def _connect(self):
        self.connection = self.connect(
            user=self.user,
            password=self.password,
            host=self.host,
            database_name=self.database_name,
            port=self.port,
        )

    def create(self):
        """
        Take chance to create database
        """
        admin_database_name = {"mysql": "mysql", "postgresql": "postgres"}[self.db_engine_name]
        try:
            self.connection = self.connect(
                user=self.user,
                password=self.password,
                host=self.host,
                database_name=admin_database_name,
                port=self.port,
            )
        except Exception:
            print(sys.exc_info())
        if self.db_engine_name == "mysql":
            self._cursor(sql=f"CREATE DATABASE IF NOT EXISTS {self.database_name}")
            self._cursor(sql=f"GRANT ALL PRIVILEGES ON {self.database_name}.* TO '{self.user}'")
        elif self.db_engine_name == "postgresql":
            self._cursor(sql=f"CREATE DATABASE {self.database_name} WITH OWNER = {self.user}")
            self._cursor(sql=f"GRANT ALL PRIVILEGES ON DATABASE {self.database_name}.* TO {self.user}")
        self.connection.close()
        return True

    def connect(
        self,
        user=None,
        password=None,
        host=None,
        database_name=None,
        port=None,
    ):
        connection = None
        if self.db_engine_name == "mysql":
            connection = self.db_api_engine.connect(
                user=user,
                password=password,
                host=host if host else "localhost",
                port=port if port else 3306,
                database=database_name,
            )
        elif self.db_engine_name == "postgresql":
            connection = self.db_api_engine.connect(
                user=user,
                password=password,
                host=host if host else "localhost",
                port=port if port else 5432,
                database=database_name,
            )
            connection.autocommit = True
        elif self.db_engine_name == "sqlite3":
            connection = self.db_api_engine.connect(database=self.database_name, isolation_level=None)
        return connection

    def _parse_url(self):
        self.db_engine_name = self.url.split(":")[0]
        self.user = self.url.split("//")[1].split(":")[0]
        self.password = self.url.split("//")[1].split(":")[1].split("@")[0]
        self.host = self.url.split("@")[1].split(":")[0]
        self.port = self.url.split("@")[1].split(":")[1].split("/")[0]
        self.database_name = self.url.split("@")[1].split("/")[1]

    def close(self):
        self.connection.close()

    def get_primary_key_columns(self, table_name=""):
        """returns database primary columns for given table"""
        if self.db_schema is not None:
            cols = self.db_schema.get_schema_table_attr(table_name)
            rez = {}
            for x in cols:
                if cols[x].get("pk"):
                    cols[x]["name"] = x
                    rez[x] = cols[x]
            return rez

        if self.db_engine_name in ("mysql", "postgresql"):
            return self.get_database_columns(table_name, "column_key='PRI'")
        elif self.db_engine_name == "sqlite3":
            return self.get_database_columns(table_name, "pk=1")

    def get_database_columns(self, table_name="", filter="", query_database=None):
        """returns database columns for given table"""

        if self.db_schema is not None and filter == "" and query_database is None:
            cols = self.db_schema.get_schema_table_attr(table_name)
            for x in cols:
                cols[x]["name"] = x
            return cols

        cols = {}
        sql = self.db_cursor_class.get_table_columns_sql(table_name, filter, self.database_name)

        for x in self.cursor(sql).records():
            if "name" in x:
                if "datalen" not in x:  # SQLITE
                    if "(" in x["datatype"]:
                        field_length = re.search(r"\((.*?)\)", x["datatype"]).group(1)
                        if "," not in field_length:
                            x["datalen"] = field_length
                            x["datadec"] = "0"
                        else:
                            x["datalen"] = field_length.split(",")[0]
                            x["datadec"] = field_length.split(",")[1]
                        x["datatype"] = x["datatype"].split("(")[0]
                    else:
                        x["datalen"] = "0"
                        x["datadec"] = "0"
                cols[x["name"]] = x
        return cols

    def get_tables(self, table_name=""):
        """Returns a list of tables names from database"""
        table_select_clause = f" and TABLE_NAME='{table_name}'" if table_name else ""
        sql = self.db_cursor_class.get_table_names_sql(table_select_clause, self.database_name)
        return [x["table_name"] for x in self.cursor(sql).records()]

    def set_schema(self, db_schema: ZzDbSchema):
        """assign and migrate schema to database"""
        self.db_schema = db_schema
        return self.migrate_schema()

    def migrate_schema(self):
        """creates (no alter) tables and columns in a physical database"""
        if self.db_schema is None:
            return
        self.migrate_error_list = []
        for table in self.db_schema.get_schema_tables():
            # column that are already in
            database_columns = self.get_database_columns(table, query_database=True)
            schema_columns = self.db_schema.get_schema_columns(table)
            if not self.guest_mode:
                self._add_zz_columns(schema_columns)
            for column in schema_columns:
                colDic = self.db_schema.get_schema_attr(table, column)
                if column not in database_columns:  # new column
                    colDic["table"] = table
                    colDic["column"] = column
                    self.create_column(colDic)
                else:  # change schema as it is in database
                    colDic["datalen"] = database_columns[column]["datalen"]
                    colDic["datadec"] = database_columns[column]["datadec"]
        self.migrate_indexes()
        return True

    def _add_zz_columns(self, schema_columns):
        """adding zz-columns to the zz-schema"""
        schema_columns["zz_time"] = {"datatype": "bigint"}
        schema_columns["zz_mode"] = {"datatype": "char", "datalen": 1}
        # schema_columns["update_time"] = {"datatype": "bigint"}
        # schema_columns["insert_session_id"] = {"datatype": "int"}
        # schema_columns["update_session_id"] = {"datatype": "int"}
        # schema_columns["user_lock"] = {"datatype": "char", "datalen": 1}

    def create_column(self, column_definition):
        """migrate given 'column_definition' to database"""

        column_definition["datadec"] = column_definition.get("datadec", 0)
        column_definition["primarykey"] = "PRIMARY KEY" if column_definition.get("pk", "") else ""
        if column_definition.get("to_table") and column_definition.get("to_column"):
            # pull attributes from primary table
            primary_column_definition = self.db_schema.get_schema_attr(
                column_definition["to_table"], column_definition["to_column"]
            )
            for x in ["datatype", "datalen", "datadec"]:
                column_definition[x] = primary_column_definition[x]

        if "datatype" not in column_definition:
            return None
        datatype = column_definition["datatype"].upper()
        if datatype[:3] in ["NUM", "DEC"]:
            column_definition["datatype"] = "NUMERIC"
            column_definition["default"] = "DEFAULT '0'"
            column_definition["size"] = "({datalen},{datadec})".format(**column_definition)
        elif "INT" in datatype:
            column_definition["default"] = "DEFAULT '0'"
            column_definition["size"] = ""
        elif "CHAR" in datatype:
            column_definition["default"] = "DEFAULT ''"
            column_definition["size"] = (
                "({datalen})".format(**column_definition) if column_definition["datalen"] else ""
            )
        elif "DATE" in datatype:
            column_definition["default"] = "DEFAULT '0000-00-00'"
            column_definition["size"] = ""
        elif "TEXT" in datatype:
            column_definition["default"] = ""
            column_definition["size"] = ""
        else:
            column_definition["size"] = ""
            column_definition["default"] = ""
        column_definition["escape_char"] = self.escape_char
        sql_column_text = (
            """ {escape_char}{column}{escape_char} {datatype} {size} {primarykey} {default}""".format(
                **column_definition
            )
        )
        table = column_definition["table"]
        if table in self.get_tables():
            sql_cmd = f"ALTER TABLE {table} ADD {sql_column_text}"
        else:
            sql_cmd = f"CREATE TABLE {table} ({sql_column_text})"

        if not self.run_migrate_sql(sql_cmd):
            return False
        if not self.guest_mode and not table.upper().startswith("LOG_"):

            self.create_index(column_definition)

            log_column_definition = dict(column_definition)
            log_column_definition["pk"] = None
            log_column_definition["ai"] = None
            log_column_definition["uk"] = None
            log_column_definition["table"] = "log_" + log_column_definition["table"]
            self.create_column(log_column_definition)
        return True

    def create_index(self, column_definition):
        """
        create index for column
        """
        if (
            column_definition.get("index")
            or column_definition.get("column") == "name"
            or column_definition.get("column") == "date"
            or column_definition.get("to_table")
        ):
            sql_cmd = "CREATE INDEX {table}_{column} on {table} ({column})".format(**column_definition)
            self.run_migrate_sql(sql_cmd)

    def run_migrate_sql(self, sql_cmd):
        self._cursor(sql_cmd)
        # if 'Group' in sql_cmd:
        #     print(sql_cmd)
        if self.last_sql_error != "":
            self.migrate_error_list.append(self.last_sql_error)
            return False
        return True

    def migrate_indexes(self):
        if self.guest_mode:
            return
        indexes = self.db_schema.get_schema_indexes()
        for x in indexes:
            if not x.get("name"):
                x["name"] = re.sub(r"[^\w\d]+", "_", x["expression"])
            sql_cmd = "CREATE INDEX {table}_{name} on {table} ({expression})".format(**x)
            self.run_migrate_sql(sql_cmd)

    def _sqlite_patch(self, sql, record, table_columns):
        """Adapt sql statement for sqlite - convert str to int, replace placeholder character to ?"""
        for x in record:
            if "int" in table_columns.get(x, {}).get("type", ""):
                try:
                    record[x] = int_(record[x])
                except Exception:
                    print(table_columns.get(x, {}).get("type", ""), record[x])
        sql = sql.replace("%s", "?")
        return sql

    def _check_record_for_numbers(self, table, record):
        """ "makes sure that all number columns value is not blank string"""
        for x in record:
            if record[x] != "":
                continue
            datatype = self.db_schema.get_schema_attr(table, x).get("datatype")
            if datatype is None:
                continue
            if "int" in datatype or "dec" in datatype or "num" in datatype:
                record[x] = "0"

    def raw_insert(self, table_name="", record={}):
        """insert dictionary into table"""
        if not (table_name and record):
            return None

        sql = (
            f"insert into {table_name} ("
            + ",".join([f"{self.escape_char}{x}{self.escape_char}" for x in record.keys()])
            + ") values ("
            + ",".join(["%s" for x in record.keys()])
            + ")"
        )

        if self.db_engine_name == "sqlite3":
            sql = sql.replace("%s", "?")

        data = [record[x] for x in record.keys()]

        self._cursor(sql, data)

        if self.last_sql_error:
            return False
        else:
            return True

    def insert(self, table_name="", record={}):
        """insert dictionary into table"""
        if not (table_name and record):
            return None

        if not table_name.upper().startswith("LOG_"):
            record["zz_time"] = f"{self.cursor().now()}"
            record["zz_mode"] = "i"
            # check foreign keys
            foreign_keys_list = self.db_schema.get_primary_tables(table_name, record)
            for x in foreign_keys_list:
                x["escape_char"] = self.escape_char
                if (
                    self.get(
                        x["primary_table"],
                        "{escape_char}{primary_column}{escape_char}= '{child_value}' ".format(**x),
                        x["child_value"],
                    )
                    == {}
                ):
                    self.last_sql_error = (
                        "Foreign key error for insert:"
                        + f" For {self.escape_char}{table_name}{self.escape_char}"
                        + ".{escape_char}{child_column}{escape_char}".format(**x)
                        + " not found value '{child_value}' ".format(**x)
                        + "in table "
                        + x["primary_table"]
                        + ".{primary_column}".format(**x)
                    )
                    self.last_error_data = x
                    return False

        table_columns = self.get_database_columns(table_name)
        primary_key_columns = self.get_primary_key_columns(table_name)
        columns_list = [x for x in record if x in table_columns]

        for x in primary_key_columns:
            if x not in columns_list:
                columns_list.append(x)
            is_string_data = True if ("char" in primary_key_columns[x]["datatype"]) else False
            if is_string_data:
                primary_key_value = record.get(x, "")
            else:
                primary_key_value = int_(record.get(x, 0))
            while (
                self.cursor(
                    sql=f"""select {self.escape_char}{x}{self.escape_char}
                            from {table_name} 
                            where {self.escape_char}{x}{self.escape_char}='{primary_key_value}'
                        """
                ).row_count()
                > 0
            ):
                if is_string_data:
                    primary_key_value += "_"
                else:
                    primary_key_value += 1
            record[x] = primary_key_value

        sql = (
            f"insert into {table_name} ("
            + ",".join([f"{self.escape_char}{x}{self.escape_char}" for x in columns_list])
            + ") values ("
            + ",".join(["%s" for x in columns_list])
            + ")"
        )

        if self.db_engine_name == "sqlite3":
            sql = self._sqlite_patch(sql, record, table_columns)

        self._check_record_for_numbers(table_name, record)
        data = [record[x] for x in columns_list]

        self._cursor(sql, data)

        if self.last_sql_error:
            return False
        else:
            if not table_name.upper().startswith("LOG_") and table_name.upper() != "PLATFORM":
                self.insert("log_" + table_name, record)
            return True

    def update(self, table_name="", record={}):
        """update from dictionary to table"""
        if not (table_name and record):
            return None

        table_columns = self.get_database_columns(table_name)
        primary_key_columns = self.get_primary_key_columns(table_name)

        if not table_name.upper().startswith("LOG_"):
            record["zz_time"] = f"{self.cursor().now()}"
            record["zz_mode"] = "u"
            foreign_keys_list = self.db_schema.get_primary_tables(table_name, record)
            for x in foreign_keys_list:
                if x["child_column"] not in record:  # column not going to change - skip checking
                    continue
                if self.get(x["primary_table"], "%(primary_column)s='%(child_value)s'" % x) == {}:
                    self.last_sql_error = (
                        "Foreign key error for update:"
                        + f" For {table_name}"
                        + ".{child_column}".format(**x)
                        + " not found value '{child_value}' ".format(**x)
                        + "in table "
                        + x["primary_table"]
                        + ".{primary_column}".format(**x)
                    )
                    self.last_error_data = x
                    return False

        columns_list = [x for x in record if x in table_columns]
        if is_sub_list(primary_key_columns.keys(), record.keys()):
            sql = f"update {table_name} set " + ",".join(
                [
                    f" {self.escape_char}{x}{self.escape_char}=%s "
                    for x in record
                    if x not in primary_key_columns and x in columns_list
                ]
            )
            sql += " where " + " and ".join(
                [f" {self.escape_char}{x}{self.escape_char} = %s " for x in primary_key_columns]
            )
            if self.db_engine_name == "sqlite3":
                sql = self._sqlite_patch(sql, record, table_columns)

            self._check_record_for_numbers(table_name, record)
            data = [record[x] for x in record if x not in primary_key_columns and x in columns_list]
            data += [record[x] for x in primary_key_columns]

            self._cursor(sql, data)

            if self.last_sql_error:
                return False
            else:
                if not table_name.upper().startswith("LOG_") and table_name.upper() != "PLATFORM":
                    self.insert("log_" + table_name, record)
                return True
        else:
            self.last_sql_error = "Update requires a primary key column!"

    def delete(self, table_name="", record={}):
        if not (table_name and record):
            return None
        self.last_error_data = {}
        for x in self.db_schema.get_child_tables(table_name, record):
            x["escape_char"] = self.escape_char
            rez = self._cursor(
                "select 1 from {child_table} where {escape_char}{child_column}{escape_char}='{parent_value}'".format(
                    **x
                )
            )
            if {} != rez:
                self.last_sql_error = (
                    "Foreign key error for delete:"
                    + f" Row in {self.escape_char}{table_name}{self.escape_char}"
                    + ".{escape_char}{parent_column}{escape_char}".format(**x)
                    + "={parent_value}".format(**x)
                    + " can not to be deleted, because "
                    + ' it used in table "{child_table}"."{child_column}"'.format(**x)
                )
                self.last_error_data = x

                return False
        table_columns = self.get_database_columns(table_name)
        columns_list = [x for x in record if x in table_columns]
        where_clause = " and ".join([f"{self.escape_char}{x}{self.escape_char} = %s " for x in columns_list])
        data = [record[x] for x in columns_list]

        select_sql = f"select * from {table_name} where {where_clause}"
        if self.db_engine_name == "sqlite3":
            select_sql = self._sqlite_patch(select_sql, record, table_columns)

        row_to_be_deleted = self._cursor(select_sql, data)
        for x in row_to_be_deleted:
            row_to_be_deleted[x]["zz_mode"] = "d"
            row_to_be_deleted[x]["zz_time"] = f"{self.cursor().now()}"
            self.insert("log_" + table_name, row_to_be_deleted[x])

        sql = f"delete from {table_name} where {where_clause}"
        if self.db_engine_name == "sqlite3":
            sql = self._sqlite_patch(sql, record, table_columns)

        self._cursor(sql, data)

        if self.last_sql_error:
            return False
        else:
            return True

    def get(self, table_name="", where="", column_name=""):
        """returns value of given column or record dictionary
        from first row  given table_name for where condition
        """
        column_name = f"({column_name}) as ret " if column_name else "*"
        row = self._cursor(f"""select {column_name} from {table_name} where {where}""")
        if self.last_sql_error:
            return ""
        else:
            if row:
                if column_name == "*":
                    return row[0]
                else:
                    return row[0]["ret"]
        return {}

    def _dict_factory(self, cursor, row, sql):
        return {
            col[0]: f"{row[idx] if row[idx] is not None else ''}".rstrip()
            for idx, col in enumerate(cursor.description)
        }

    def _cursor(self, sql, data=[]):
        self.last_sql_error = ""
        self.last_sql = ""
        self.last_record = ""
        _rows = {}
        try:
            _work_cursor = self.connection.cursor()
            if data:
                _work_cursor.execute(sql, data)
            else:
                _work_cursor.execute(sql)
            if _work_cursor.description:
                i = 0
                for x in _work_cursor.fetchall():
                    _rows[i] = self._dict_factory(_work_cursor, x, sql)
                    i += 1
        except self.db_api_engine.Error as err:
            self.last_sql_error = {err}
            self.last_sql = sql
            self.last_record = "!".join([f"{x}" for x in data])
            _rows = {0: {}}
        return _rows

    def cursor(self, sql="", table_name="", order="", where="", data=[], cache_flag=True):
        # TODO - sanitaze where and order
        return self.db_cursor_class(
            self,
            sql,
            table_name=table_name,
            order=order,
            where=where,
            data=data,
            cache_flag=cache_flag,
        )

    def table(self, table_name="", order="", where="", cache_flag=True):
        return self.db_cursor_class(
            self,
            sql="",
            table_name=table_name,
            order=order,
            where=where,
            cache_flag=cache_flag,
        )
