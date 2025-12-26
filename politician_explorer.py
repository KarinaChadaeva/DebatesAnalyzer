import pandas as pd
from collections import Counter
from helper_functions import preprocess_texts, sentiment_distribution


class PoliticianExplorer:
    def __init__(self, parser):
        self.parser = parser
    
    def show_politician_info(self, surname, top_n_words = 15):
        p = self._get_politician(surname)
        debates = p.debates_participated

        self._print_header(f"POLITICIAN PROFILE: {p.csv_key} ({p.name})")
        self._print_basic_info(p)

        self._print_debates_for_politician(p, debates)
        self._print_opponents(p, top_k=None)

        self._print_top_words_for_politician(p, debates, top_n_words)
        self._print_sentiment_for_politician(p, debates)

    
    def compare_two_politicians(self, politician1_surname, politician2_surname, top_n_words = 15):
        p1 = self._get_politician(politician1_surname)
        p2 = self._get_politician(politician2_surname)

        self._print_header(f"COMPARE: {p1.csv_key} ({p1.name}) vs {p2.csv_key} ({p2.name})")

        stats1 = self._collect_stats(p1, p1.debates_participated, label=p1.csv_key)
        stats2 = self._collect_stats(p2, p2.debates_participated, label=p2.csv_key)

        df = pd.DataFrame([stats1, stats2])
        print(df.to_string(index=False, max_colwidth=40, justify="left"))

        print(f"\n-----TOP WORDS (TOP-{top_n_words})-----")
        print(f"\n{p1.csv_key}:")
        self._print_top_words_from_texts(self._texts_for_politician(p1, p1.debates_participated), top_n_words)

        print(f"\n{p2.csv_key}:")
        self._print_top_words_from_texts(self._texts_for_politician(p2, p2.debates_participated), top_n_words)


    def compare_politician_in_two_groups(self, 
                                         politician_surname, 
                                         group_a,
                                         group_b,
                                         group_a_name = "GROUP A",
                                         group_b_name = "GROUP B",
                                         top_n_words = 15):

        p = self._get_politician(politician_surname)

        group_a = [d for d in group_a if p in getattr(d, "politicians", [])]
        group_b = [d for d in group_b if p in getattr(d, "politicians", [])]

        self._print_header(f"COMPARE WITHIN POLITICIAN: {p.csv_key} ({p.name})")
        print(f"{group_a_name}: {len(group_a)} debates")
        print(f"{group_b_name}: {len(group_b)} debates")

        stats_a = self._collect_stats(p, group_a, label=group_a_name)
        stats_b = self._collect_stats(p, group_b, label=group_b_name)

        df = pd.DataFrame([stats_a, stats_b])
        print("\n-----COMPARISON TABLE-----")
        print(df.to_string(index=False, max_colwidth=40, justify="left"))

        print(f"\n-----TOP WORDS (TOP-{top_n_words})-----")
        print(f"\n{group_a_name}:")
        self._print_top_words_from_texts(self._texts_for_politician(p, group_a), top_n_words)

        print(f"\n{group_b_name}:")
        self._print_top_words_from_texts(self._texts_for_politician(p, group_b), top_n_words)

    
    def _get_politician(self, key):
        key = key.strip().upper()
        if key not in self.parser.politicians:
            raise KeyError(f"Unknown politician: {key}")
        return self.parser.politicians[key]

    def _texts_for_politician(self, p, debates):
        texts = []
        for d in debates:
            for u in d.utterances:
                if getattr(u.speaker, "csv_key", None) == p.csv_key and u.text:
                    texts.append(u.text)
        return texts

    def _collect_stats(self, p, debates, label):
        texts = self._texts_for_politician(p, debates)
        n_utts = len(texts)
        avg_len = (sum(len(t.split()) for t in texts) / n_utts) if n_utts else 0.0
        sent = sentiment_distribution(texts)

        return {
            "label": label,
            "n_debates": len(debates),
            "n_utterances": n_utts,
            "avg_utt_len": round(avg_len, 2),
            "pos": round(sent["positive"], 4),
            "neg": round(sent["negative"], 4),
            "neu": round(sent["neutral"], 4)}

    def _print_top_words_for_politician(self, p, debates, top_n_words):
        print(f"\n-----MOST COMMON WORDS for {p.csv_key} (TOP-{top_n_words})-----")
        self._print_top_words_from_texts(self._texts_for_politician(p, debates), top_n_words)

    def _print_top_words_from_texts(self, texts, top_n_words):
        clean_texts = preprocess_texts(texts)
        c = Counter()
        for t in clean_texts:
            c.update(t.split())

        if not c:
            print("(no tokens)")
            return

        for word, count in c.most_common(top_n_words):
            print(f"{word:<18} {count}")

    def _print_sentiment_for_politician(self, p, debates):
        print(f"\n-----SENTIMENT for {p.csv_key}-----")
        self._print_sentiment_from_texts(self._texts_for_politician(p, debates))

    def _print_sentiment_from_texts(self, texts):
        stats = sentiment_distribution(texts)
        if stats["total"] == 0:
            print("(no utterances)")
            return

        print(f"Total utterances: {stats['total']}")
        print(f"Positive: {stats['positive']:.2%}")
        print(f"Negative: {stats['negative']:.2%}")
        print(f"Neutral:  {stats['neutral']:.2%}")

    def _print_header(self, title: str):
        line = "=" * len(title)
        print(f"\n{line}\n{title}\n{line}")

    def _print_basic_info(self, p):
        print("\n-----BASIC INFO-----")
        party = getattr(p.party, "value", p.party)
        gender = getattr(p.gender, "value", p.gender)
        print(f"csv_key: {p.csv_key}")
        print(f"name:    {p.name}")
        print(f"party:   {party}")
        print(f"gender:  {gender}")
        print(f"dob:     {p.date_of_birth}")
        print(f"debates: {len(p.debates_participated)}")


    def _print_debates_for_politician(self, p, debates):
        print("\n-----DEBATES-----")
        rows = []
        for d in sorted(debates, key=lambda x: x.date):
            opponents = [pp.csv_key for pp in d.politicians if pp.csv_key != p.csv_key]
            rows.append({
                "date": d.date,
                "type": d.debate_type.value,
                "opponents": ", ".join(opponents) if opponents else "(none)",
                "title": d.full_name})

        df = pd.DataFrame(rows)[["date", "type", "opponents", "title"]]
        print(df.to_string(index=False, max_colwidth=60, justify="left"))


    def _print_opponents(self, p, top_k=None):
        print("\n-----OPPONENTS-----")
        if not p.opponents:
            print("(empty)")
            return

        items = sorted(p.opponents.items(), key=lambda x: x[1], reverse=True)
        if top_k is not None:
            items = items[:top_k]

        for name, cnt in items:
            print(f"{name:<25} {cnt}")