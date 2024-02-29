print('Input the number of cards:')
num_of_flashcards = int(input())
flashcards = {}
for i in range(num_of_flashcards):
    print(f'The term for card {i + 1}')
    term = None
    while True:
        term = input()
        if term in flashcards.keys():
            print(f'The term "{term}" already exists. Try again:')
        else:
            flashcards[term] = None
            break
    print(f'The definition for card {i + 1}:')
    while True:
        definition = input()
        if definition in flashcards.values():
            print(f'The definition "{definition}" already exists. Try again:')
        else:
            flashcards[term] = definition
            break
for k, v in flashcards.items():
    print(f'Print the definition of "{k}":')
    guess_definition = input()
    if flashcards[k] == guess_definition:
        print('Correct!')
    elif flashcards[k] != guess_definition and guess_definition in flashcards.values():
        print(f'Wrong. The right answer is "{v}", but your definition is correct for "{[key for key in flashcards.keys() if flashcards[k] == guess_definition]}".')
    else:
        print(f'Wrong. The right answer is "{v}".')
