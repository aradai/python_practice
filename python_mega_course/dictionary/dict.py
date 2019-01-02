#!/usr/bin/env python3

import json
import difflib

def json_to_dict(name):
    return json.load(open(name, "r"))

def search(dict, string):
    try:
        #return dict[string]
        if string.lower() in dict.keys():
            i = 1
            for value in dict[string.lower()]:
                print(str(i) + ".: " + value)
                i = i + 1
        elif string.title() in dict.keys():
            i = 1
            for value in dict[string.title()]:
                print(str(i) + ".: " + value)
                i = i + 1
        elif string.upper() in dict.keys():
            i = 1
            for value in dict[string.upper()]:
                print(str(i) + ".: " + value)
                i = i + 1
        else:
            raise KeyError
    except KeyError:
        answ = "n"
        for word in difflib.get_close_matches(string.lower(), dict.keys(), cutoff = 0.6):
            answ = input("Is your word {0}? Yes[y] or no[n]? ".format(word))
            while answ != "y" and answ != "n":
                answ = input("Choose between 'y' and 'n': ")
            if answ == "y":
                #return dict[word]
                i = 1
                for value in dict[word]:
                    print(str(i) + ".: " + value)
                    i = i + 1
                break
        if answ == "n":        
            for word in difflib.get_close_matches(string.upper(), dict.keys(), cutoff = 0.6):
                answ = input("Is your word {0}? Yes[y] or no[n]? ".format(word))
                while answ != "y" and answ != "n":
                    answ = input("Choose between 'y' and 'n': ")
                if answ == "y":
                    #return dict[word]
                    i = 1
                    for value in dict[word]:
                        print(str(i) + ".: " + value)
                        i = i + 1
                    break

        if answ == "n":   
            print("This word is not in the dictionary")

data = json_to_dict("data.json")

word = input("The word you looking for: ")

search(data, word)