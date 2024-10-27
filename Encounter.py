# Encounter
import random
# encounter types
enemies = ["Evil Witch", "Ogre", "Terry the Terrible", "Slime"]
# dictionaries for values to be called upon in later functions
health = {"Magic User": 33,
          "Fighter": 99,
          "Archer": 66,
          "Evil Witch": 15,
          "Ogre": 110,
          "Terry the Terrible": 65,
          "Slime": 40}
max_attack = {"Magic": 11,
              "Sword": 6,
              "Bow and Arrow": 9,
              "Evil Witch": 15,
              "Ogre": 3,
              "Terry the Terrible": 8,
              "Slime": 5}
min_attack = {"Magic": 5,
              "Sword": 0,
              "Bow and Arrow": 0,
              "Evil Witch": 10,
              "Ogre": 0,
              "Terry the Terrible": 0,
              "Slime": 0}

# Function for user to select weapon


def weapon_choice():
    # Ask for input from user to select weapon
    weapon_input = input("""Please choose your weapon.
                       1. Magic
                       2. Sword
                       3. Bow and Arrow
                       Input the number of your chosen weapon: """)
    # If/Else clauses to set values
    if weapon_input == "1":
        weapon = "Magic"
        return weapon
    elif weapon_input == "2":
        weapon = "Sword"
        return weapon
    elif weapon_input == "3":
        weapon = "Bow and Arrow"
        return weapon
    else:
        print("Please input 1, 2 or 3 to select weapon.")
        weapon_choice()

# function for character classes


def class_select(weapon):
    if weapon == "Magic":
        character_class = "Magic User"
        return character_class
    elif weapon == "Sword":
        character_class = "Fighter"
        return character_class
    elif weapon == "Bow and Arrow":
        character_class = "Archer"
        return character_class
    else:
        print("An error has occurred, please restart.")


# function to randomly generate an enemy
def random_encounter():
    encounter_selector = random.choice(enemies)
    print(f"The {encounter_selector} has appeared")
    return encounter_selector

# function for player to select move


def fight_choice():
    fight_choice = input("""Please chose from:
                       1. Attack
                       2. Heal
                       3. Defend
                       """)
    if fight_choice.lower() == "attack" or fight_choice == "1":
        return 1
    elif fight_choice.lower() == "heal" or fight_choice == "2":
        return 2
    elif fight_choice.lower() == "defend" or fight_choice == "3":
        return 3
    else:
        print("Please give valid input.")
        return fight_choice()

# function where enemy fights player until one has no health


def fight(weapon, character, opponent):
    # set player health
    player_health = health[character]
    # set enemy health
    enemy_health = health[opponent]
    # while loop so combat ends if player or enemy die
    while player_health > 0 and enemy_health > 0:
        player_choice = fight_choice()
        if player_choice == 1:
            print("You have attacked.")
            # enemy loses health values set in previous dictionary for attack
            enemy_health -= random.randint(
                min_attack[weapon], max_attack[weapon])
            # player loses health from dictionary setting attack values for their opponent
            player_health -= random.randint(
                min_attack[opponent], max_attack[opponent])
        elif player_choice == 2:
            print("You have healed")
            # player heals some health
            player_health += random.randint(
                min_attack[weapon]+3, max_attack[weapon]+3)
            if player_health > health[character]:
                player_health = health[character]
            # the enemy will still attack if player heals
            player_health -= random.randint(
                min_attack[opponent], max_attack[opponent])
        elif player_choice == 3:
            # random value generated
            defend_chance = random.randint(1, 10)
            # scenario 1 where player fails to defend properly and takes half damage
            if defend_chance == 0:
                print("You did not defend properly")
                player_health -= int(random.randint(
                    min_attack[opponent], max_attack[opponent])/2)
            # scenario 2 where player successfully defends
            elif 0 < defend_chance < 8:
                print("You have blocked the attack successfully.")
            # scenario 3 where player successfully deflects the attack
            elif defend_chance >= 8:
                print("You have defended yourself successfully, the attack deflects.")
                enemy_health -= random.randint(
                    min_attack[opponent], max_attack[opponent])

        # display player and enemy health at end of round
        print(f"Your health: {player_health}")
        print(f"Enemy health: {enemy_health}")

    # give identity of victor dependent on who loses health
    if enemy_health <= 0:
        print("You have defeated your opponent")
    elif player_health <= 0:
        print("You have been defeated!")


# the game, combining all functions
def game():
    weapon = weapon_choice()
    print(f"You have selected {weapon}.")
    character = class_select(weapon)
    print(f"Your character class is {character}.")
    encounter_type = random_encounter()
    fight(weapon, character, encounter_type)


# running the game
if __name__ == "__main__":
    game()
