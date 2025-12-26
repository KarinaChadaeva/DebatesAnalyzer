from enum import Enum

class Party(Enum):
    DEMOCRAT = "democrat"
    REPUBLICAN = "republican"

class Gender(Enum):
    MALE = "male"
    FEMALE = "female"

class DebateType(Enum):
    PRIMARIES = 'primaries'
    GENERAL = 'general'