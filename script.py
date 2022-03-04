import random

class Player:

    def __init__(self, name, health = 100, lockpick = 5):
        self.name = name
        self.health = health
        self.lockpick = lockpick
        self.gold = 0

    def update_status(self, health_change, lockpick_change, gold_change):
        self.health += health_change
        self.lockpick += lockpick_change
        self.gold += gold_change

        if self.health < 0:
            print(f"Player HP: {self.health}")
            print("Player defeated")
        else:
            print(f"Player HP: {self.health}")

    def attack(self, enemy):
        damage = 10
        enemy.update_status(-damage)

class Enemy:

    enemy_type = [
        {'name': 'Rat', 'health': 10, 'damage': 1, 'steal': 0, 'hit_chance': 75},
        {'name': 'Thief', 'health': 25, 'damage': 5, 'steal': 5, 'hit_chance': 50},
        {'name': 'Blind Ogre', 'health': 50, 'damage': 25, 'steal': 0, 'hit_chance': 25}
        ]

    def __init__(self, current_room_number):

        # No weights for now
        spawn_chance = random.randint(0, 2)

        # print(Enemy.enemy_type[0]['name'])

        self.name = Enemy.enemy_type[spawn_chance]['name']
        self.health = Enemy.enemy_type[spawn_chance]['health']
        self.damage = Enemy.enemy_type[spawn_chance]['damage']
        self.steal = Enemy.enemy_type[spawn_chance]['steal']
        self.hit_chance = Enemy.enemy_type[spawn_chance]['hit_chance']

    def update_status(self, health_change):
        self.health += health_change

        if self.health <= 0:
            print(f"Enemy HP: {self.health}")
            print("Enemy defeated")
        else:
            print(f"Enemy HP: {self.health}")

    def attack(self, player):
        player.update_status(-self.damage, 0, -self.steal)

class Room:

    def __init__(self, player, room_number):
        self.current_player = player
        self.current_room_number = room_number
        self.current_room_type = 0

    def create_room(self):
        self.current_room_type = random.randint(0, 2)
        player = self.current_player

        if self.current_room_type == 0:
            # Spawn Enemy
            enemy = Enemy(self.current_room_number)

            enemy.attack(self.current_player)
            player.attack(enemy)

################################################################################################
################################################################################################

player = Player('Mir')
enemy = Enemy(0)

player.attack(enemy)
enemy.attack(player)

