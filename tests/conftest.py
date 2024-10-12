import pytest
from entities import Action, Record
from datetime import datetime


@pytest.fixture
def many_dumb_records():
    records = []
    enums = [elem.value for elem in Action]
    for elem in range(30):
        record = Record(line=elem,
                        name=f"Nombre {elem % 7}",
                        action=enums[elem % 3],
                        update_at=datetime.utcnow())
        records.append(record)
    return records
