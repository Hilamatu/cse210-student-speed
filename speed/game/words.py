from game import constants
from game.actor import Actor
from game.point import Point

import random

class Words:
    
    def __init__(self):
        
        super().__init__()
        self._words = []
        self.prepare_5_words()
        self.word = ''
        self.buffer = ''
              
    
    def get_all(self):
        """Gets all the words.
        
        Args:
            self (Words): An instance of words.

        Returns:
            list: The ramdom words
        """
        return self._words

  

    
    def set_letter(self, letter):
        """appends this letter to words and buffer

        Args:
            letter (string): inputed letter
            self (Words): An instance of words.
            direction (Point): The direction to move.
        """
        if letter == "*":
            self.word = ""
            self.buffer = ""
        else:    
            self.word += letter
            self.buffer += letter
            count = len(self._words) - 1
            for n in range(count, -1, -1):
                word = self._words[n]           
                word.move_next()




    def reset_list(self, word):
        """removes the past words and append other random word

        Args:
            letter (string): inputed letter
            self (Words): An instance of words.
            
        """
        self._words.remove(word)
        
        words_list = constants.LIBRARY
        text = random.choice(words_list)
        y = 1
        x = 0
        
        x = random.randint(0, constants.MAX_X - len(text))
        position = Point(x , y)
        velocity = Point(0, 1)
        self._add_word(text, position, velocity)
        

    def _add_word(self, text, position, velocity):
        """add the word object with the text, position and velocity

        Args:
            text (string): a random word
            self (Words): An instance of words.
            
        """
        word = Actor()
        word.set_text(text)
        word.set_position(position)
        word.set_velocity(velocity)
        self._words.append(word)

    def prepare_5_words(self):
        """ Selects 5 random words from the words.txt

        Args:
            text (string): a random word
            self (Words): An instance of words.
            
        """
        words_list = constants.LIBRARY
        x = 0
        y = 20
        for n in range(constants.STARTING_WORDS):
            text = random.choice(words_list)
            x = random.randint(0, constants.MAX_X - len(text))
            position = Point(x, y + n)
            velocity = Point(0, 1)
            self._add_word(text, position, velocity)

  