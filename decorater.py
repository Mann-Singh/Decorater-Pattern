import abc
import character
#Abstract class for decorater objects
class Decorater(character.Character, abc.ABC):
    def __init__(self, c):
        self._character = c 
        
    def description(self) -> str:
        return self._character.description()
        
    def magic_resistance(self) -> int:
        return self._character.magic_resistance()

    def strength(self) -> int:
        return self._character.strength()

    def __str__(self):
        return self._character.__str__()
