import pandas as pd
from politicians_data import POLITICIANS_DATA, get_politician_info, is_politician
from enums import DebateType
from model import Politician, Utterance, Debate


class DebateParser():
    def __init__(self):
        self.df = None
        self.debates = []
        self.politicians = {}

    def load_csv(self, path):
        self.df = pd.read_csv(path)
        self._parse_debates()
    
    def _parse_debates(self):
        debates_dict = dict()

        for _, row in self.df.iterrows():
            speaker_name = str(row["speaker"]).strip().upper()
            if is_politician(speaker_name):
                speaker = self._get_or_create_politician(speaker_name)
            else:
                speaker = speaker_name

            key = row["link"].strip()

            if key not in debates_dict:
                debate = self._create_debate(row)
                debates_dict[key] = debate
            else:
                debate = debates_dict[key]

            utterance = Utterance(speaker=speaker, text=row['text'])
            debate._add_utterance(utterance)
            if isinstance(speaker, Politician):
                debate._add_politician(speaker)

        self.debates = list(debates_dict.values())
        self._calculate_opponents()

    def _get_or_create_politician(self, name):
        key = name.strip().upper()

        if key in self.politicians:
            return self.politicians[key]

        info = get_politician_info(key)
        if info is None:
            raise ValueError(f"Политик '{name}' не найден в POLITICIANS_DATA")

        politician = Politician(
            csv_key = key,
            name = info["full_name"],
            party = info["party"],
            date_of_birth = info["date_of_birth"],
            gender = info["gender"]
        )
        self.politicians[key] = politician
        return politician

    
    def _create_debate(self, row):
        debate_date = pd.to_datetime(row['date']).date()
        debate_type = DebateType.PRIMARIES if 'primary' in row['election_type'].lower() else DebateType.GENERAL
        return Debate(
            name = row['title'],
            link = row['link'],
            debate_type = debate_type,
            debate_date = debate_date,
            place = row['place'])
    
    def _calculate_opponents(self):
        for debate in self.debates:
            politicians = debate.politicians
            
            for politician in politicians:
                for opponent in politicians:
                    if opponent != politician:
                        if opponent.name not in politician.opponents:
                            politician.opponents[opponent.name] = 0
                        politician.opponents[opponent.name] += 1