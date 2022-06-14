import random

class Character:
    def __init__(self) -> None:
        # self.base_health = base_health
        # self.base_magic = base_magic
        # self.health_Stats = health_Stats
        # self.magic_Stats = magic_Stats
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
    
    def getBaseRacialStats(self, race):
        health_dict = {'Human':10, 'Caporian':7, 'Tecalan':15, 'Falixi':11, 'Karnian':13}
        magic_dict = {'Human':10, 'Caporian':13, 'Tecalan':5, 'Falixi':9, 'Karnian':7}
        base_health = 0
        base_magic = 0
        
        if race == 'Human':
            base_health = health_dict['Human']
            base_magic = magic_dict['Human']
        elif race == 'Caporian':
            base_health = health_dict['Caporian']
            base_magic = magic_dict['Caporian']
        elif race == 'Tecalan':
            base_health = health_dict['Tecalan']
            base_magic = magic_dict['Tecalan']
        elif race == 'Falixi':
            base_health = health_dict['Falixi']
            base_magic = magic_dict['Falixi']
        elif race == 'Karnian':
            base_health = health_dict['Karnian']
            base_magic = magic_dict['Karnian']
        else:
            pass

        return base_health, base_magic

    def getBaseRoleStats(self, role):
        role_health = {'Fighter':20, 'Archer':14, 'Wizard':9, 'Jokester':10, 'Valkyrie':18}
        role_magic = {'Fighter':0, 'Archer':6, 'Wizard':11, 'Jokester':10, 'Valkyrie':2}

        health_Stats = 0
        magic_Stats = 0
        if role == 'Fighter':
            health_Stats = role_health['Fighter']
            magic_Stats = role_magic['Fighter']
        elif role == 'Archer':
            health_Stats = role_health['Archer']
            magic_Stats = role_magic['Archer']
        elif role == 'Wizard':
            health_Stats = role_health['Wizard']
            magic_Stats = role_magic['Wizard']
        elif role == 'Jokester':
            health_Stats = role_health['Jokester']
            magic_Stats = role_magic['Jokester']
        elif role == 'Valkrie':
            health_Stats = role_health['Valkyrie']
            magic_Stats = role_magic['Valkyrie']
        else:
            pass
        return health_Stats, magic_Stats



print("Welcome to the Eldan Character Generator.")
print("Creating a character for you:\n")
player_character = Character()
player_race = player_character.character_race()
player_role = player_character.character_role()
player_baseRacialStats = player_character.getBaseRacialStats(player_race)
player_baseRoleStats = player_character.getBaseRoleStats(player_role)
# player_health, player_magic = ('')

if player_race == 'Tecalan' and player_role == 'Wizard':
    player_role = 'Shaman'
elif player_race == 'Human' and player_role == 'Jokester':
    player_role = 'Bard'
elif player_race == 'Caporian' and player_role == 'Fighter':
    player_role = 'Protector'
else:
    pass



print(f"Your character is a...{player_race} {player_role}\nYour base stats are: {player_baseRacialStats}.\nYour role stats are: {player_baseRoleStats}")

