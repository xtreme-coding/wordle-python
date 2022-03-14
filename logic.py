from letter_state import LetterState

class Wordle():

    MAX_ATTEMPTS = 6
    WORD_LENGTH = 5

    def __init__(self, secret_word:str):
        self.secret_word:str = secret_word.upper()
        self.attempts = []
        pass

    @property
    def is_solved(self):
        return len(self.attempts) > 0 and self.attempts[-1] == self.secret_word

    def add_guess(self, word:str):
        word = word.upper()
        self.attempts.append(word)

    def check_guess(self, word:str):
        word = word.upper()
        result = []
        for i in range(self.WORD_LENGTH):
            char = word[i]
            letter = LetterState(char)
            letter.is_in_word = char in self.secret_word
            letter.is_in_position = char == self.secret_word[i]
            result.append(letter)
        return result

    @property
    def remaining_attempts(self) -> int:
        return self.MAX_ATTEMPTS - len(self.attempts)

    @property
    def attempts_available(self):
        return self.remaining_attempts > 0 and not self.is_solved