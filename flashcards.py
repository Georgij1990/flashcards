print('Input the number of cards:')
num_of_flashcards = int(input())
flashcards = {}
for i in range(num_of_flashcards):
    print(f'The term for card {i + 1}')
    term = input()
    print(f'The definition for card {i + 1}:')
    definition = input()
    flashcards[term] = definition
for k, v in flashcards.items():
    print(f'Print the definition of "{k}":')
    guess_definition = input()
    if flashcards[k] == guess_definition:
        print('Correct!')
    else:
        print(f'Wrong. The right answer is "{flashcards[k]}".')
