import random
import string
import nltk
from nltk.corpus import words

class RandomPasswordGenerator:
    def __init__(self, length=12, include_numbers=True, include_symbols=True):
        self.length = length
        self.include_numbers = include_numbers
        self.include_symbols = include_symbols

    def generate(self):
        chars = string.ascii_letters
        if self.include_numbers:
            chars += string.digits
        if self.include_symbols:
            chars += string.punctuation

        return ''.join(random.choice(chars) for _ in range(self.length))


class PinCodeGenerator:
    def __init__(self, length=4):
        self.length = length

    def generate(self):
        return ''.join(random.choice(string.digits) for _ in range(self.length))


class MemorablePasswordGenerator:
    def __init__(self, num_words=4, separator='-', capitalize=True):
        self.num_words = num_words
        self.separator = separator
        self.capitalize = capitalize

        # Zajistí, že corpus je stažený
        nltk.download('words', quiet=True)

    def generate(self):
        word_list = words.words()
        selected_words = random.sample(word_list, self.num_words)
        if self.capitalize:
            selected_words = [word.capitalize() for word in selected_words]
        return self.separator.join(selected_words)
