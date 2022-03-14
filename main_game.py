from letter_state import LetterState
from logic import Wordle
from colorama import Fore
from typing import List
import random

def main():
    print('Welcome to my wordle game!')
    word_set = load_word_set('words.txt')
    secret_word = random.choice(list(word_set))
    wordle = Wordle(secret_word)

    while wordle.attempts_available:
        word = input('\nEnter your guess: ').upper()
        if len(word) != wordle.WORD_LENGTH:
            print(Fore.RED + f'Word length must be of {wordle.WORD_LENGTH} characters.' + Fore.RESET)
            continue

        if not word in word_set:
            print(Fore.RED + f'{word} is not a valid word...' + Fore.RESET)
            continue

        wordle.add_guess(word)
        display_results(wordle)
    
    if wordle.is_solved:
        print('Congo! You have solved the puzzle.')
    else:
        print('Oops! Better luck next time.')
        print(f'The secret word was {wordle.secret_word}.')
        
def display_results(wordle: Wordle):
    print('\nResults so far...')
    print(f'{wordle.remaining_attempts} attempts remaining!\n')

    lines = []
    for word in wordle.attempts:
        result = wordle.check_guess(word)
        colored_result = convert_result_to_color(result)
        print(colored_result)
    
    for _ in range(wordle.remaining_attempts):
        print(" ".join(["_"] * wordle.WORD_LENGTH))

def load_word_set(path: str):
    word_set = set()
    with open(path, 'r') as f:
        for line in f.readlines():
            word = line.strip().upper()
            word_set.add(word)
    return word_set 

def convert_result_to_color(result: List[LetterState]):
    result_with_color = []
    for letter in result:
        if letter.is_in_position:
            color = Fore.GREEN
        elif letter.is_in_word:
            color = Fore.YELLOW
        else:
            color = Fore.RED
        colored_letter = color + letter.character + Fore.RESET
        result_with_color.append(colored_letter)
    return ' '.join(result_with_color)

if __name__ == '__main__':
    main()