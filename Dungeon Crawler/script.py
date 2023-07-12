import random
import os

import ascii_art

class Player:

    def __init__(self, name, health = 100, lockpick = 5):  
        self.name = name
        self.health = health
        self.lockpick = lockpick
        self.gold = 0
        self.damage = 10
        self.is_alive = True

    def update_status(self, health_change = 0, lockpick_change = 0, gold_change = 0):
        self.health += health_change
        self.lockpick += lockpick_change
        self.gold += gold_change

        if self.health <= 0:
            self.health = 0
            self.is_alive = False

    def attack(self, enemy):
        is_hit = [0, 1]
        damage_mult = random.choices(is_hit, weights=[enemy.hit_chance, 100 - enemy.hit_chance], k=1)
        enemy.update_status(-self.damage * damage_mult[0])

        return damage_mult[0] == 1

class Enemy:

    enemy_type = [
        {'name': 'Rat', 'health': 10, 'damage': 1, 'steal': 0, 'hit_chance': 75},
        {'name': 'Thief', 'health': 25, 'damage': 5, 'steal': 5, 'hit_chance': 50},
        {'name': 'Blind Ogre', 'health': 50, 'damage': 25, 'steal': 0, 'hit_chance': 25}
        ]

    def __init__(self, game, current_room_number):

        self.game = game

        # Weighted random enemy type
        enemy_types = [0, 1, 2]
        random_enemy = random.choices(enemy_types, weights=[50, 35, 15], k=1)

        # print(Enemy.enemy_type[0]['name'])

        self.name = Enemy.enemy_type[random_enemy[0]]['name']
        self.health = Enemy.enemy_type[random_enemy[0]]['health']
        self.damage = Enemy.enemy_type[random_enemy[0]]['damage']
        self.steal = Enemy.enemy_type[random_enemy[0]]['steal']
        self.hit_chance = Enemy.enemy_type[random_enemy[0]]['hit_chance']
        self.is_alive = True

    def update_status(self, health_change):
        self.health += health_change

        if self.health <= 0:
            self.is_alive = False

    def attack(self, player):
        is_hit = [0, 1]
        damage_mult = random.choices(is_hit, weights=[100 - self.hit_chance, self.hit_chance], k=1)
        player.update_status(-self.damage * damage_mult[0], 0, -self.steal)
        
        return damage_mult[0] == 1

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
                did_player_hit = player.attack(enemy)

                if did_player_hit:
                    message = f"{player.name} attacks for 10!"
                else:
                    message = f"{player.name} misses!"

                if enemy.is_alive:
                    did_enemy_hit = enemy.attack(self.current_player)
                    
                    if did_enemy_hit:
                        message += f"\n{enemy.name} ({enemy.health}HP) attacks for {enemy.damage}!"
                    else:
                        message += f"\n{enemy.name} ({enemy.health}HP) misses!"

                    game.render(message)

            else:
                game.render_gameover(f"You run away!")      

            game.render(message)

        # Check if game over
        if player.is_alive:
            game.render(f"{enemy.name} Defeated!")
        else:
            game.render_gameover(f"Player Defeated!")   
        return

    def room_treasure(self):
        player.update_status(gold_change = 25)
        game.render("You found a treasure room! (+25 GP)")

    def room_fountain(self):
        player.update_status(health_change = 25)
        game.render("You found a fountain! (+25 HP)")

    def create_room(self):

        # Weighted random room type
        room_types = [0, 1, 2]
        random_room = random.choices(room_types, weights=[75, 20, 5], k=1)
        self.current_room_type = random_room[0]

        if self.current_room_type == 0:
            self.room_enemy()
            game.continue_game()
            
        if self.current_room_type == 1:
            self.room_treasure()
            game.continue_game()

        if self.current_room_type == 2:
            self.room_fountain()
            game.continue_game()

class Game:

    def __init__(self, player):
        self.player = player
        self.room_number = 0

    def start(self):
        self.render_start()
        self.continue_game("Start Game? Y/N")

        while player.is_alive:

            room = Room(self.player, self.room_number)
            room.create_room()

            self.room_number += 1

        print("Print Game Over Stats Here")

    def render(self, message = ""):
        os.system('cls' if os.name == 'nt' else 'clear')

        print("=" * 100)
        print(f"Room: {self.room_number} || {player.name} | HP: {player.health} | GP: {player.gold} | LP: {player.lockpick}")
        print("=" * 100)
        if message:
            print(message)

    def get_input(self, message = "", check_input = ""):
        player_input = input(message).upper()
        return player_input == check_input

    def continue_game(self, message = "Continue? Y/N"):
        if input(message).upper() == "Y":
            return
        else:
            self.render_gameover(f"You surrendered!")

    def render_start(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("=" * 100)
        print(ascii_art.title)
        print("=" * 100)

    def render_gameover(self, reason):
        self.render()

        print("=" * 100)
        print(ascii_art.gameover)
        print("=" * 100)

        print("\n", reason)

        quit()

################################################################################################
################################################################################################

player = Player("Mir")
game = Game(player)

game.start()