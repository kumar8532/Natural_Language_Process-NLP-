# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 11:06:37 2026

@author: prince yadav
"""


import nltk
import re
from gensim.models import Word2Vec
from nltk.corpus import stopwords

# Run these downloads once if needed
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

paragraph = """I have three visions for India. In 3000 years of our history,
people from all over the world have come and invaded us, captured our lands,
conquered our minds. From Alexander onwards, the Greeks, the Turks, the Moguls,
the Portuguese, the British, the French, the Dutch, all of them came and looted
us, took over what was ours. Yet we have not done this to any other nation.
We have not conquered anyone. We have not grabbed their land, their culture,
their history and tried to enforce our way of life on them. Why? Because we
respect the freedom of others. That is why my first vision is that of freedom.
I believe that India got its first vision of this in 1857, when we started
the War of Independence. It is this freedom that we must protect and nurture
and build on. If we are not free, no one will respect us. My second vision
for India’s development. For fifty years we have been a developing nation.
It is time we see ourselves as a developed nation. We are among the top 5
nations of the world in terms of GDP. We have a 10 percent growth rate in
most areas. Our poverty levels are falling. Our achievements are being
globally recognised today. Yet we lack the self-confidence to see ourselves
as a developed nation, self-reliant and self-assured. Isn’t this incorrect?
I have a third vision. India must stand up to the world. Because I believe
that unless India stands up to the world, no one will respect us. Only
strength respects strength. We must be strong not only as a military power
but also as an economic power. Both must go hand-in-hand. My good fortune
was to have worked with three great minds. Dr. Vikram Sarabhai of the Dept.
of space, Professor Satish Dhawan, who succeeded him and Dr. Brahm Prakash,
father of nuclear material. I was lucky to have worked with all three of
them closely and consider this the great opportunity of my life.
I see four milestones in my career"""

# Preprocessing
text = re.sub(r'\[[0-9]*\]', ' ', paragraph)
text = re.sub(r'\s+', ' ', text)
text = text.lower()
text = re.sub(r'\d', ' ', text)
text = re.sub(r'\s+', ' ', text)

# Tokenize sentences and words
sentences = nltk.sent_tokenize(text)
sentences = [nltk.word_tokenize(sentence) for sentence in sentences]

# Remove stopwords
stop_words = set(stopwords.words('english'))
sentences = [
    [word for word in sentence if word not in stop_words]
    for sentence in sentences
]

# Train Word2Vec model
model = Word2Vec(
    sentences,
    min_count=1,
    vector_size=100,
    window=5,
    workers=4
)

# Get vocabulary
words = list(model.wv.key_to_index.keys())
print("Vocabulary:", words[:20])

# Find word vector
if 'war' in model.wv:
    vector = model.wv['war']
    print("\nWar vector shape:", vector.shape)
    print("War vector:", vector)

# Find most similar words
if 'vikram' in model.wv:
    similar = model.wv.most_similar('vikram', topn=5)
    print("\nWords similar to vikram:")
    print(similar)
else:
    print("'vikram' vocabulary mein nahi mila.")








