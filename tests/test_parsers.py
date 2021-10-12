from parsers import parse_line, parse_row, ServiceRecord
from entities import Action
from datetime import datetime
import pytest
from errors import HeaderException


class TestParser:
    def test_parser_line(self):
        line = "Pepe Perez Abandonó 25/3/2021 13:48:29"
        record = parse_line(line, 1)
        assert record.action == Action.ABANDONO
        assert isinstance(record.update_at, datetime)
        assert record.name == "Pepe Perez"

    def test_parser_row(self):
        row = ['Pepe Pérez', 'Abandonó', '25/3/2021 13:48:29']
        record = parse_row(row, 1)
        assert record.action == Action.ABANDONO
        assert isinstance(record.update_at, datetime)
        assert record.name == 'Pepe Pérez'

    def test_parser_row_fails(self):
        row = ["nombre", "accion", "hora"]
        with pytest.raises(HeaderException):
            parse_row(row, 1)

    def test_get_names(self, many_dumb_recrods):
        servicio = ServiceRecord(many_dumb_recrods)
        nombres = servicio.get_names()
        assert len(nombres) == 7
        assert "Nombre 7" not in nombres

    def test_leaving_and_joining_time(self, many_dumb_recrods):
        servicio = ServiceRecord(many_dumb_recrods)
        name = servicio.get_names()[0]
        assert servicio.get_joined_time(name) <= servicio.get_leaving_time(name)
