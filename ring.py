import decorater
#overrides Decorater class to give the character a new description, mr, and str
class Ring(decorater.Decorater):
  def description(self) -> str:
    return self._character.description() + " with a Ring"

  def magic_resistance(self) -> int:
    return self._character.magic_resistance() + 2

  def strength(self) -> int:
    return self._character.strength() 

  def __str__(self):
    return "Name: " +  self.description() + "\nMR: " + str(self.magic_resistance()) + "\nSTR: "  + str(self.strength())
