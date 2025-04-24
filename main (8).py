# Authors: Prabhas Dama and Manjot Singh
# Date: April 21, 2025
# Description: A program uses the decorator design pattern to create a character with items of the users choice to boost character stats. The game then uses the decorated character to fight against 3 random monsters choosen out of a list of 7. If the user wins 2/3 of the fights, they win the game.

import bard
import warrior
import wizard

import shield
import cloak
import ring

import check_input
import random


def main():

  print("Character Maker!\nChoose a starting character: \n")

  char_choice = check_input.get_int_range("1) Bard\n2) Warrior\n3) Wizard\n", 1, 3)
  if char_choice == 1:
    char = bard.Bard()
    print(char)
  elif char_choice == 2:
    char = warrior.Warrior()
    print(char)
  else:
    char = wizard.Wizard()
    print(char)

  #While loop runs twice, letting the user choose two items, once an item is chosen, it is removed from the list of items.
  n = 2
  items = ["Sturdy Shield", "Protective Cloak", "Magic Ring"]
  while n > 0:
    print("\nChoose " + str(n) + " items:\n")
    item_choice = check_input.get_int_range(
        "1)" + items[0] + "\n2)" + items[1] + "\n3)" + items[2] + "\n", 1, 3)

    if items[item_choice - 1] == "Sturdy Shield":
      char = shield.Shield(char)
      print(char)
      items.remove("Sturdy Shield")
      n -= 1

    elif items[item_choice - 1] == "Protective Cloak":
      char = cloak.Cloak(char)
      print(char)
      items.remove("Protective Cloak")
      n -= 1

    elif items[item_choice - 1] == "Magic Ring":
      char = ring.Ring(char)
      print(char)
      items.remove("Magic Ring")
      n -= 1

    print("\nChoose " + str(n) + " items:\n")
    #At this point there are only two items left in the list, so the user is only given two choices.
    item_choice_2 = check_input.get_int_range(
        "1)" + items[0] + "\n2)" + items[1] + "\n", 1, 2)

    if items[item_choice_2 - 1] == "Sturdy Shield":
      char = shield.Shield(char)
      print(char)
      n -= 1

    elif items[item_choice_2 - 1] == "Protective Cloak":
      char = cloak.Cloak(char)
      print(char)
      n -= 1

    elif items[item_choice_2 - 1] == "Magic Ring":
      char = ring.Ring(char)
      print(char)
      n -= 1

  print("\nYou must pass two of the following three trials!\n")
  #List of monsters, out of the list, three are randomly chosen and added to a new list.
  monsters = [["Spiked Dragon", 0, 6], ["Orc Warlord", 1, 5],
              ["Shadow Knight", 2, 4], ["Lava Monster", 3, 3],
              ["Fiendish Ghoul", 4, 2,], ["Goblin Mage", 5, 1], 
              ["Dark Magician", 6, 0]]
  monster_list = []
  #The game runs for 3 battles regardless of the outcome of the battles.
  for i in range(3):
    monst_choice = random.randint(0, len(monsters) - 1)
    monster_list.append(monsters[monst_choice])
    monsters.remove(monsters[monst_choice])

  #Tracks win to check if user won at least 2 battles.
  num_wins = 0
  for i in range(3):
    print("Trial " + str(i + 1) + " of 3:")
    print("You encounter a " +
          str(monster_list[i][0] + "\nMR: " + str(monster_list[i][1]) +
              "\nSTR: " + str(monster_list[i][2])))
    print("\nFight:")
    #User is given a choice to either battle or dodge the monster.
    battle_choice = check_input.get_int_range("1) Battle\n2) Dodge\n", 1, 2)
    if battle_choice == 1:
      #user
      if char.strength() >= monster_list[i][1] and char.magic_resistance(
      ) >= monster_list[i][2]:
        print("You battle with the " + monster_list[i][0] +
              " and easily defeat it!\n")
        print("You have passed this trial.\n")
        num_wins += 1
      else:
        print("You battle with the " + monster_list[i][0] +
              " and are defeated!\n")
        print("You have failed this trial.\n")

    else:
      #25% chance to dodge the monster.
      if random.randint(0, 100) < 25:
        print("You dodge the " + monster_list[i][0] + " and escape!")
        print("You have passed this trial.\n")
        num_wins += 1
      else:
        print("You attemp to dodge the " + monster_list[i][0] +
              ", but it manages to hit you!\n")
        print("You have failed this trial.\n")
  #checking the win condition.
  if num_wins >= 2:
    print("You have passed the three trials... barely.")
  else:
    print("You have failed the trials.")


main()
