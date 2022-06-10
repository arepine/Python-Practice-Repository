import random

class Character:
    def __init__(self) -> None:
        pass

    def character_role(self, role=''):
        self.role = role
        role_dict = {'Fighter':1, 'Archer':2, 'Wizard':3, 'Jokester':4, 'Valkyrie':5}
        role = random.choice(list(role_dict))
        return role
    
    def character_race(self, race=''):
        self.race = race
        race_dict = {'Human':1, 'Caporian':2, 'Tecalan':3, 'Falixi':4, 'Karnian':5}
        race = random.choice(list(race_dict))
        return race

    def __str__(self) -> str:
        return f"Your character is a {self.race} {self.role}"
    
    def getBaseStats(self, base_health=0, base_magic=0):
        if self.race == 'Human':
            base_health = 10
            base_magic = 10
        elif self.race == 'Caporian':
            base_health = 7
            base_magic = 13
        elif self.race == 'Tecalan':
            base_health = 15
            base_magic = 5
        elif self.race == 'Falixi':
            base_health = 11
            base_magic = 9
        else:
            base_health = 13
            base_magic = 7
        return base_health, base_magic



print("Welcome to the Eldan Character Generator.")
print("Creating a character for you:\n")
player_character = Character()
player_race = player_character.character_race()
player_role = player_character.character_role()
player_baseStats = player_character.getBaseStats()

if player_race == 'Tecalan' and player_role == 'Wizard':
    player_role = 'Shaman'
elif player_race == 'Human' and player_role == 'Jokester':
    player_role = 'Bard'
elif player_race == 'Caporian' and player_role == 'Fighter':
    player_role = 'Protector'
else:
    pass



print(f"Your character is a...{player_race} {player_role}\nYour base stats are: {player_baseStats}")

