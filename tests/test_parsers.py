from parsers import parse_row, ServiceRecord
from entities import Action
from datetime import datetime
import pytest
from errors import HeaderException


class TestParser():

    def test_parser_row(self):
        row = ['John Doe', 'Abandonó', '25/3/2021 13:48:29']
        record = parse_row(row, 1)
        assert record.action == Action.ABANDONO
        assert isinstance(record.update_at, datetime)
        assert record.name == 'John Doe'

    def test_parser_row_fails(self):
        row = ["nombre", "accion", "hora"]
        with pytest.raises(HeaderException):
            parse_row(row, 1)

    def test_get_names(self, many_dumb_records):
        servicio = ServiceRecord(many_dumb_records)
        nombres = servicio.get_names()
        assert len(nombres) == 7
        assert "Nombre 7" not in nombres

    def test_leaving_and_joining_time(self, many_dumb_records):
        servicio = ServiceRecord(many_dumb_records)
        for name in servicio.get_names():
            assert servicio.get_joined_time(name) <= servicio.get_leaving_time(name)
