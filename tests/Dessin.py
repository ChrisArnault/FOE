import os
import sys
import numpy as np
import cv2

"""
event:
1 btn left down
4 btn left up

1 click down
4 click up

2 btn right down
5 btn right up
3 btn middle down
6 btn middle up

7 2-click
7 2-btn left
8 2-btn right
9 2-btn middle

"""

class Terrain(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Obstacle(object):
    def __init__(self, cell1, cell2):
        self.cell1 = cell1
        self.cell2 = cell2

class Game(object):
    cell_width = 20
    cell_height = 20

    terrain_width = 4 * cell_width
    terrain_height = 4 * cell_height

    terrains_in_width = 7
    terrains_in_height = 7

    margin = 10
    halfmargin = 5

    panel_x = margin
    panel_y = margin
    panel_width = 200
    panel_height = 400

    board_x = margin + panel_width + margin
    board_y = margin
    board_width = terrains_in_width * terrain_width
    board_height = terrains_in_height * terrain_height

    image_width = margin + panel_width + margin + board_width + margin
    image_height = margin + board_height + margin

    blue = (255, 0, 0)
    green = (0, 255, 0)
    red = (0, 0, 255)

    def __init__(self):
        self.img = np.zeros((self.image_height, self.image_width, 3),
                            np.uint8)
        self.command = np.zeros((200, 200, 3), np.uint8)

        self.panel()
        self.board()

        self.moving = False
        self.moving_obstacle = None

        cv2.namedWindow('image')
        cv2.setMouseCallback('image', self.callback)

    def panel(self):
        cv2.rectangle(self.img,
                      pt1=(self.panel_x - self.halfmargin, self.panel_y - self.halfmargin),
                      pt2=(self.panel_x + self.panel_width + self.halfmargin, self.panel_y + self.panel_height + self.halfmargin),
                      color=self.red, thickness=2)

        self.draw_obstacle(Obstacle(( 1,  1), ( 2,  1)), arg="panel")
        self.draw_obstacle(Obstacle(( 1,  3), ( 1,  4)), arg="panel")

    def board(self):
        cv2.rectangle(self.img,
                      pt1=(self.board_x - self.halfmargin, self.board_y - self.halfmargin),
                      pt2=(self.board_x + self.board_width + self.halfmargin, self.board_y + self.board_height + self.halfmargin),
                      color=self.red, thickness=2)

        self.terrains = np.zeros((self.terrains_in_height, self.terrains_in_width), dtype=Terrain)
        for ix in range(self.terrains_in_width):
            for iy in range(self.terrains_in_height):
                self.terrains[iy, ix] = Terrain(ix, iy)

        self.terrains[5, 0] = Terrain(-1, -1)
        self.terrains[5, 6] = Terrain(-1, -1)

        self.terrains[6, 0] = Terrain(-1, -1)
        self.terrains[6, 1] = Terrain(-1, -1)
        self.terrains[6, 5] = Terrain(-1, -1)
        self.terrains[6, 6] = Terrain(-1, -1)

        draw_terrains = np.vectorize(self.draw_terrain)
        draw_terrains(self.terrains)

        self.setup_obstacles()

    def callback(self, event, x, y, flags, param):
        on = ""
        cell_x = 0
        cell_y = 0
        if x > self.panel_x and x < (self.panel_x + self.panel_width) and \
                y > self.panel_y and y < (self.panel_y + self.panel_height):
            on = "panel"
            x -= self.panel_x
            y -= self.panel_y
            cell_x = int(x / self.cell_width)
            cell_y = int(y / self.cell_height)
        elif x > self.board_x and x < (self.board_x + self.board_width) and \
                y > self.board_y and y < (self.board_y + self.board_height):
            on = "board"
            x -= self.board_x
            y -= self.board_y
            cell_x = int(x / self.cell_width)
            cell_y = int(y / self.cell_height)
            terrain_x = int(x / self.terrain_width)
            terrain_y = int(y / self.terrain_height)

        if self.moving:
            print(on, " cell=", cell_x, cell_y, "moving", self.moving_obstacle)
            if event == 4:
                self.moving = False
                self.moving_obstacle = None
        else:
            if event == 1:
                self.moving = True
            elif on == "panel":
                if (cell_x == 1 or cell_x == 2) and cell_y == 1:
                    self.moving_obstacle = "H"
                elif cell_x == 1 and (cell_y == 3 or cell_y == 4):
                    self.moving_obstacle = "V"
                print("panel cell=",    cell_x, cell_y, "event", event, self.moving, self.moving_obstacle)
            elif on == "board":
                print("board terrain=", terrain_x, terrain_y, "cell=", cell_x, cell_y)

    def setup_obstacles(self):
        self.obstacles = np.array([
            Obstacle(( 1,  1), ( 2,  1)),
            Obstacle(( 4,  1), ( 4,  2)),
            Obstacle((11,  2), (11,  3)),
            Obstacle((14,  2), (15,  2)),
            Obstacle((18,  1), (19,  1)),
            Obstacle((23,  2), (23,  3)),
            Obstacle((24,  1), (25,  1)),

            Obstacle(( 0,  7), ( 1,  7)),
            Obstacle(( 6,  7), ( 7,  7)),
            Obstacle(( 9,  7), (10,  7)),
            Obstacle((12,  5), (12,  6)),
            Obstacle((17,  6), (18,  6)),
            Obstacle((21,  5), (21,  6)),
            Obstacle((26,  4), (26,  5)),

            Obstacle(( 1, 11), ( 2, 11)),
            Obstacle(( 5, 10), ( 5, 11)),
            Obstacle((26,  8), (26,  9)),

            Obstacle(( 1, 15), ( 2, 15)),
            Obstacle(( 4, 15), ( 5, 15)),
            Obstacle((27, 12), (27, 13)),

            Obstacle(( 1, 18), ( 1, 19)),
            Obstacle(( 7, 18), ( 7, 19)),
            Obstacle((20, 16), (20, 17)),
            Obstacle((25, 17), (25, 18)),

            Obstacle(( 7, 21), ( 7, 22)),
            Obstacle((11, 20), (11, 21)),
            Obstacle((12, 22), (12, 23)),
            Obstacle((18, 23), (19, 23)),
            Obstacle((21, 21), (22, 21)),

            Obstacle(( 9, 24), (10, 24)),
            Obstacle((12, 27), (13, 27)),
            Obstacle((16, 27), (17, 27))
        ])

        # print("setup_obstacles", self.obstacles.shape, self.obstacles)
        # self.draw_obstacle(self.obstacles[0])

        draw_obstacles = np.vectorize(self.draw_obstacle)
        draw_obstacles(self.obstacles, arg="board")


    def draw_cell(self, cell, fill_color, arg="board"):
        x = cell[0]*self.cell_width
        y = cell[1]*self.cell_height
        where = self.img
        if arg == "board":
            x += self.board_x
            y += self.board_y
        elif arg == "panel":
            x += self.panel_x
            y += self.panel_y
        cv2.rectangle(where, (x, y), (x + self.cell_width, y + self.cell_height), fill_color, -1)

    def draw_obstacle(self, obstacle, arg="img"):
        # print("draw_obstacle", obstacle.shape, obstacle)
        cell1 = obstacle.cell1
        cell2 = obstacle.cell2
        # print("draw_obstacle", obstacle.shape, obstacle, cell1, cell2)
        self.draw_cell(cell1, (255, 255, 255), arg)
        self.draw_cell(cell2, (255, 255, 255), arg)

    def draw_terrain(self, terrain):
        if terrain.x == -1:
            return
        nx = terrain.x
        ny = terrain.y
        x0 = self.board_x + nx * self.terrain_width
        y0 = self.board_y + ny * self.terrain_height

        y = y0
        color = (255, 0, 0)
        cv2.line(self.img, pt1=(x0, y), pt2=(x0 + 4 * self.cell_width - 1, y), color=color, thickness=2)
        for iy in range(1, 4):
            y += self.cell_height
            cv2.line(self.img, pt1=(x0, y), pt2=(x0 + 4 * self.cell_width - 1, y), color=color, thickness=1)
        y += self.cell_height
        cv2.line(self.img, pt1=(x0, y), pt2=(x0 + 4 * self.cell_width - 1, y), color=color, thickness=2)

        x = x0
        cv2.line(self.img, pt1=(x, y0), pt2=(x, y0 + 4 * self.cell_height - 1), color=color, thickness=2)
        for ix in range(1, 4):
            x += self.cell_width
            cv2.line(self.img, pt1=(x, y0), pt2 = (x, y0 + 4*self.cell_height - 1), color=color, thickness=1)
        x += self.cell_width
        cv2.line(self.img, pt1=(x, y0), pt2 = (x, y0 + 4*self.cell_height - 1), color=color, thickness=2)

# print(terrains, terrains[0, 0])
# draw_terrain(terrains[0, 0])

game = Game()

mode = True

while(1):
    cv2.imshow('image', game.img)
    # cv2.imshow('command', game.command)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break

cv2.destroyAllWindows()
