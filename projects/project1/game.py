from secrets import choice
from projects.project1.multideck import MultiDeck



def game() -> None:
    """
    Main function for the game of BlackJack
    """
    face_cards = ["J", "Q", "K", "A"]
    yes = ["y", "Y", "Yes", "yes"]
    valid_hits = ["H", "h", "hit", "Hit"]
    valid_stays = ["S", "s", "stay", "Stay"]

    player_hand = []
    dealer_hand = []
    player_score = 0
    dealer_score = 0
    deck_count = choice([2,4,6,8])
    deck = MultiDeck(deck_count)


    def check() -> None:
        """
        checks if player has 21 or has busted, if not, allows hit or stay
        """
        player_score = value(player_hand)
        print("\n")
        print_hand(player_hand, player_score)
        if player_score == 21: # forces stay when player reaches 21 and calculates dealer score
            dealer_hand[1] = hidden_card
            dealer_score = value(dealer_hand)
            stay()
        if player_score > 21:
            print("\n")
            print("Player Busted! You went over 21!")
            game_over()
        else:
            choice = ""
            while choice not in valid_hits + valid_stays:
                choice = input("Do you want to (H)it or (S)tay? ")
                if choice in valid_hits:
                    hit(player_hand)
                    check()
                elif choice in valid_stays:
                    stay()
                else:
                    choice = print("Invalid input. ", end="")
    
    def print_hand(hand, score):
        if hand == player_hand:
            print(f"Player's Hand: ", end="")
        else:
            print(f"Dealer's Hand: ", end="")
        for card in hand:
            print(card, end=" ")
        print(f"| Score = {score}")

    def value(hand) -> int:
        """
        Calculates value of inputted hand and returns the score
        """
        value = 0
        def score(one, value):
            for card in hand:
                if card != "[Hidden]":
                    card = card[1]
                    if card == "1":
                        card = "10"
                    if card not in face_cards:
                        value += int(card)
                    else:
                        if card != "A":
                            value += 10
                        elif one:
                            value +=1
                        elif value < 11:
                            value += 11
                        else:
                            value += 1
            return value
        value = score(False, value)

        if value > 21: # reevaluates Aces that could've wrongly been scored 11 instead of 1
            value = 0
            value = score(True, value)
        return value


    def hit(hand) -> None:
        """
        Adds a card to the inputted hand
        """
        card = deck.rand_card()
        hand.append(f"[{card.card_rank}{card.card_suit}]")


    def stay() -> None:
        """
        Reveals dealer hand calculates dealer score and prints the winner
        """
        player_score = value(player_hand)
        dealer_hand[1] = hidden_card
        dealer_score = value(dealer_hand)
        if dealer_score == 21:
            print_hand(dealer_hand, dealer_score)
            if dealer_score == player_score:
                print("Both Blackjacks! It's a Tie!")
            else:
                print("Dealer has a Blackjack! Dealer wins!")
            game_over()
        else:
            while dealer_score < 17:
                hit(dealer_hand)
                dealer_score = value(dealer_hand)
            else:
                print_hand(dealer_hand, dealer_score)
                if dealer_score == player_score:
                    print("It's a Tie!")
                elif dealer_score > 21:
                    print("\n")
                    print("Dealer Busted! Player wins!")
                elif dealer_score > player_score:
                    print("\n")
                    print("Dealer wins!")
                else:
                    print("\n")
                    print("Player wins!")
                game_over()
            

    def game_over() -> None:
        """
        Let's player decide to play the game again
        """
        redo = input("Would you like to play again? ")
        if redo in yes:
            game()
        else:
            exit()
        

    print("Welcome to Blackjack!")
    print("\n")

    hit(player_hand) # adds initial cards by hitting twice for each hand
    hit(player_hand)
    
    hit(dealer_hand)
    hidden_card = deck.rand_card()
    hidden_card = f"[{hidden_card.card_rank}{hidden_card.card_suit}]"
    dealer_hand.append("[Hidden]")

    player_score = value(player_hand)
    dealer_score = value(dealer_hand)

    print("Inital Deal:")
    print_hand(player_hand, player_score)
    print_hand(dealer_hand, dealer_score)


    if player_score == 21: # checks for Blackjack on iniitial deal, if Player has Blackjack checks if dealer also has Blackjack
        dealer_hand[1] = hidden_card
        dealer_score = value(dealer_hand)
        if player_score > dealer_score:
            print_hand(dealer_hand, dealer_score)
            print("\n")
            print("Player has Blackjack! Player wins!")
            game_over()
        else:
            stay() # if player has a Blackjack and Dealer also has a Blackjack, will force a tie
    check()
