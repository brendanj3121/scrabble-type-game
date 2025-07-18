import random
import nltk
nltk.download("words", quiet=True)
from nltk.corpus import words
import csv

class Player:

    bag = ["j", "k", "q", "x", "z" * 1] + \
(["b", "c", "f", "h", "m", "p", "v", "w", "y", " "] * 2) + \
(["g"] * 3) + \
(["d", "l", "s", "u"] * 4) + \
(["n", "r", "t"] * 6) + \
(["o"] * 8) + \
(["a", "i"] * 9) + \
(["e"] * 12)

    pull = []
    blanks = []

    def __init__(self, name=None):
        #Initializes player's name and starts them with zero points
        self.name = name
        self._points = 0

    @property
    def points(self):
        return self._points

player = Player()

def main():
    player.name = input("Name: ")
    print("Your letters:", draw(7))
    while True:
        play = input("Your word: ")
        if validate(play) == True:
            break
        else:
            print("Use available tiles")
            pass
    print("Score:", score(play))
    high_score(player.name, player._points)


def draw(n):
    #Draw random tiles from Scrabble bag. Default to 7 tiles without given n value.
    player.pull.extend(random.sample(player.bag, n))
    return player.pull

def validate(word):
    #Validates that user input only includes available tiles.
    #Should only be used after draw is used to randomly generate tiles
    validation = []
    validation.extend(player.pull)
    # This allows for checking if only available tiles are used without removing from self.pull.
    # While loop can be used for validation.
    x = len(word)
    for c in word.lower():
        if c in validation:
            validation.remove(c)
            x -= 1
            if x == 0:
                return True
            else:
                pass
        elif " " in validation:
            validation.remove(" ")
            x -= 1
            player.blanks.append(c)
            if x == 0:
                return True
            else:
                pass
        else:
            player.blanks.clear()
            return False

def score(word):
    #Scores user's word. Word must be in English dictionary to earn points.
    #If all letters are used, user earns 'Scrabble!', + 50 points
    if word.lower() in words.words():
        if len(word) == len(player.pull):
                player._points += 50
        for c in word:
            if c in player.blanks:
                player.blanks.remove(c)
                pass
            elif c in "aeioulnstr":
                player._points += 1
            elif c in "dg":
                player._points += 2
            elif c in "bcmp":
                player._points += 3
            elif c in "fhvwy":
                player._points += 4
            elif c in "k":
                player._points += 5
            elif c in "jx":
                player._points += 8
            elif c in "qz":
                player._points += 10
        return player._points
    else:
        return player._points

def high_score(name, score):
    with open("high_score.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "score"])
        writer.writerow({"name": name, "score": score})

    with open("high_score.csv") as file:
        high = 0
        reader = csv.reader(file)
        for row in reader:
            score = int(row[1])
            if score > high:
                high = score
                high_score = row
            else:
                pass
        print("High score:", *high_score)

if __name__ == "__main__":
    main()
