import character
#overrides character class to gain a unique description, mr, and str
class Warrior(character.Character):
  def description(self) -> str:
    return "Harcor the Warrior"

  def magic_resistance(self) -> int:
    return 0

  def strength(self) -> int:
    return 4

  def __str__(self):
    return "Name: " +  self.description() + "\nMR: " + str(self.magic_resistance()) + "\nSTR: "  + str(self.strength())