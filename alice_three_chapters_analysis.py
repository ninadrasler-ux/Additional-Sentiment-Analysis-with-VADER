import re
import nltk

from nltk.corpus import stopwords

stop_words = stopwords.words('english')

chapters = [
    "down_the_rabbit_hole.txt",
    "mad_tea_party.txt",
    "queens_croquet_ground.txt"
]

for chapter in chapters:
    with open(chapter, "r", encoding="utf-8") as f:
        text = f.read()

    text = text.replace('“', '"').replace('”', '"')

    text = text.lower()

    text = re.sub(r"[^\w\s]", " ", text)

    words = text.split()

    filtered_words = [word for word in words if word not in stop_words]

    total_words = len(filtered_words)

    positive_words = {"happy", "merry", "wonderful", "beautiful", "joy", "joyful", "love", "happiness", "glad", "satisfied", "pleased", "delightful", "laughter"}

    negative_words = {"sad", "ugly", "horrible", "unhappy", "dreadful", "angry", "hate", "fear", "frightened", "afraid", "frantic", "horror", "mad"}

    positive_count = 0

    negative_count = 0

    found_positive = []

    found_negative = []

    for word in filtered_words:
        if word in positive_words:
            positive_count += 1
            found_positive.append(word)
        if word in negative_words:
            negative_count += 1
            found_negative.append(word)

    positive_density = (positive_count / total_words) * 1000

    negative_density = (negative_count / total_words) * 1000

    print(chapter)
    print(f"Positive words: {positive_count}")
    print(f"Negative words: {negative_count}")
    print(f"Found positive: {found_positive}")
    print(f"Found negative: {found_negative}")
    print(f"Positive density: {positive_density:.2f}")
    print(f"Negative density: {negative_density:.2f}")
