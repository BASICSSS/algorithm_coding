
from collections import Counter

word = "Mississipi"
print(word.upper())

word_counter = Counter(word.upper())  # MISSISSIPI
print(word_counter)

print(word_counter['M'])
print(word_counter["A"])
print(word_counter.get("A"))
print(word_counter[('M', 'S')]);

print(word_counter.most_common(2))
most_word = word_counter.most_common()

print(most_word)