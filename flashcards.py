import random

flashcards = {}


def add_flashcard():
    print('The card:')
    while True:
        term = input()
        if term in flashcards.keys():
            print(f'The term "{term}" already exists. Try again:')
        else:
            flashcards[term] = None
            break
    print('The definition of the card:')
    while True:
        definition = input()
        if definition in flashcards.values():
            print(f'The definition "{definition}" already exists. Try again:')
        else:
            flashcards[term] = definition
            break
    print(f'The pair ("{term}":"{definition}") has been added.')


def remove_flashcard():
    print('Which card?')
    card_to_remove = input()
    if card_to_remove in flashcards.keys():
        del flashcards[card_to_remove]
        print('The card has been removed.')
    else:
        print(f'Can\'t remove "{card_to_remove}": there is no such card.')


def import_flashcards():
    counter = 0
    print('File name:')
    file_name = input()
    try:
        counter = 0
        with open(file_name, "r") as file1:
            for line in file1:
                strip_line = line.strip()
                term, definition = strip_line.split(':')
                flashcards[term] = definition
                counter += 1
        print(f'{counter} cards have been loaded.')
    except:
        print('File not found.')
    print(f'{counter} cards have been loaded.')


def export_flashcards():
    print('File name:')
    file_name = input()
    with open(file_name, 'w') as file2:
        for (k, v) in flashcards.items():
            file2.write(f'{k}:{v}\n')
    print(f'{len(flashcards)} cards have been saved.')


def ask():
    print('How many times to ask?:')
    number_of_ask = int(input())
    for i in range(number_of_ask):
        key_index = random.randint(0, len(flashcards) - 1)
        key_list = list(flashcards.keys())
        key = key_list[key_index]
        value = flashcards[key]
        print(f'Print the definition of  {key_list[key_index]}:')
        definition = input()
        if definition == value:
            print('Correct')
        elif definition != value and definition in flashcards.values():
            print(
                f'Wrong. The right answer is "{value}", but your definition is correct for "{[key for key in key_list if flashcards[key] == definition]}".')
        else:
            print(f'Wrong. The right answer is "{value}".')


def control_flashcards():
    while True:
        print('Input the action (add, remove, import, export, ask, exit):')
        action = input()
        if action == 'add':
            add_flashcard()
        elif action == 'remove':
            remove_flashcard()
        elif action == 'import':
            import_flashcards()
        elif action == 'export':
            export_flashcards()
        elif action == 'ask':
            ask()
        elif action == 'exit':
            print('Bye bye!')
            break



control_flashcards()
