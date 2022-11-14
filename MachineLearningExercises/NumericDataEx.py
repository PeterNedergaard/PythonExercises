from sklearn.preprocessing import OneHotEncoder
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

text = open("moby_dick.txt", "r", encoding="utf8")

vectorizer = CountVectorizer()

fit = vectorizer.fit_transform(text)
res = fit.todense()
wood_idx = vectorizer.vocabulary_['wood']
wood_count = sum(res[:, wood_idx])

print("'wood' occurs " + str(wood_count) + " times")
