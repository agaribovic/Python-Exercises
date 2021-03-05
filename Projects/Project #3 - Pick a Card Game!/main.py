import time, random

ranks = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
suits = ["Clubs","Hearts","Diamonds","Spades"]
deck = []

value = 1
for rank in ranks:
    for suit in suits:
        deck.append([rank + " of " + suit, value])
    value = value + 1

random.shuffle(deck)
score = 0
card1 = deck.pop(0)

player = input("Please enter your name to get started: ")
rules = "You simply have to decide whether the second card is searched for higher or lower than the first card. As you progress, you will be shown a new card. Choose higher or lower to decide whether it is searched for more or less than the previous card. The objective is to get the most right in a row."

while True:
    print(player, "'s score so far is ", score,sep='')
    print("\n\nThe current card is", card1[0])
    while True:
        choice = input("higher or lower?")
        if len(choice) > 0:
            if choice[0].lower() in ["h","l"]:
                break
            elif choice.lower() == "--help":
                print(rules, end="")
                break
 
 
    card2 = deck.pop(0)
    print("The next card picked is", card2[0])
    time.sleep(1)

    if choice[0].lower() == "h" and card2[1] > card1[1]:
        print("Correct!")
        score +=1
        time.sleep(1)
    if choice[0].lower() == "h" and card2[1] < card1[1]:
        print("Wrong!")
        time.sleep(1)
        break
    if choice[0].lower() == "l" and card2[1] < card1[1]:
        print("Correct!")
        score +=1
        time.sleep(1)
    if choice[0].lower() == "l" and card2[1] > card1[1]:
        print("Wrong!")
        time.sleep(1)
        break
    else:
        print("draw!")

    card1 = card2


print("Game over!")
print(player, "'s final score is ", score,sep='')
time.sleep(4)
