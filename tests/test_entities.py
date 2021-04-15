from entities import Record, Action
from datetime import datetime
import pytest


class TestEntities:
    def test_can_instantiate(self):
        record = Record(
            line=1,
            name="Pepe Perez",
            action=Action.ABANDONO,
            update_at=datetime.strptime("23/2/2021 8:30:03", '%d/%m/%Y %H:%M:%S')
        )

    def test_cant_instantiate(self):
        with pytest.raises(Exception):
            record = Record(
                line=1,
                name="pedro lopez",
                action=Action.ANTES,
                update_at=datetime.strptime("30/2/2021 8:30:03", '%d/%m/%Y %H:%M:%S')
            )
