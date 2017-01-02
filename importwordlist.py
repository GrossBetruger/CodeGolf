import requests
import json 

WORDLIST_URL = "http://norvig.com/ngrams/word.list"
WORDLIST_FILENAME = "english_words.json"

def importwords():
	raw = requests.get(WORDLIST_URL)
	return raw.text.split("\n")


def dumplist(wordlst, filename):
	with open(filename, "wb") as f:
		json.dump(wordlst, f)


def read_wordlist(filename): 
	with open(filename, "rb") as f:
		return json.load(f)


if __name__=="__main__":
	# words = importwords()
	# dumplist(words, WORDLIST_FILENAME)
	wordlst = read_wordlist(WORDLIST_FILENAME)
	for wrd in wordlst:
		print wrd 
	print "number of words in list:", "{:,}".format(len(wordlst))