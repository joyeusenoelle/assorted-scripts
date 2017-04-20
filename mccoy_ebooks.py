import random
from twython import Twython

def get_word():
    with open("nounlist.txt") as file:
        nouns = file.read().split("\n")
    noun = random.choice(nouns)
    nouns.pop(nouns.index(noun))
    with open("nounlist.txt","w") as file:
        file.write("\n".join(nouns))
    return articleize(noun)

def articleize(word):
    if word[0] in ["a","e","i","o","u"]:
        return "an {}".format(word)
    return "a {}".format(word)

def main():
    tweet = "I'm a doctor, not {}!".format(get_word())
    try:
        twitter = Twython() #Twitter credentials redacted, obviously
        twitter.update_status(status=tweet)
        print("Updated: {}".format(tweet))
    except:
        print("Couldn't tweet {}".format(tweet))

if __name__ == "__main__":
    main()
