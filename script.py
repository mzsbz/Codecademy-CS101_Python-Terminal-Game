import random
import os

class Player:

    def __init__(self, name, health = 100, lockpick = 5):  
        self.name = name
        self.health = health
        self.lockpick = lockpick
        self.gold = 0
        self.is_alive = True

    def update_status(self, health_change = 0, lockpick_change = 0, gold_change = 0):
        self.health += health_change
        self.lockpick += lockpick_change
        self.gold += gold_change

        # Health will never go above 100
        self.health = min(self.health, 100)

        if self.health <= 0:
            self.is_alive = False

    def attack(self, enemy):
        damage = 10
        enemy.update_status(-damage)

class Enemy:

    enemy_type = [
        {'name': 'Rat', 'health': 10, 'damage': 1, 'steal': 0, 'hit_chance': 75},
        {'name': 'Thief', 'health': 25, 'damage': 5, 'steal': 5, 'hit_chance': 50},
        {'name': 'Blind Ogre', 'health': 50, 'damage': 25, 'steal': 0, 'hit_chance': 25}
        ]

    def __init__(self, game, current_room_number):

        self.game = game

        # No weights for now
        spawn_chance = random.randint(0, 2)

        # print(Enemy.enemy_type[0]['name'])

        self.name = Enemy.enemy_type[spawn_chance]['name']
        self.health = Enemy.enemy_type[spawn_chance]['health']
        self.damage = Enemy.enemy_type[spawn_chance]['damage']
        self.steal = Enemy.enemy_type[spawn_chance]['steal']
        self.hit_chance = Enemy.enemy_type[spawn_chance]['hit_chance']
        self.is_alive = True

    def update_status(self, health_change):
        self.health += health_change

        if self.health <= 0:
            self.is_alive = False

    def attack(self, player):
        player.update_status(-self.damage, 0, -self.steal)

class Room:

    def __init__(self, player, room_number):
        self.current_player = player
        self.current_room_number = room_number
        self.current_room_type = 0

    def room_enemy(self):
        player = self.current_player

        # Spawn Enemy
        enemy = Enemy(game, self.current_room_number)
        message = f"{enemy.name} spawns!"

        game.render(message)

        # Loop Battle
        while player.is_alive and enemy.is_alive:

            # Player Action
            if  game.get_input("Fight? Y/N", "Y"):
                message = f"{player.name} attacks for 10!"
                player.attack(enemy)

                if enemy.is_alive:
                    message += f"\n{enemy.name} ({enemy.health}HP) attacks for {enemy.damage}!"
                    game.render(message)
                    
                    enemy.attack(self.current_player)

            game.render(message)

        # Check if game over
        if player.is_alive:
            game.render(f"{enemy.name} Defeated!")
        else:
            game.render(f"Player Defeated!")
            quit()
        return

    def create_room(self):
        self.current_room_type = 0
        player = self.current_player

        if self.current_room_type == 0:
            self.room_enemy()
            game.continue_game()
        # TEMPORARILY DISABLED, GET TERMINAL UI WORKING FIRST
        #     
        # if self.current_room_type == 1:
        #     player.update_status(gold_change = 25)

        #     return

        # if self.current_room_type == 2:
        #     player.update_status(health_change = 25)

        #     return

class Game:

    def __init__(self, player):
        self.player = player
        self.room_number = 0

    def start(self):
        while player.is_alive:

            room = Room(self.player, self.room_number)
            room.create_room()

            self.room_number += 1

        print("Print Game Over Stats Here")

    def render(self, message = ""):
        os.system('cls' if os.name == 'nt' else 'clear')

        print("=" * 40)
        print(f"Room: {self.room_number} || {player.name} | HP: {player.health} | GP: {player.gold} | LP: {player.lockpick}")
        print("=" * 40)
        print(message)

    def get_input(self, message = "", check_input = ""):
        player_input = input(message).upper()
        return player_input == check_input

    def continue_game(self):
        if input("Continue? Y/N").upper() == "Y":
            return
        else:
            quit()


################################################################################################
################################################################################################

player = Player("Mir")
game = Game(player)

game.start()