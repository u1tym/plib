# -*- coding: utf-8 -*-

import sys
import warnings

sys.dont_write_bytecode = True
warnings.filterwarnings('ignore')

import psycopg
from psycopg import Connection, Cursor
from psycopg.rows import dict_row

from typing import Self
from typing import Optional
from typing import Literal
from typing import Union
from typing import Any

RecordType = dict[str, Union[str, int, float, bool, None]]
TableType = list[RecordType]

class Db:
    _con: Optional[Connection]
    _cur: Optional[Cursor]

    _ip: str
    _pt: int
    _nm: str
    _us: str
    _pw: str

    last_error: str

    def __init__(self: Self, ip: str, port: int, dbname: str, user: str, password: str) -> None:
        self._con = None
        self._cur = None

        self._ip = ip
        self._pt = port
        self._nm = dbname
        self._us = user
        self._pw = password

        self.last_error = ""

    def connect(self: Self) -> bool:
        result: bool = False

        try:
            self._con = psycopg.connect(
                host=self._ip, port=self._pt,
                dbname=self._nm,
                user=self._us, password=self._pw
            )
            self._con.row_factory = dict_row # type: ignore
            self._cur = self._con.cursor()
            result = True
        except Exception as e:
            self.last_error = str(e)

            if self._cur is not None:
                self._cur.close()
                self._cur = None

            if self._con is not None:
                self._con.close()
                self._con = None

        return result

    def disconnect(self: Self) -> None:

        if self._cur is not None:
            self._cur.close()
            self._cur = None

        if self._con is not None:
            self._con.close()
            self._con = None

        return

    def fetchall(self: Self, sql: str) -> Union[Literal[False], TableType]:

        if self._cur is None:
            return False

        result: Union[Literal[False], TableType] = False

        try:
            self._cur.execute(sql.encode('utf-8'))
            rows: list[dict[str, Any]] = self._cur.fetchall() # type: ignore
            result = []
            for row in rows:
                add_record: RecordType = {}
                for col_name in row.keys():
                    col_value: Union[str, int, float, bool, None] = row[col_name]
                    add_record[col_name] = col_value
                result.append(add_record)

        except Exception as e:
            self.last_error = str(e)

        return result

    def executesql(self: Self, sql: str) -> bool:

        if self._cur is None:
            return False

        result: bool = False
        try:
            self._cur.execute(sql.encode('utf-8'))
            result = True

        except Exception as e:
            self.last_error = str(e)

        return result


    def commit(self: Self) -> bool:

        if self._con is None:
            return False

        result: bool = False

        try:
            self._con.commit()
            result = True

        except Exception as e:
            self.last_error = str(e)

        return result


    def rollback(self: Self) -> bool:

        if self._con is None:
            return False

        result: bool = False

        try:
            self._con.rollback()
            result = True

        except Exception as e:
            self.last_error = str(e)

        return result
