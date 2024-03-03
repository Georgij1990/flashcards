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
    while True:
        definition = input()
        if definition in flashcards.values():
            print(f'The definition "{definition}" already exists. Try again:')
        else:
            flashcards[term] = definition
            break


def remove_flashcard():
    print('Which card?')
    card_to_remove = input()
    if card_to_remove in flashcards.keys():
        del flashcards[card_to_remove]
        print('The card has been removed.')
    else:
        print(f'Can\'t remove "{card_to_remove}": there is no such card.')


def import_flashcards():
    print('File name:')
    file_name = input()
    try:
        counter = 0
        with open(file_name, "r") as file1:
            for line in file1:
                strip_line = line.strip()
                term, definition = strip_line.split(':')
                flashcards[term] = definition
        print(f'{counter} cards have been loaded.')
    except:
        print('File not found.')


def export_flashcards():
    print('File name:')
    file_name = input()
    with open(file_name, 'w') as file2:
        for (k, v) in flashcards.items():
            file2.write(f'{k}:{v}\n')
    print(f'{len(flashcards)} cards have been saved.')


def ask():
    print('Input the number of cards:')
    num_of_flashcards = int(input())
    for i in range(num_of_flashcards):
        add_flashcard()


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


if __name__ == '__main__':
    control_flashcards()

# print('Input the number of cards:')
# num_of_flashcards = int(input())

# for i in range(num_of_flashcards):
#     print(f'The term for card {i + 1}')
#     term = None
#     while True:
#         term = input()
#         if term in flashcards.keys():
#             print(f'The term "{term}" already exists. Try again:')
#         else:
#             flashcards[term] = None
#             break
#     print(f'The definition for card {i + 1}:')
#     while True:
#         definition = input()
#         if definition in flashcards.values():
#             print(f'The definition "{definition}" already exists. Try again:')
#         else:
#             flashcards[term] = definition
#             break
# for k, v in flashcards.items():
#     print(f'Print the definition of "{k}":')
#     guess_definition = input()
#     if flashcards[k] == guess_definition:
#         print('Correct!')
#     elif flashcards[k] != guess_definition and guess_definition in flashcards.values():
#         print(f'Wrong. The right answer is "{v}", but your definition is correct for "{[key for key in flashcards.keys() if flashcards[k] == guess_definition]}".')
#     else:
#         print(f'Wrong. The right answer is "{v}".')
