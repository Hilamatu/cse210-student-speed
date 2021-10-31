import random
from game import constants
from game.actor import Actor
from game.point import Point

class Limit(Actor):
    """set the limit where words will disappear 
    
    Stereotype:
        Information Holder

   
    """
    def __init__(self):
        """The class constructor. Invokes the superclass constructor
        
        Args:
            self (Actor): an instance of Actor.
        """
        super().__init__()
        self.set_limit_line()
    
  

    def set_limit_line(self):
        """sets the limit of the screen
        
        Args:
            self (Limit): an instance of Limit.
        """
        x = 1
        y = 19
        position = Point(x, y)
        self.set_position(position)
        