import json
from difflib import get_close_matches
data = json.load(open("dictionary.json"))


def search(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        print("Did you mean {} instead? ".format(get_close_matches(word, data.keys())[0]))
        decide = input("Press yes for y or n for no: ")
        if decide is "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif decide is "n":
            return "We didn't understand your entry"
        else:
            return "You have entered wrong input please press y or n"
    else:
        return "{} does not exists in dictionary".format(word)


word = input("Enter the word to find: ")

output = search(word)
if type(output) is list:
    for item in output:
        print(item)
else:
    print(output)