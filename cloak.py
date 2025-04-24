import decorater
#overrides Decorater class to give the character a new description, mr, and str
class Cloak(decorater.Decorater):
  def description(self) -> str:
    return "Cloaked " + self._character.description()
    
  def magic_resistance(self) -> int:
    return self._character.magic_resistance() + 1

  def strength(self) -> int:
    return self._character.strength() + 1

  def __str__(self):
    return "Name: " +  self.description() + "\nMR: " + str(self.magic_resistance()) + "\nSTR: "  + str(self.strength())
    