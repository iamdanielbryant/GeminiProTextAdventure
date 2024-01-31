import requests

badwordfile = "https://www.cs.cmu.edu/~biglou/resources/bad-words.txt"

req = requests.get(badwordfile)
wordlist = str(req.content).split("\\n")
wordlist.pop(0)

def checkForBadwords(text):
    for word in text.split():
        for badword in wordlist:
            if word.lower() == badword.lower():
                return True
    return False