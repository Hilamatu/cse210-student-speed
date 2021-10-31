from time import sleep
from game import constants
from game.limit import Limit
from game.score import Score
from game.words import Words

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
       
    """

    def __init__(self, input_service, output_service):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self._limit = Limit()
        self._input_service = input_service
        self._keep_playing = True
        self._output_service = output_service
        self._score = Score()
        self._words = Words()
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            sleep(constants.FRAME_LENGTH)

    def _get_inputs(self):
        """Gets the inputs. In this case,
        that means getting the typed letter

        Args:
            self (Director): An instance of Director.
        """
        
        letter = self._input_service.get_letter()
        self._words.set_letter(letter)

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, check if there is a matched word and if the words reached the limit line.

        Args:
            self (Director): An instance of Director.
        """
        self._check_limit()
        self._check_matched_words()
        
    def _do_outputs(self):
        """Outputs the important game information. In 
        this case, printing the words, the limit line, the score, and the buffer

        Args:
            self (Director): An instance of Director.
        """
        buff = str(self._words.buffer)
        self._output_service.clear_screen(buff)
        self._output_service.draw_actor(self._limit)
        self._output_service.draw_actors(self._words.get_all())
        self._output_service.draw_actor(self._score)
        self._output_service.flush_buffer()

    def _check_limit(self):
        """Chechs if the words reached the limit line

        Args:
            self (Director): An instance of Director.
        """
        
        words_list = self._words.get_all()
        for word in words_list:
            if self._limit.get_position().equals(word.get_position()):
                self._words.reset_list(word)
                

    def _check_matched_words(self):
        """Checks if there are words that match with the inputed words.
        Args:
            self (Director): An instance of Director.
        """

        word = self._words.word
        words_list = self._words.get_all()
    
        for wd in words_list:
            if wd.get_text() == word:
                points = len(word)
                self._score.add_points(points)
                self._words.word = ''
                    
            