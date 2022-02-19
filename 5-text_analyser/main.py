"""
Βάλτε το αρχείο μέσα στον φάκελο με όνομα text.txt
Αυτό το πρόγραμμα χρειάζεται να είναι εγκατεστημένες οι βιβλιοθήκες numpy και pandas
"""

import numpy as np
import pandas as pd
import collections

with open("text.txt", "r") as f:
    text = []
    for line in f:
        for i in range(33, 65):
            line = line.replace(chr(i), " ")
        for i in range(91, 97):
            line = line.replace(chr(i), " ")
        for i in range(122, 127):
            line = line.replace(chr(i), " ")
        line = line.lower()
        text += line.split()

def run(arr, x):
    counter = collections.Counter(arr)
    word_series = pd.Series(counter, counter.keys())
    word_series = word_series.sort_values(ascending=False)
    result = word_series.head(x)
    print(result)



run(text, 10)
print()
two_letters = [word[:2] for word in text]
run(two_letters, 3)
print()
three_letters = [word[:3] for word in text]
run(three_letters, 3)

