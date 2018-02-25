import random, collections


def make_new_deck():
    # spade club heart diamond
    deck = []
    for i in range(0, 52):
        deck.append(i)
        i += 1
    return deck


def shuffle_deck(deck):
    random.shuffle(deck)
    return deck


def card_suit(card_number):
    suit_code_options = 'Spades Hearts Diamonds Clubs'.split(' ')
    suit_code = card_number % 4
    return suit_code_options[suit_code]


def card_value(card_number):
    card_value_options = '1 2 3 4 5 6 7 8 9 10 J Q K'.split(' ')
    card_value = card_number % 13
    return card_value_options[card_value]


def card_ID(card_number):
    return card_value(card_number) + " of " + card_suit(card_number)


def hand_ID(cardlist):
    """return card IDs of a list of cards"""
    hand_ID_list = []
    for card in cardlist:
        hand_ID_list.append(card_ID(card))
    return hand_ID_list


def four_of_a_kind_check(cardlist):
    """check if a cardlist has four of a kind"""
    card_value_list = []
    for item in cardlist:   # determine card values for cards in cardlist and put into card_value_list
        card_value_list.append(card_value(item))
    # print(card_value_list)
    counter = collections.Counter(card_value_list)
    print(counter)
    for key in counter.keys():
        if counter[key] == 4:
            print("Holy shit four of a kind")
            return key
        else:
            pass
    return False


def deal(deck, hand_list, player, cards_dealt):
    """assigns cards_dealt to hand_list[player] and removes them from deck"""
    new_cards = random.sample(deck, cards_dealt)
    # print(new_cards)
    hand_list[player] = new_cards
    for cards in new_cards:
        deck.remove(cards)
    return deck, hand_list


def start_game(num_players):
    """input number of players, outputs player_list, hand_list, and game_deck"""
    game_deck = make_new_deck()
    player_list = []
    hand_list = [None]*num_players
    print(hand_list)
    for player in range(0, num_players):
        hand_list[player] = [None]
    print("\nHand list before any assignment is:", end=" ")
    print(hand_list)
    for player in range(0, num_players):  # assign player_list
        player_list.append("Player " + player.__str__())
    # print("Player list is: ", player_list)
    for player in range(0, num_players):  # assign hands
        print("\nAssigning values for player {}".format(player))
        game_deck, hand_list = deal(game_deck, hand_list, player, 5)
        print(f"Hand list is {hand_list}")
        # print(hand_list[player])
        # print(hand_list)
    print(player_list)
    print(hand_list)

#
# deck1 = make_new_deck()
# print(card_ID(5))
# #
# print(deck1)
# #
# for card in deck1:
#     print("Your card is", card_ID(deck1[card]))

# hand_list1 = [[None]]
# deal(deck1, hand_list1, 0, 5)
# print(hand_list1)
# hand1 = [1, 14, 27, 40]
#
# print(hand_ID(hand1))
# print(four_of_a_kind_check(hand1))


start_game(1)
print("Done")

