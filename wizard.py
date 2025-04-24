import character
#vcerrides character class to gain a unique description, mr, and str
class Wizard(character.Character):
  def description(self) -> str:
    return "Altar the Wizard"

  def magic_resistance(self) -> int:
    return 3

  def strength(self) -> int:
    return 1

  def __str__(self):
    return "Name: " +  self.description() + "\nMR: " + str(self.magic_resistance()) + "\nSTR: "  + str(self.strength())