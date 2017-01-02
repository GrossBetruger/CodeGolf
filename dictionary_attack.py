import json 
from itertools import combinations 


ENGLISH_WORDS_FILENAME = "english_words.json"


def load_words():
	with open(ENGLISH_WORDS_FILENAME, "rb") as f:
		return json.load(f)



def build_ngram(n, dictionary):
	return list(combinations(dictionary, n))


if __name__=="__main__":
	twowords = build_ngram(2, load_words())
	for i in twowords[:100]:
		print i


