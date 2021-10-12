from entities import Record, Action
from datetime import datetime
from typing import List
from errors import HeaderException


def parse_row(row: list, num: int) -> Record:
    if row[1] not in [elem.value for elem in Action]:
        raise HeaderException
    new_record = Record(
        line=num,
        name=row[0],
        action=Action(row[1]),
        update_at=datetime.strptime(row[2], '%d/%m/%Y %H:%M:%S')
        # update_at=datetime.strptime(row[2], '%m/%d/%Y, %H:%M:%S %p')
    )
    return new_record


class ServiceRecord:
    def __init__(self, list_of_records: List[Record]) -> None:
        self.records = list_of_records

    def _meeting_start(self) -> datetime:
        starting_time = datetime.utcnow()
        for elem in self.records:
            if elem.action == Action.UNIDO:
                starting_time = elem.update_at if elem.update_at < starting_time else starting_time
        return starting_time

    def _meeting_end(self) -> datetime:
        end_time = datetime.strptime("01/01/1970 00:00:00", '%m/%d/%Y %H:%M:%S')
        for elem in reversed(self.records):
            if elem.action == Action.ABANDONO:
                end_time = elem.update_at if elem.update_at > end_time else end_time
        return end_time

    def get_names(self) -> List[str]:
        # conjunto = set()
        # for elem in self.records:
        #     conjunto.add(elem.name)
        # return list(conjunto)
        return list(set(elem.name for elem in self.records))

    def get_joined_time(self, name: str) -> datetime:
        joined_time = self._meeting_start()
        for elem in self.records:
            if elem.name == name:
                if elem.action == Action.UNIDO:
                    if elem.update_at > joined_time:
                        return elem.update_at
        return joined_time

    def get_leaving_time(self, name: str) -> datetime:
        leaving_time = self._meeting_end()
        for elem in reversed(self.records):
            if elem.name == name:
                if elem.action == Action.ABANDONO:
                    if elem.update_at < leaving_time:
                        return elem.update_at
        return leaving_time
