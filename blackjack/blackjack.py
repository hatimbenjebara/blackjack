import random

# Define the card deck values
card_values = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': [1, 11]  # Ace can be 1 or 11
}

# Function to deal a card
def deal_card():
    return random.choice(list(card_values.keys()))

# Function to calculate the best sum considering Ace as 1 or 11
def calculate_best_sum(hand):
    total = 0
    aces = 0
    for card in hand:
        if card == 'A':
            aces += 1
        else:
            total += card_values[card]
    
    # Handle Ace values, trying to maximize without going over 21
    for _ in range(aces):
        if total + 11 <= 21:
            total += 11
        else:
            total += 1
    return total

# Player's strategy function (modify this for smarter strategies)
def player_decision(player_hand, dealer_card):
    # Dumb strategy: hit if total < 17
    return calculate_best_sum(player_hand) < 17

# Game simulation function
def play_blackjack():
    # Initialize hands
    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card()]

    print(f"Player's hand: {player_hand}, Dealer's face-up card: {dealer_hand[0]}")

    # Player's turn
    while player_decision(player_hand, dealer_hand[0]):
        player_hand.append(deal_card())
        print(f"Player hits: {player_hand}")
        if calculate_best_sum(player_hand) > 21:
            print(f"Player busts with {player_hand}. Dealer wins!")
            return

    player_total = calculate_best_sum(player_hand)
    print(f"Player stands with {player_hand} (total = {player_total})")

    # Dealer's turn
    dealer_hand.append(deal_card())
    while calculate_best_sum(dealer_hand) < 17:
        dealer_hand.append(deal_card())
        print(f"Dealer hits: {dealer_hand}")
    
    dealer_total = calculate_best_sum(dealer_hand)
    print(f"Dealer stands with {dealer_hand} (total = {dealer_total})")

    # Determine winner
    if dealer_total > 21:
        print("Dealer busts! Player wins!")
    elif player_total > dealer_total:
        print("Player wins!")
    elif player_total == dealer_total:
        print("It's a tie! Dealer wins!")
    else:
        print("Dealer wins!")

# Play a game
play_blackjack()
