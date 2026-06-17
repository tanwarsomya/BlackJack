from game import Game

def show_hand(hand, label):
    print(f"{label}: {', '.join([str(card) for card in hand])}")

def play_game():
    print("Welcome to Blackjack!")
    game_state = True
    while game_state:
        game = Game()
        game.deal_initial_cards()
        show_hand(game.player_hand, "Your hand")       
        show_hand([game.dealer_hand[0]], "Dealer shows")
        while True:
            choice = input("Hit or Stand? (h/s): ")
            if choice == "h":
                game.player_hit()
                show_hand(game.player_hand, "Your hand")
                if game.calculate_hand(game.player_hand) > 21:
                    print("You busted!")
                    break
            elif choice == "s":
                break
        game.dealer_turn()
        show_hand(game.dealer_hand, "Dealer's hand")
        print(game.check_winner())
        choice = input("Play again? (y/n): ")
        if choice == "n":
            print("Great fun playing with you, hope to see you soon!")
            game_state = False

if __name__ == "__main__":
    play_game()