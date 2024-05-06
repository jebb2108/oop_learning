import random

# Константы карт

suit_tuple = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
rank_tuple = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10',
              'Jack', 'Queen', 'King')

n_cards = 8


# Проходит по колоде и возвращает случайную карту из колоды
def get_card(deck_list_in):
    this_card = deck_list_in.pop()  # Снимает одну карту с верхней части
    # колоды и возвращает ее.
    return this_card


# Проходит по колоде и возвращает перемешанную копию колоды
def shuffle(deck_list_in):
    deck_list_out = deck_list_in.copy()
    random.shuffle(deck_list_out)
    return deck_list_out


# Основной код
print('Welcome to Higher or Lower.')
print('You have to choose whether the next card to be shown will be'
      'higher or lower than the current one.')
print('Getting it right adds 20 points; get it wrong and you 15 points')
print('You have 50 points to starts.')
print()


starting_deck_list = []

for suit in suit_tuple:
    for this_value, rank in enumerate(rank_tuple):
        card_dict = {'rank': rank, 'suit': suit, 'value': this_value + 1}
        starting_deck_list.append(card_dict)

score = 50

while True:
    print()
    game_deck_list = shuffle(starting_deck_list)
    current_card_dict = get_card(game_deck_list)
    current_card_rank = current_card_dict['rank']
    current_card_value = current_card_dict['value']
    current_card_suit = current_card_dict['suit']
    print('Starting card is:', current_card_rank + ' of'
          + current_card_suit)
    print()

    for card_number in range(0, n_cards): # Игрок играет в одну игру
                                          # из этого количества карт
        answer = input('Will the next card be higher or lower than '
                       + current_card_rank + ' of ' +
                       current_card_suit + '? (enter h or l): ')
        answer = answer.casefold() # Переводит в нижний регистр
        next_card_dict = get_card(game_deck_list)
        next_card_rank = next_card_dict['rank']
        next_card_value = next_card_dict['value']
        next_card_suit = next_card_dict['suit']
        print('Next card is:', next_card_rank + ' of ' +next_card_suit)

        if answer == 'h':
            if next_card_value > current_card_value:
                print('You got it right, it was higher')
                score += 20
            else:
                print('Sorry, it was not higher')
                score -= 15
        elif answer == 'l':
            if next_card_value < current_card_value:
                print('You got it right, it was lower')
                score += 20
            else:
                print('Sorry, it was not lower')
                score -= 15
        print('Your score is:', score)
        print()
        current_card_rank = next_card_rank
        current_card_value = next_card_value # не нужна текущая масть.

    go_again = input('To play again, press ENTER, or "q" to quit: ')
    if go_again == 'q':
        break

print('OK bye')