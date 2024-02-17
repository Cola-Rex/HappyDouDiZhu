import random

# 定义扑克牌，其中 R 和 B 代表红、黑鬼
DECK = ['3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2'] * 4 + ['R', 'B']

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def receive_cards(self, cards):
        self.hand.extend(cards)
        self.hand.sort(key=lambda x: (DECK.index(x), x))

    def play_card(self):
        # 这里使用一个简单的策略：随机出牌
        card = random.choice(self.hand)
        self.hand.remove(card)
        print(f"{self.name} plays: {card}")
        return card

def game():
    # 洗牌
    random.shuffle(DECK)

    # 分发初始牌
    player1 = Player("Player 1")
    player2 = Player("Player 2")
    player3 = Player("Player 3")
    player1.receive_cards(DECK[:17])
    player2.receive_cards(DECK[17:34])
    player3.receive_cards(DECK[34:51])

    # 随机选择地主，并给地主最后三张牌
    landlord = random.choice([player1, player2, player3])
    landlord.receive_cards(DECK[51:])
    print(f"{landlord.name} is the landlord!\n")

    # 地主先出牌
    turn_order = [landlord, player1, player2, player3]
    turn_order = [player for player in turn_order if player != landlord] + [landlord]

    # 游戏主循环
    while all([len(player.hand) > 0 for player in turn_order]):
        for player in turn_order:
            player.play_card()
            if len(player.hand) == 0:
                print(f"\n{player.name} wins!")
                return

if __name__ == "__main__":
    game()
