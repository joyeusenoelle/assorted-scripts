import sys

def replaceText(words):
	""" Replaces each word in a sentence with the first letter, length of interstitial letters, and last letter. """
	new_words = []
	try:
		words = words.split(" ")
	except:
		words = words
	for word in words:
		if len(word) <= 2:
			new_words.append(word)
		else:
			if word[-1] in (".",",","?","!",":"):
				l = len(word) - 3
				new_words.append("{}{}{}{}".format(word[0],l,word[-2],word[-1]))
			else:
				l = len(word) - 2
				new_words.append("{}{}{}".format(word[0],l,word[-1]))
	return " ".join(new_words)

if __name__ == "__main__":
	text = sys.argv[1:]
	print(replaceText(text))