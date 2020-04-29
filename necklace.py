#!/usr/bin/env python
# Seeing if one necklace can be made from another

def same_necklace(first, second):
    if len(first) == 0 and len(second) == 0:
        return True
    elif len(first) == 0 and len(second) != 0:
        return False
    elif len(second) == 0 and len(first) != 0:
        return False
    else:
        first = list(first)
        second = list(second)
    
        for letter in first:
            second.append(second[0])
            second.pop(0)
            if first == second:
                return True
        return False

# Bonus 1 to see how many times the original string is repeated when each bead is moved
# to the other side exactly once
def repeats(word):
    if len(word) == 0:
        numberRepeats = 1
        return numberRepeats
    else:
        word = list(word)
        original = list(word)
        numberRepeats = 0

        for letter in word:
            word.append(word[0])
            word.pop(0)
            if word == original:
                numberRepeats += 1
        return numberRepeats
