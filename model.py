from datetime import date
from enums import Party, Gender, DebateType


class Politician:
    def __init__(self, csv_key, name, party:Party, date_of_birth: date, gender: Gender):
        self.csv_key = csv_key.upper()
        self.name = name
        self.party = party
        self.date_of_birth = date_of_birth
        self.gender = gender

        self.debates_participated = []
        self.opponents = {}


class Utterance:
    def __init__(self, speaker: Politician, text):
        self.speaker = speaker
        self.text = text
        

class Debate:
    def __init__(self, name, link, debate_type: DebateType, debate_date: date, place):
        self.full_name = name
        self.link = link
        self.debate_type = debate_type
        self.date = debate_date
        self.year = self.date.year
        self.place = place

        self.politicians = []
        self.other_speakers = []
        self.utterances = []
    
    def __iter__(self):
        return iter(self.utterances)

    def _add_politician(self, politician: Politician):
        if politician not in self.politicians:
            self.politicians.append(politician)
            politician.debates_participated.append(self)

    def _add_utterance(self, utterance: Utterance):
        self.utterances.append(utterance)
        if isinstance(utterance.speaker, Politician):
            return
        if utterance.speaker not in self.other_speakers:
            self.other_speakers.append(utterance.speaker)
