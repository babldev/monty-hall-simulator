# -*- coding: utf-8 -*-
import random


class Door(object):
    """Represents a single door"""
    opened = False
    is_car = False

    def open(self):
        self.opened = True

    def __str__(self):
        """Called when we try to print this object"""
        if not self.opened:
            return '🚪'
        elif self.is_car:
            return '🚗'
        else:
            return '🐴'


class Game(object):
    doors = []

    DOORS = 3

    def __init__(self):
        for i in range(self.DOORS):
            self.doors.append(Door())

        random_door = random.randint(0, len(self.doors) - 1)
        self.doors[random_door].is_car = True

    def open_door(self, idx):
        self.doors[idx].open()

    def open_door_with_donkey_other_than_door(self, idx):
        # Start with all door choices [0, 1, 2]
        choices = range(self.DOORS)

        # Remove the specified door from the choices.
        choices.remove(idx)

        # Remove the car if it is still there
        for c_idx in choices:
            if self.doors[c_idx].is_car:
                choices.remove(c_idx)

        # Select a random door from remaining choices and open it.
        rand_idx = random.randint(0, len(choices) - 1)
        self.doors[choices[rand_idx]].open()

    def __str__(self):
        """Called when we try to print this object"""
        return ' '.join(str(door) for door in self.doors)


def prompt_door():
    """Called when we try to print this object"""
    choice = input('Choose door 1, 2, or 3: ')
    return int(choice) - 1  # Convert to 0 index


def play():
    """Run a single game"""
    game = Game()
    print(game)

    # Step 1
    choice = prompt_door()
    game.open_door_with_donkey_other_than_door(choice)
    print(game)

    # Step 2
    choice = prompt_door()
    game.open_door(choice)
    print(game)


play()

