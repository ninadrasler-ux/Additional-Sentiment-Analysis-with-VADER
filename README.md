# Sentiment Analysis of Three Chapters from *Alice’s Adventures in Wonderland*

This project explores the sentiment of three chapters from *Alice’s Adventures in Wonderland* using two complementary approaches:

1. **Manual sentiment sets** (custom positive/negative word lists)
2. **VADER** (Valence Aware Dictionary and sEntiment Reasoner), a rule‑based sentiment tool developed for modern online text

The goal is to compare how classical literary prose is interpreted by a manual, context‑aware method versus an automated tool optimized for short, informal, contemporary language.

---

## Chapters Analyzed

- *Down the Rabbit-Hole*  
- *A Mad Tea-Party*  
- *The Queen’s Croquet-Ground*

The text files are included in the repository.

---

## Methodology

### 1. Manual Sentiment Sets  
I created two small lexical sets (positive and negative) and counted occurrences in each chapter.  
This approach captures:

- subtle emotional cues  
- narrative tension  
- context-dependent negativity (confusion, fear, frustration)  
- tone shifts that are not lexically explicit  

### 2. VADER Sentiment Analysis  
VADER was applied to the full text of each chapter.  
It returns four scores:

- **pos** — proportion of positive sentiment  
- **neg** — proportion of negative sentiment  
- **neu** — proportion of neutral sentiment  
- **compound** — overall polarity from –1 to +1  

VADER is designed for **social media**, not classical literature, which becomes important in the interpretation.

**Note:** VADER was applied to the raw, uncleaned text of each chapter, whereas the manual sentiment sets were applied to a cleaned version (lowercased, stripped of punctuation, and normalized). This methodological difference is intentional: it highlights how automated tools behave on unprocessed literary prose compared to a curated, context-sensitive manual approach.

---

## VADER Results

| Chapter                     | Positive | Negative | Neutral | Compound |
|-----------------------------|----------|----------|---------|----------|
| Down the Rabbit-Hole       | 0.104    | 0.073    | 0.823   | 0.9977   |
| A Mad Tea-Party            | 0.072    | 0.068    | 0.860   | 0.9562   |
| The Queen’s Croquet-Ground | 0.099    | 0.079    | 0.822   | 0.9970   |

All three chapters receive **very high positive compound scores**, despite containing confusion, conflict, absurdity, and emotionally mixed scenes.

---

## Manual vs. VADER: Key Differences

### Manual sentiment sets
- More balanced distribution of positive and negative cues  
- Capture subtle tension, confusion, fear, frustration  
- Sensitive to narrative context and tone  
- Do not treat whimsical or absurd language as inherently positive  

### VADER
- Strong bias toward **positive interpretation**  
- Interprets many neutral or playful expressions as mildly positive  
- Cannot detect irony, satire, or social discomfort  
- Optimized for short, explicit, modern online language  

### Key Insight  
The manual approach detects a **mixed emotional landscape**, while VADER produces an almost uniformly **positive polarity**.  
This highlights how sentiment tools behave differently depending on the genre they were designed for.

---

## Chapter-by-Chapter Interpretation

Before looking at each chapter individually, it is important to note that *Alice’s Adventures in Wonderland* belongs to the genre of **literary nonsense**. The narrative deliberately disrupts logic, meaning, and conversational norms. Because VADER relies on surface-level lexical cues and was designed for modern, explicit online language, it cannot recognize nonsense, irony, absurdity, or destabilized semantics. As a result, it systematically misinterprets the tone of the text as overwhelmingly positive.

### 1. Down the Rabbit-Hole  
VADER assigns an almost fully positive compound score (0.9977).  
This is likely due to:

- playful, imaginative vocabulary  
- lack of explicit negative markers  
- whimsical narrative tone  

The manual set captures more negative or tense elements such as disorientation, fear of the unknown, and confusion.

---

### 2. A Mad Tea-Party  
Although the scene is chaotic and socially uncomfortable, VADER returns a highly positive score (0.9562).

Reasons:

- playful rather than aggressive wording  
- implicit rather than explicit negativity  
- inability to detect social tension or absurdity  

The manual approach identifies more frustration, conflict, and emotional discomfort.

---

### 3. The Queen’s Croquet-Ground  
Despite threats (“Off with her head!”), chaos, and tension, VADER assigns a near-perfect positive score (0.9970).

This happens because:

- VADER does not interpret threats contextually  
- irony and satire are not recognized  
- surface-level vocabulary is not strongly negative  

The manual set detects negative cues related to fear, authority, and conflict.

---

## Summary

This comparison shows that:

- VADER is **not well-suited for classical literary prose**, where tone is subtle and context-dependent.  
- Manual sentiment sets capture narrative dynamics and emotional complexity more accurately.  
- Tool choice significantly shapes interpretation.

---

## Next Steps

Future work will apply VADER (and possibly other sentiment tools) to **more contemporary texts**—online comments, forums, short posts, and news—domains where VADER’s design assumptions align more closely with the linguistic characteristics of the data.

---

## Code

The analysis script is included in the repository:

- `alice_three_chapters_analysis.py` — manual sentiment sets  
- `alice_VADER_analysis.py` — VADER sentiment analysis

Both scripts operate on the three text files in the `/texts` directory.


