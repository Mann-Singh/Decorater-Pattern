import abc
#Abstract class for character object
class Character(abc.ABC):
  @abc.abstractmethod
  def description(self) -> str:
    pass

  @abc.abstractmethod
  def magic_resistance(self) -> int:
    pass

  @abc.abstractmethod
  def strength(self) -> int:
    pass

  def __str__(self):
    return "Name: " +  self.description() + "\nMR: " + str(self.magic_resistance()) + "\nSTR: "  + str(self.strength())