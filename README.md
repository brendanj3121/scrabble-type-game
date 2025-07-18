# First Word: An Arcade Word Game
    #### Video Demo:  <https://www.youtube.com/watch?v=fJeo2aIBInw>
### Description:

Welcome to First Word! This program is a one-turn, single-player, Scrabble arcade game. User's will be given random letter tiles, asked to use those tiles to form a word, and then given a score from the word played.

### class Player:

The Player class contains three lists: "bag", "pull", and "blanks".

"Bag" is a simulated Scrabble tile bag.

"Pull" is an empty list that gets filled by the __draw__ function. This is used in the __validate__ funtion.

"Blanks" is an empty list that gets filled by "blank" tiles used. The player may use any letter for  " " in *Player.pull*, and that letter will be populated in *Player.blanks*. This is used in the __score__ function.

The Player class is initialized with a *name* (default __None__), and a *points* value of 0.

### draw(n)

__Draw__ function uses *random* library to generate *n* random tiles from *Player.bag*. Tiles are placed in *Player.pull*

`player.pull.extend(random.sample(player.bag, n))`

### validate(word)

__Validate__ function checks that only tiles available from *Player.pull* are input by the user.

First, empty list *validation* is populated with tiles from *Player.pull*. Having this list populate every time __validate()__ is called allows for use of a while loop without removing items from *Player.pull*.

__Validate__ iterates over each character in argument. It checks that the letter is in *validation* list, then removes that character from list and subtracts 1 from character counter `x = len(word)`

If character not in *validation*, validate checks for blank tiles. If blank tile " " is used, character is appended to *Player.blanks*.

If character not in *validation* and there are no blank tiles, __validate__ returns *False*.

When character counter `x  == 0`, __validate__ returns *True*.

```
validation = []
    validation.extend(player.pull)
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
```
### score(word)

__Score__ adds to and returns *Player.points* to the user based on the given word argument.

First, `if word.lower() in words.words():` utilizes *words* from the nltk.corpus module. This checks if the word argument exists in the English dictionary. If not, zero points returned to user.

Imported and downloaded as follows:

```
import nltk
nltk.download("words", quiet=True)
from nltk.corpus import words
```

If user uses all tiles, 50 bonus points are awarded.
```
if len(word) == len(player.pull):
                player._points += 50
```
__Score__ then iterates over all characters in word argument, and adds to *Player._points* based on letter value (from Scrabble's rules). Before checking letter value, __score__ checks if the character is in the *Player.blanks* list. If it is, __score__ will remove character from *Player.blanks* and award 0 points for character.

### highscore(name, score)

__High_score__ keeps track of all users who have played __First Word__ and their scores. It returns the user with the highest score.

First, __high_score__ utilizes *csv* library to write *Player.name* and *Player._points* to __high_score.csv__. This utilizes csv.Dictwriter.writerow as follows:
```
with open("high_score.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "score"])
        writer.writerow({"name": name, "score": score})
```

__High_score__ then iterates over each row of *high_score.csv*, reading score values, and comparing them against each other to find the highest score. This utilizes csv.reader as follows:

```
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
```

### main()
This is where the game happens!

First, *Player.name* is assigned with an input function.

__Draw__ is used to generate tiles for the user: `print("Your letters:", draw(7))`

__Validate__ is used within while loop. This prevents user from inputting characters outside of their available letters in *Player.pull*.

```
while True:
        play = input("Your word: ")
        if validate(play) == True:
            break
        else:
            print("Use available tiles")
            pass
```

__Score__ returns player their points.

__High_score__ returns player the player with the highest score (so far).


# Thanks for playing!
