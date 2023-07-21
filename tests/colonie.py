#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

# ------------------------------------------------------------------------------------
# Simulation des colonnies
#   Jeu assemble une grille sur laquelle on installe
#     - des terrains (4x4),
#     - une ambassade
#     - des obstacles
#   Les terrains peuvent recevoir
#     - des routes
#     - des modules d'habitation
#     - des modules de production
#     - des modules de diplomatie
#
# les rues sont connectées entre elles et à l'ambassade
# Les bâtiments diplomatiques gagnent plus de diplomatie s'ils sont connectés à l'ambassade
#
#
# ------------------------------------------------------------------------------------


class Object(object):
    def __init__(self, x: int, y: int):
        self.dx = x
        self.dy = y
        self.dx = None
        self.dy = None

    def install(self, grille):
        """
        l'objet a été positionné (x, y)
        On va remplir la grille
        """
        if self.dx is None:
            return

        for x in range(self.dx):
            for y in range(self.dy):
                grille[x, y] = True

    def contact(self, ambassade):
        for x in (self.x, self.x + self.dx):
            for y in (self.y, self.y + self.dy):
                if ambassade.contact(x, y):
                    return True
        return False


class Terrain(Object):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.dx = 4
        self.dy = 4
        self.occupe = False
        print("terrain", x, y)

    def install(self, grille):
        self.occupe = True


class Ambassade(Object):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.dx = 9
        self.dy = 6
        self.occupe = False
        print("ambassade", x, y)

    def contact(self, x: int, y: int):
        return (x == (self.x - 1)) or \
               (x == (self.x + self.dx + 1)) or \
               (y == (self.y - 1)) or \
               (y == (self.y + self.dy + 1))


class Obstacle(Object):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.dx = 1
        self.dy = 1


class Rue(Object):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.dx = 1
        self.dy = 1


class Habitat(Object):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        pass


class Producteur(Object):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        pass


class Diplomatie(Object):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.diplomatie = 0
        self.connecte = False


class Jeu(object):
    def __init__(self):
        self.grille = np.zeros((7*4, 7*4))
        self.terrains = []
        self.pièces = 0
        self.diplomatie = 0

    def add_terrain(self, x: int, y: int):
        terrain = Terrain(x, y)
        self.terrains.append(terrain)
        terrain.install(self.grille)

    def add_pièces(self, pièces: int):
        self.pièces += pièces

    def remove_pièces(self, pièces: int):
        self.pièces -= pièces
        if self.pièces < 0:
            self.pièces = 0

    def add_diplomatie(self, diplomatie: int):
        self.diplomatie += diplomatie

    def remove_diplomatie(self, diplomatie: int):
        self.diplomatie -= diplomatie
        if self.diplomatie < 0:
            self.diplomatie = 0

# ------------------------------------------------------------------
#
# ------------------------------------------------------------------
