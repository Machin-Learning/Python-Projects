# import json
import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        q = input(f"Do you mean by press Y|n {get_close_matches(word, data.keys())[0]}")
        if q == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        else:
            print("The word is not in dictionary")

    else:
        print("The word is not in dictionary")

    

word = input("Enter the word you want to search: ")

output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)