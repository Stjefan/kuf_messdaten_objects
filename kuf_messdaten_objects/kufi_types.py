from dataclasses import dataclass
from enum import Enum
from uuid import UUID
import logging

class Messfiletyp(Enum):
    version_07_21_ohne_wetterdaten = 1
    version_07_21_mit_wetterdaten = 2
    sva_200a_richtungsdaten = 3

@dataclass
class WatchedFolder:
    target_dir: str
    typ: Messfiletyp
    project_name: str
    messpunkt_name: str
    id_in_db: int
    connection_string: str

@dataclass
class MesspunktMessdaten:
    id_databse: UUID
    folder: str
    messfiletyp: Messfiletyp

def foo():
    print(99)

def bar():
    logging.info("Abc...")
    print("Hello")
    return 45