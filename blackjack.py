import random

playerIn = True
dealerIn = True

# Deck of cards / Player Dealer Hand
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10] * 4 + ['J', 'Q', 'K', 'A'] * 4
# I exceeded the recommended 88 character so I multiplied it by 4, 
# Since there are 4 suits of each card
playerHand = []
dealerHand = []

# Deal the cards
# Here I am using the random.choice() function to randomly select a card from the deck and .append to add it to the hands of both player and dealer.

def dealCard(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)

# Calculate each hand total
# I used a for loop to iterate through the playerHand and dealerHand and add the values of each card to the total
def total(turn):
    total = 0
    face = ['J', 'K', 'Q']
    for card in turn:
        if isinstance(card, int):
            total += card
        elif card in face:
            total += 10
        else:  # card is 'A'
            if total + 11 > 21:
                total += 1
            else:
                total += 11
    return total

# Reveal part of the dealer's hand
# This function is necessary to determine the winner of the game.
def revealDealerHand():
    if len(dealerHand) == 2:
        return [dealerHand[0], 'X']
    elif len(dealerHand) > 2:
        return [dealerHand[0], dealerHand[1], '...']

# Gameplay loop
# Here I am using a while loop to keep the game going until one of the players busts or stands
for _ in range(2):
    dealCard(dealerHand)
    dealCard(playerHand)

while playerIn or dealerIn:
    print(f"Dealer has {revealDealerHand()} and X")
    print(f"You have {playerHand} for a total of {total(playerHand)}")

    if playerIn:
        stayOrHit = input("1: Stay\n2: Hit\n")
        if stayOrHit == '1':
            playerIn = False
            dealerIn = False
        else:
            dealCard(playerHand)
            if total(playerHand) >= 21:
                break

    if not playerIn:  # Dealer's turn after player stays
        while total(dealerHand) < 17:
            dealCard(dealerHand)
            if total(dealerHand) >= 21:
                break

    if total(dealerHand) >= 21 or total(playerHand) >= 21:
        break
# If the player or the dealer has 21 then the game ends and the winner is declared

# Determine the winner
# This is where I use the if/else statements to determine the winner
# In this case if the player has a 21, then they win with a Blackjack
if total(playerHand) == 21:
    print(f"You have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
    print("Blackjack! You win!")
# In this case if the dealer has a 21, then they win with a Blackjack
elif total(dealerHand) == 21:
    print(f"You have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
    print("Blackjack! The house always wins!")
# In this case if the player has a higher total of 21, then they bust and the dealer wins
elif total(playerHand) > 21:
    print(f"You have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
    print("You bust! Dealer wins!")
# In this case if the dealer has a higher total of 21, then they bust and the player wins
elif total(dealerHand) > 21:
    print(f"You have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
    print("Dealer busts! You win!")
# In this case it checks the dealer is closer to 21, if the dealer is closer and does not surpass 21 then the dealer wins
elif 21 - total(dealerHand) < 21 - total(playerHand):
    print(f"You have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
    print("Dealer wins!")
# In this case it checks the player closer to 21, if the player is closer and does not surpass 21 then the player wins
elif 21 - total(dealerHand) > 21 - total(playerHand):
    print(f"You have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
    print("You win!")
# In this case it checks if the player and dealer have a similar total, if they are then it's a tie
else:
    print(f"You have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
    print("It's a tie!")

# Add a line to exit the game after the result is shown
input("Press Enter to exit the game.")
