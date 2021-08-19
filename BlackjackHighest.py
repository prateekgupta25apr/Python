"""
Blackjack Highest

Question :
Have the function BlackjackHighest(strArr) take the strArr parameter being passed which
will be an array of numbers and letters representing blackjack cards. Numbers in the
array will be written out. So for example strArr may be ["two","three","ace","king"].
The full list of possibilities for strArr is: two, three, four, five, six, seven, eight,
nine, ten, jack, queen, king, ace. Your program should output below, above, or blackjack
signifying if you have blackjack (numbers add up to 21) or not and the highest card in
your hand in relation to whether or not you have blackjack. If the array contains an
ace but your hand will go above 21, you must count the ace as a 1. You must always try
and stay below the 21 mark. So using the array mentioned above, the output should be
below king. The ace is counted as a 1 in this example because if it wasn't you would
be above the 21 mark.

Another example would be if strArr was ["four","ten","king"], the output here
should be above king. If you have a tie between a ten and a face card in your hand,
return the face card as the "highest card". If you have multiple face cards, the order
of importance is jack, queen, king.


Examples

Input: ["four","ace","ten"]
Output: below ten

Input: ["ace","queen"]
Output: blackjack ace
"""


def BlackjackHighest(s):
    # List to hold the value of the cards
    cards = list()

    # Booleans to specify do we have "jack", "queen", "king" or "ace"
    isJack = False
    isQueen = False
    isKing = False
    isAce = False

    # Variable to specify how many ace we have
    aceCount = 0

    # Traversing through s
    for i in range(len(s)):

        # Checking for card name and appending card values to list cards accordingly
        if s[i] == "two":
            cards.append(2)
        elif s[i] == "three":
            cards.append(3)
        elif s[i] == "four":
            cards.append(4)
        elif s[i] == "five":
            cards.append(5)
        elif s[i] == "six":
            cards.append(6)
        elif s[i] == "seven":
            cards.append(7)
        elif s[i] == "eight":
            cards.append(8)
        elif s[i] == "nine":
            cards.append(9)
        elif s[i] == "ten":
            cards.append(10)
        elif s[i] == "jack":
            isJack = True
            cards.append(10)
        elif s[i] == "queen":
            isQueen = True
            cards.append(10)
        elif s[i] == "king":
            isKing = True
            cards.append(10)
        elif s[i] == "ace":
            aceCount += 1
            cards.append(1)

    # Totaling all the values in "cards" list
    total = sum(cards)

    # Checking for Ace value
    if (total + 10) <= 21:
        total += 10
        isAce = True

    # Preparing result
    result = ""
    if total == 21:
        result = "blackjack"
    elif total < 21:
        result = "below"
    else:
        result = "above"

    if isAce:
        result += " ace"
    elif isKing:
        result += " king"
    elif isQueen:
        result += " queen"
    elif isJack:
        result += " jack"
    else:

        # Getting max value in cards
        maxValue = max(cards)

        if maxValue == 10:
            result += " ten"
        elif maxValue == 9:
            result += " nine"
        elif maxValue == 8:
            result += " eight"
        elif maxValue == 7:
            result += " seven"
        elif maxValue == 6:
            result += " six"
        elif maxValue == 5:
            result += " five"
        elif maxValue == 4:
            result += " four"
        elif maxValue == 3:
            result += " three"
        elif maxValue == 2:
            result += " two"
        elif maxValue == 1:
            result += " ace"

    # Returning result
    return result


# keep this function call here
print(BlackjackHighest(input()))
