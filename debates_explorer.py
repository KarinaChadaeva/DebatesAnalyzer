import pandas as pd
from collections import Counter
from helper_functions import preprocess_texts, sentiment_distribution

INCLUDES = {'most_common_words', 'emotions', 'all'}


class DebateExplorer:
    def __init__(self, debates, include: list[str] = None, top_n_words = 10):
        self.debates = debates
        self.include = include
        self.top_n = top_n_words

    def show_debates_stats(self):
        include_set = self._normalize_include()
        self._base_stats()

        if 'most_common_words' in include_set:
            self._calculate_most_common()
        
        if 'emotions' in include_set:
            self._calculate_emotions()
        

    def _normalize_include(self):
        if self.include is None:
            return set()
        include_set = {str(x).strip().lower() for x in self.include if x and str(x).strip()}
        unknown = include_set - INCLUDES
        if unknown:
            raise ValueError(f"Unknown values: {sorted(unknown)}. Allowed: {sorted(INCLUDES)}")
        if "all" in include_set:
            return INCLUDES - {"all"}
        return include_set
    
    def _base_stats(self):
        print("\n-----BASE DEBATE(S) INFO-----")
        rows = []
        for d in self.debates:
            n_utts = len(d.utterances)
            avg_len = (sum(len(str(u.text).split()) for u in d.utterances) / n_utts if n_utts else 0.0)
            rows.append({
                "date": d.date,
                "type": d.debate_type.value,
                "politicians": ", ".join(p.csv_key for p in d.politicians),
                "utterances": n_utts,
                "avg_len": round(avg_len, 2),
                "title": d.full_name})

        df = pd.DataFrame(rows)
        df = df[["date", "type", "politicians", "utterances", "avg_len", "title"]]
        print(df.to_string(index=False, max_colwidth=40, justify="left"))
    
    def _calculate_most_common(self):
        print(f"\n-----MOST COMMON WORDS (TOP-{self.top_n})-----")
        raw_texts = [u.text for d in self.debates for u in d.utterances]
        clean_texts = preprocess_texts(raw_texts)
        c = Counter()
        for t in clean_texts:
            c.update(t.split())

        for word, count in c.most_common(self.top_n):
            print(f"{word:<18} {count}")

    def _calculate_emotions(self):
        print(f"\n-----SENTIMENT ANALYSIS-----")
        texts = [u.text for d in self.debates for u in d.utterances]
        stats = sentiment_distribution(texts)

        print(f"Total utterances count: {stats['total']}")
        print(f"Positive: {stats['positive']:.2%}")
        print(f"Negative: {stats['negative']:.2%}")
        print(f"Neutral: {stats['neutral']:.2%}")
