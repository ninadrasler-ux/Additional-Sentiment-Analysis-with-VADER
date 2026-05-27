
import nltk

nltk.download('vader_lexicon')

from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

chapters = [
    "down_the_rabbit_hole.txt",
    "mad_tea_party.txt",
    "queens_croquet_ground.txt"
]

for chapter in chapters:
    with open(chapter, "r", encoding="utf-8") as f:
        text = f.read()

    scores = sia.polarity_scores(text)

    print(chapter)
    print(f"Positive: {scores['pos']}")
    print(f"Negative: {scores['neg']}")
    print(f"Neutral: {scores['neu']}")
    print(f"Compound: {scores['compound']}")
