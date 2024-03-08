import random

flashcards = {}
hardest_cards = {}
log_list = []


def add_flashcard():
    msg = 'The card:'
    log_list.append(msg)
    print(msg)
    while True:
        term = input()
        log_list.append(term)
        if term in flashcards.keys():
            msg = f'The term "{term}" already exists. Try again:'
            log_list.append(msg)
            print(msg)
        else:
            flashcards[term] = None
            break
    msg = 'The definition of the card:'
    log_list.append(msg)
    print(msg)
    while True:
        definition = input()
        log_list.append(definition)
        if definition in flashcards.values():
            msg = f'The definition "{definition}" already exists. Try again:'
            log_list.append(msg)
            print(msg)
        else:
            flashcards[term] = definition
            break
    msg = f'The pair ("{term}":"{definition}") has been added.'
    log_list.append(msg)
    print(msg)


def remove_flashcard():
    msg = 'Which card?'
    log_list.append(msg)
    print(msg)
    card_to_remove = input()
    log_list.append(card_to_remove)
    if card_to_remove in flashcards.keys():
        del flashcards[card_to_remove]
        msg = 'The card has been removed.'
        log_list.append(msg)
        print(msg)
    else:
        msg = f'Can\'t remove "{card_to_remove}": there is no such card.'
        log_list.append(msg)
        print(msg)


def import_flashcards():
    counter = 0
    msg = 'File name:'
    log_list.append(msg)
    print(msg)
    file_name = input()
    log_list.append(file_name)
    try:
        counter = 0
        with open(file_name, "r") as file1:
            for line in file1:
                strip_line = line.strip()
                term, definition, errors = strip_line.split(':')
                flashcards[term] = definition
                hardest_cards[term] = int(errors)
                counter += 1
        msg = f'{counter} cards have been loaded.'
        log_list.append(msg)
        print(msg)
    except:
        msg = 'File not found.'
        log_list.append(msg)
        print(msg)
    msg = f'{counter} cards have been loaded.'
    log_list.append(msg)
    print(msg)


def export_flashcards():
    msg = 'File name:'
    log_list.append(msg)
    print(msg)
    file_name = input()
    log_list.append(file_name)
    with open(file_name, 'w') as file2:
        for (k, v) in flashcards.items():
            if k not in hardest_cards.keys():
                file2.write(f'{k}:{v}:0\n')
            else:
                file2.write(f'{k}:{v}:{hardest_cards[k]}\n')
    msg = f'{len(flashcards)} cards have been saved.'
    log_list.append(msg)
    print(msg)


def ask():
    msg = 'How many times to ask?:'
    log_list.append(msg)
    print(msg)
    number_of_ask = int(input())
    log_list.append(number_of_ask)
    for i in range(number_of_ask):
        key_index = random.randint(0, len(flashcards) - 1)
        key_list = list(flashcards.keys())
        key = key_list[key_index]
        value = flashcards[key]
        msg = f'Print the definition of  {key_list[key_index]}:'
        log_list.append(msg)
        print(msg)
        definition = input()
        log_list.append(definition)
        if definition == value:
            msg = 'Correct'
            log_list.append(msg)
            print(msg)
        elif definition != value and definition in flashcards.values():
            msg = f'Wrong. The right answer is "{value}", but your definition is correct for "{[key for key in key_list if flashcards[key] == definition]}".'
            log_list.append(msg)
            print(msg)
            if key not in hardest_cards.keys():
                hardest_cards[key] = 1
            else:
                hardest_cards[key] += 1
        else:
            msg = f'Wrong. The right answer is "{value}".'
            log_list.append(msg)
            print(msg)
            if key not in hardest_cards.keys():
                hardest_cards[key] = 1
            else:
                hardest_cards[key] += 1


def log():
    msg = 'File name:'
    log_list.append(msg)
    print(msg)
    file_name = input()
    log_list.append(file_name)
    with open(file_name, 'w') as file1:
        for i in log_list:
            print(i, file=file1)
    print('The log has been saved.')


def show_hardest_card():
    sorted_hardest_cards = sorted(hardest_cards.items(), key=lambda x: x[1], reverse=True)
    if len(sorted_hardest_cards) == 0:
        print('There are no cards with errors.')
    else:
        hardest_cards_terms = return_cards(sorted_hardest_cards)
        arr = hardest_cards_terms.split(',')
        if len(arr) == 1:
            msg = f'The hardest card is "{hardest_cards_terms}". You have {sorted_hardest_cards[0][1]} errors answering it.'
            log_list.append(msg)
            print(msg)
        else:
            msg = f'The hardest card are "{hardest_cards_terms}". You have {sorted_hardest_cards[0][1]} errors answering them.'
            log_list.append(msg)
            print(msg)


def return_cards(sorted_dict):
    highest_val = sorted_dict[0][1]
    returned_list = [sorted_dict[0][0]]
    for i in range(1, len(sorted_dict)):
        if sorted_dict[i][1] == highest_val:
            returned_list.append(sorted_dict[i][0])
    return '", "'.join(returned_list)


def reset_stats():
    hardest_cards.clear()
    msg = 'Card statistics have been reset.'
    log_list.append(msg)
    print(msg)


def control_flashcards():
    while True:
        print('Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):')
        action = input()
        log_list.append(action)
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
        elif action == 'log':
            log()
        elif action == 'hardest card':
            show_hardest_card()
        elif action == 'reset stats':
            reset_stats()


control_flashcards()
