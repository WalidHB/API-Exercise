import requests

def start_deck():
    """
    Start a new deck of cards and shuffle it.
    """

    req = requests.get('https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1')

    if req.status_code == 200:
        deck = req.json()
        deck_started = True
        deck_id = deck["deck_id"]
        print("Deck started and shuffled.")
        
        return deck_started, deck_id
    else:

        print("Connection error.")
        return False, None


def draw_card(deck_id, card_number):
    """
    Draw cards from the deck with the specified deck ID.
    """

    req = requests.get(f'https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count={card_number}')

    if req.status_code == 200:
        result = req.json()


        print('The cards are:')
        for card in result["cards"]:
            print(f'{card["value"]} OF {card["suit"]}\n')
        print(f'Remaining cards: {result["remaining"]}')

        user_input = input("Exit? [y]es / [n]o ").lower()
        if user_input in ['y', 'yes']:
            return True

        elif user_input in ['n', 'no']:
            return False
        else:
            print('Wrong input.')
    else:
        print("Connection error.")
        return False

def main():

    exit_flag = False
    deck_started = False

    while not exit_flag:

        if not deck_started:

            user_input = input("Start a new deck? [y]es / [n]o ").lower()

            if user_input in ['y', 'yes']:
                deck_started, deck_id = start_deck()

            elif user_input in ['n', 'no']:

                while True:
                    user_input = input("Exit? [y]es / [n]o ")
                    if user_input in ['y', 'yes']:
                        exit_flag = True
                        break

                    elif user_input in ['n', 'no']:
                        break
                    else:
                        print('Wrong input.')

                continue

            else:
                print('Wrong input.')

            
        card_number = input("Please enter the number of cards you want to draw: ")
        exit_flag = draw_card(deck_id, card_number)


if __name__ == "__main__":
    main()