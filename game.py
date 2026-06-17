from deck import Deck

class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player_hand = []
        self.dealer_hand = []
        
    def deal_initial_cards(self):
        for i in range(2):
            self.player_hand.append(self.deck.deal())
            self.dealer_hand.append(self.deck.deal())
            
    def calculate_hand(self, hand):
        aces = 0
        total = 0
        for card in hand:
            total += card.get_value()
            if card.rank == "Ace":
                aces += 1
        while total > 21 and aces > 0:
            total -= 10
            aces -= 1
        return total
    
    def player_hit(self):
        self.player_hand.append(self.deck.deal())
        
    def dealer_turn(self):
        while self.calculate_hand(self.dealer_hand) < 17:
            self.dealer_hand.append(self.deck.deal())
        
    def check_winner(self):
        player_total = self.calculate_hand(self.player_hand)
        dealer_total = self.calculate_hand(self.dealer_hand)
        
        if player_total > 21:
            return "Player busts! Dealer wins :("
        elif dealer_total > 21:
            return "Dealer busts!!! Player wins :)"
        elif player_total > dealer_total:
            return "Player wins!!!"
        elif player_total < dealer_total:
            return "Dealer wins :("
        else:
            return "Push! It's a tie!"
        