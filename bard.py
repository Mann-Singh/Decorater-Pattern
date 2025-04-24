import character
#overrides character class to gain a unique description, mr, and str
class Bard(character.Character):
  def description(self) -> str:
    return "Barth the Bard"

  def magic_resistance(self) -> int:
    return 2
    
  def strength(self) -> int:
    return 2
  def __str__(self):
    return "Name: " +  self.description() + "\nMR: " + str(self.magic_resistance()) + "\nSTR: "  + str(self.strength())
    