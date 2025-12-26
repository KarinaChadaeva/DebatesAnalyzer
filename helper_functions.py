import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download("vader_lexicon")

STOP_WORDS = set(stopwords.words("english"))
CUSTOM = {"would", "one", "let", "two", "way", "take", "never", "look", "like",
          "done", "well", "back", "us", "first", "think", "know", "believe", "want", "say", "said", "tell",
          "make", "made", "get", "got", "going", "go", "today", "now", "years", "year", "time", "question", "answer", "moderator"}

STOP_WORDS = STOP_WORDS | CUSTOM

def preprocess_texts(texts):
    clean_texts = []

    for text in texts:
        if not text:
            continue

        tokens = word_tokenize(text.lower())
        filtered = [t for t in tokens if t.isalpha() and t not in STOP_WORDS]

        if filtered:
            clean_texts.append(" ".join(filtered))

    return clean_texts


def sentiment_distribution(texts):
    _SIA = SentimentIntensityAnalyzer()
    pos = neg = neu = total = 0

    for text in texts:
        if not text:
            continue

        scores = _SIA.polarity_scores(text)
        total += 1

        if scores["compound"] >= 0.05:
            pos += 1
        elif scores["compound"] <= -0.05:
            neg += 1
        else:
            neu += 1

    if total == 0:
        return {
            "positive": 0.0,
            "negative": 0.0,
            "neutral": 0.0,
            "total": 0,
        }

    return {
        "positive": pos / total,
        "negative": neg / total,
        "neutral": neu / total,
        "total": total,
    }