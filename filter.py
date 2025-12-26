from enums import DebateType
from parser import DebateParser


class DebateFilter:
    def __init__(self, parser: DebateParser):
        self.debates = parser.debates

    def filter_debates(self, 
                       years: list[int] = None, 
                       debate_type: DebateType = None,
                       politicians: list[str] = None,
                       both: bool = False,):
        filtered = self.debates.copy()

        if years:
            filtered = [d for d in filtered if d.year in years]

        if debate_type:
            filtered = [d for d in filtered if d.debate_type == debate_type]

        if politicians:
            wanted = {p.strip().upper() for p in politicians if p and p.strip()}

            if both and len(wanted) == 2:
                filtered = [d for d in filtered if wanted.issubset({p.csv_key for p in d.politicians})]
            else:
                filtered = [d for d in filtered if len({p.csv_key for p in d.politicians} & wanted) > 0]

        return filtered