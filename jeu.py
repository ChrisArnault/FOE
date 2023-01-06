#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle
import numpy as np
import tkinter as tk
from tkinter import ttk

Data = {
    # Base de données
    'terrains_vrais': [
         #. .  .  .  |   .  .  .  .  |   .  .  .  .  |   .  .  .
         0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0,  # (0, 0),
         0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0,  # (0, 0),
         0, 0, 0, 1, 1,  1, 1, 1, 1, 1,  1, 1, 1, 1, 1,  1, 0, 0,  # (3, 13),
         0, 0, 0, 1, 1,  1, 1, 1, 1, 1,  1, 1, 1, 1, 1,  1, 0, 0,  # (3, 13),
         0, 0, 0, 1, 1,  1, 1, 1, 1, 1,  1, 1, 1, 1, 1,  1, 0, 0,  # (3, 13),

         0, 0, 0, 1, 1,  1, 1, 1, 1, 1,  1, 1, 1, 1, 1,  1, 1, 0,  # (3, 14),
         0, 0, 0, 1, 1,  1, 1, 1, 1, 1,  1, 1, 1, 1, 1,  1, 1, 0,  # (3, 14),
         0, 0, 0, 1, 1,  1, 1, 1, 1, 1,  1, 1, 1, 1, 1,  1, 1, 0,  # (3, 14),
         0, 0, 0, 1, 1,  1, 1, 1, 1, 1,  1, 1, 1, 1, 1,  1, 1, 0,  # (3, 14),
         0, 0, 0, 1, 1,  1, 1, 1, 1, 1,  1, 1, 1, 1, 1,  1, 1, 0,  # (3, 14),

         0, 0, 0, 1, 1,  1, 1, 1, 1, 1,  1, 1, 1, 1, 1,  0, 0, 0,  # (3, 12),
         0, 0, 0, 0, 0,  1, 1, 1, 1, 1,  1, 1, 1, 1, 0,  0, 0, 0,  # (5, 9),
         0, 0, 0, 0, 0,  1, 1, 1, 1, 1,  1, 1, 1, 1, 0,  0, 0, 0,  # (5, 9),
         0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0,  # (0, 0),
         0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0,  # (0, 0),

         0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0,  # (0, 0),
         0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0,  # (0, 0),
         0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0,  # (0, 0),
    ],

    'batiments': {},
    'last_id': 0,

    # Configuration
    'geom_width': 1700,
    'geom_height': 1000,

    'rows': 18,
    'columns': 18,

    'terrains_possibles': [
            #. .  .  .  |   .  .  .  .  |   .  .  .  .  |   .  .  .
            0, 0, 1, 1, 1,  1, 1, 1, 1, 1,  1, 0, 0, 0, 0,  0, 0, 0,  # (2, 9)
            0, 0, 1, 1, 1,  1, 1, 1, 1, 1,  1, 0, 0, 0, 0,  0, 0, 0,  # (2, 9)
            0, 1, 1, 1, 1,  1, 1, 1, 1, 1,  1, 1, 1, 1, 1,  1, 0, 0,  # (1, 15)
            0, 1, 1, 1, 1,  1, 1, 1, 1, 1,  1, 1, 1, 1, 1,  1, 0, 0,  # (1, 15)
            1, 1, 1, 1, 1,  1, 1, 1, 1, 1,  1, 1, 1, 1, 1,  1, 0, 0,  # (0, 16)

            1, 1, 1, 1, 1,  1, 1, 1, 1, 1,  1, 1, 1, 1, 1,  1, 1, 1,  # (0, 18)
            1, 1, 1, 1, 1,  1, 1, 1, 1, 1,  1, 1, 1, 1, 1,  1, 1, 1,  # (0, 18)
            1, 1, 1, 1, 1,  1, 1, 1, 1, 1,  1, 1, 1, 1, 1,  1, 1, 1,  # (0, 18)
            1, 1, 1, 1, 1,  1, 1, 1, 1, 1,  1, 1, 1, 1, 1,  1, 1, 1,  # (0, 18)
            1, 1, 1, 1, 1,  1, 1, 1, 1, 1,  1, 1, 1, 1, 1,  1, 1, 1,  # (0, 18)

            1, 1, 1, 1, 1,  1, 1, 1, 1, 1,  1, 1, 1, 1, 1,  1, 1, 1,  # (0, 18)
            1, 1, 1, 1, 1,  1, 1, 1, 1, 1,  1, 1, 1, 1, 1,  1, 1, 1,  # (0, 18)
            1, 1, 1, 1, 1,  1, 1, 1, 1, 1,  1, 1, 1, 1, 1,  1, 1, 1,  # (0, 18)
            1, 1, 1, 1, 1,  1, 1, 1, 1, 1,  1, 1, 1, 1, 1,  1, 1, 1,  # (0, 18)
            0, 0, 1, 1, 1,  1, 1, 1, 1, 1,  1, 1, 1, 1, 1,  1, 1, 1,  # (2, 16)

            0, 0, 1, 1, 1,  1, 1, 1, 1, 1,  1, 1, 1, 1, 1,  1, 0, 0,  # (2, 14)
            0, 0, 0, 0, 1,  1, 1, 1, 1, 1,  1, 1, 1, 1, 1,  1, 0, 0,  # (4, 12)
            0, 0, 0, 0, 0,  0, 0, 0, 0, 1,  1, 1, 0, 0, 0,  0, 0, 0,  # (9, 3)
        ],

    'size': 20,
    'margin': 100,

    'types': ['Habitation', 'Militaire', 'Production', 'Marchandise', 'Culture', 'Décoration', 'Route', 'GM', 'Hotel de Ville', 'Autre', ],
    'colors': ['cyan', 'orange', 'RoyalBlue1', 'yellow', 'snow', 'green2', 'gray50', 'hot pink', 'red', 'bisque3', ],

    'type_terrain': -1,
    'color_terrain': "gray60",
    'color_terrain_vide': "gray80",
    'color_line': "green",
}

class Batiment(object):
    def __init__(self, nom, rows, columns, type):
        self.id = Data['last_id']
        Data['last_id'] += 1
        self.nom = nom
        self.rows = rows
        self.columns = columns
        if type == "terrain":
            self.type = Data['type_terrain']
        else:
            self.type = Data['types'].index(type)
        self.row = None
        self.column = None
        self.graphs = None

    def __repr__(self):
        return "Bat {} @ r={} c={} t={}".format(self.nom, self.row, self.column, self.type)

    def install(self, row, column):
        self.row = row
        self.column = column
        Data['batiments'][self.id] = self
        if self.type == Data['type_terrain']:
            """
            on vient d'ajouter le batiment dans le dictionnaire
            il faut maintenant ajouter le "1" dans la matrice "terrains_vrais"
            """
            i = int(row/4) * Data['columns'] + int(column/4)
            Data['terrains_vrais'][i] = 1
        else:
            "les batiments existent dans la DTB. ils seront naturellement dessinés au démarrage"
            pass

    def collision(self, other, r, c):
        # if self.row == None or self.column == None: return False
        # if other.row == None or other.column == None: return False

        def test_columns(c):
            if c > self.column + self.columns: return False
            if self.column > c + other.columns: return False
            if c >= self.column and c < self.column + self.columns: return True
            if self.column >= c and self.column < c + other.columns: return True
        def test_rows(r):
            if r > self.row + self.rows: return False
            if self.row > r + other.rows: return False
            if r >= self.row and r < self.row + self.rows: return True
            if self.row >= r and self.row < r + other.rows: return True

        collision_column =  test_columns(c)
        collision_row = test_rows(r)
        return collision_column and collision_row

    def set_tag(self, tag):
        pass

    def tag(self):
        return "tag{}".format(self.id)

    def draw(self, canvas, x=None, y=None):
        size = Data['size']
        margin = Data['margin']
        if x == None:
            x = margin + self.column * size
        if y == None:
            y = margin + self.row * size

        if self.type == Data['type_terrain']:
            color = Data['color_terrain']
        else:
            color = Data['colors'][self.type]

        rect = canvas.create_rectangle(x, y,
                                       x + self.columns * size,
                                       y + self.rows * size,
                                       width=1, outline="red", fill=color,
                                       tag=self.tag())

        self.graphs = [rect]

        color = Data['color_line']
        for r in range(self.rows):
            if r == 0 : continue
            x1 = x
            y1 = y + r * size
            x2 = x + self.columns * size
            y2 = y1
            self.graphs.append(canvas.create_line(x1, y1, x2, y2, width=1, fill=color, tag=self.tag()))
        for c in range(self.columns):
            if c == 0 : continue
            x1 = x + c * size
            y1 = y
            x2 = x1
            y2 = y1 + self.rows * size
            self.graphs.append(canvas.create_line(x1, y1, x2, y2, width=1, fill=color, tag=self.tag()))

        return rect

class Terrain(Batiment):
    def __init__(self):
        super().__init__("terrain", 4, 4, "terrain")

class Jeu(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('ForgeOfEmpires')
        self.geometry("{}x{}".format(Data['geom_width'] + 20,
                                     Data['geom_height'] + 20))
        self.resizable(True, True)
        self.grid()
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=20)
        self.configure()

        self.batiment = None
        self.moving = None
        self.moving_case = None

    def canvas_geometry(self):
        full_width = (2*Data['margin'] + Data['columns'] * Data['size'] * 4)
        full_height = (2*Data['margin'] + Data['rows'] * Data['size'] * 4)
        width = Data['geom_width'] - 10
        height = Data['geom_height'] - 200

        return width, height, full_width, full_height

    def up(self, r=None, c=None):
        if self.batiment != None:
            objs = self.dessin.find_withtag(self.batiment.tag())
            # print("Moving2> tag=", self.batiment.tag(), "objs=", objs)
            for obj in objs:
                self.dessin.delete(obj)

            if r != None:
                print("Install batiment> r=", r, "c=", c)
                self.batiment.install(r, c)

            self.batiment.draw(self.dessin)

        # print("removing bat", n)
        self.batiment = None
        # self.dessin.delete(self.moving)
        self.moving = None
        self.dessin.delete(self.moving_case)
        self.moving_case = None

    def configure_canvas(self):
        frame = tk.Frame(self)
        frame.grid(row=0, column=0)

        width, height, full_width, full_height = self.canvas_geometry()

        self.dessin = tk.Canvas(frame, bg="ivory",
                                width=width,
                                height=height,
                                scrollregion=(0, 0, full_width, full_height))
        self.dessin.grid(row=0, column=0)

        def get_case(x, y):
            # retourne la case et le terrain (valide) à la coordonnée x, y

            margin = Data['margin']
            size = Data['size']

            x -= margin
            c = int(x / size)
            y -= margin
            r = int(y / size)

            if x < 0 or y < 0: return None

            rows = Data['rows']
            columns = Data['columns']

            if r < 0 or r >= rows*4: return None
            if c < 0 or c >= columns*4: return None

            tr = int(r / 4)
            tc = int(c / 4)

            terrains_possibles = Data['terrains_possibles']
            i = rows * tr + tc

            if terrains_possibles[i] == 0: return None

            # print("get_case> ", "x=", x, "y=", y, "r=", r, "c=", c, "i=", i, "t=", terrains_possibles[i], "tr=", tr, "tc=", tc)

            return (r, c, tr, tc)

        def get_terrain_vrai(tr, tc):
            rows = Data['rows']
            columns = Data['columns']
            terrains_vrais = Data['terrains_vrais']
            i = rows * tr + tc
            if terrains_vrais[i] == 1:
                return tr, tc
            return None, None

        def scrolling(e):
            # Calcule les coordonnées absolues par rapport à la position des scroll bars
            width, height, full_width,  full_height = self.canvas_geometry()

            d = Data['margin']
            y1, y2 = y_scroll.get()
            Y1, Y2 = int(y1 * (full_height - d)), int(y2 * (full_height - d))
            x1, x2 = x_scroll.get()
            X1, X2 = int(x1 * full_width), int(x2 * full_width)

            x = e.x + X1 - 2
            y = e.y + Y1

            # print("action> e.y=", e.y , "y1=", int(y1*100), "y2=", int(y2*100), "Y1=", Y1, "Y2=", Y2, "y=", y)

            return x, y

        def action(mode, e):
            x, y = scrolling(e)

            if self.batiment == None: return

            # animation sous la souris, anciennes valeurs
            global ex, ey

            if self.moving == None:
                self.moving = self.batiment.draw(self.dessin, x, y)
            else:
                objs = self.dessin.find_withtag(self.batiment.tag())
                for obj in objs:
                    # print("move bat>", "x=", x, "y=", y)
                    self.dessin.move(obj, x - ex, y - ey)

            ex = x
            ey = y

            n = self.batiment.nom
            bat_type = self.batiment.type

            # print("mode=", mode)

            # on trouve la case et le terrain sous le curseur
            result = get_case(x, y)

            if result == None: return

            # print("on est sur la zone valide")

            r, c, tr, tc = result

            # print("after get_case> ", "r=", r, "c=", c, "tr=", tr, "tc=", tc, "type=", bat_type)

            type_terrain = Data['type_terrain']

            if bat_type != type_terrain:
                print("on positionne un batiment")
                tr_vrai, tc_vrai = get_terrain_vrai(tr, tc)
                if tr_vrai == None: return

                # on va tester les collisions avec des batiments existants
                for id in Data['batiments']:
                    b = Data['batiments'][id]
                    if b.type == type_terrain: continue
                    if b.collision(self.batiment, r, c):
                        print("collision entre ", b.id, b.nom, "et", self.batiment.id, self.batiment.nom)
                        return

                # Mise en place d'un batiment normal
                if self.moving_case != None:
                    self.dessin.delete(self.moving_case)
                self.moving_case = self.case(r, c, line_color='yellow')
                print(mode, "x=", x, "y=", y, "nom=", n, "r=", r, "c=", c, "tr=", tr, "tc=", tc)

                if mode == "up":
                    self.up(r, c)

            else:
                print("on positionne un terrain")
                # Mise en place d'un terrain
                rows = Data['rows']
                columns = Data['columns']
                # terrains_possibles = Data['terrains_possibles']
                terrains_vrais = Data['terrains_vrais']
                i = rows * tr + tc

                if terrains_vrais[i] == 1: return
                if r % 4 != 0: return
                if c % 4 != 0: return

                found = False

                # on vérifie si le terrain choisi est contigu avec un terrain_vrai

                for dr in range(2):
                    rr = tr + (dr * 2 - 1)
                    if rr >= 0 and rr < rows:
                        i_vrai = rows * rr + tc
                        # print("voisins>", "rr=", rr, "tc=", tc, "i_vrai=", i_vrai, "t=", terrains_vrais[i_vrai])
                        if terrains_vrais[i_vrai] == 1:
                            found = True
                            break

                if not found:
                    for dc in range(2):
                        cc = tc + (dc * 2 - 1)
                        if cc >= 0 and cc < columns:
                            i_vrai = rows * tr + cc
                            # print("voisins>", "tr=", tr, "cc=", cc, "i_vrai=", i_vrai, "t=", terrains_vrais[i_vrai])
                            if terrains_vrais[i_vrai] == 1:
                                found = True
                                break

                if found:
                    if self.moving_case != None:
                        self.dessin.delete(self.moving_case)

                    """
                    Les contraintes de placements sont déjà validées
                    - r et c doivent multiples de 4
                    - r et c doivent se situer dans la zone des nouveaux terrains
                    - on ne peut placer un terrain que contre un terrain existant
                    Ensuite, on sa modifier la ligne de configuration
                    """

                    self.moving_case = self.case(r, c, line_color='yellow')

                    print(mode, "x=", x, "y=", y, "nom=", n, "r=", r, "c=", c, "tr=", tr, "tc=", tc)
                    if mode == "up":
                        self.up(r, c)

        def move(e):
            action("move", e)

        def button_down(e):
            action("down", e)

        def button_up(e):
            action("up", e)

        # Bind the move function
        self.dessin.bind("<Motion>", move)
        self.dessin.bind("<Button>", button_down)
        self.dessin.bind("<ButtonRelease>", button_up)

        y_scroll = tk.Scrollbar(frame, orient="vertical", command=self.dessin.yview)
        y_scroll.grid(row=0, column=1, sticky="ns")
        x_scroll = tk.Scrollbar(frame, orient="horizontal", command=self.dessin.xview)
        x_scroll.grid(row=1, column=0, sticky="ew")

        self.dessin.config(xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set)

        self.draw_grid()

        self.dessin.config(scrollregion=self.dessin.bbox("all"))

    def configure_combo(self):

        def install():
            self.up()
            n = nom.get()
            try:
                r = int(rows.get())
            except:
                r = 0
            try:
                c = int(columns.get())
            except:
                c = 0
            t = types.get()

            if n != '' and r > 0 and c > 0:
                print("install> ", "nom=", n, "rows=", r, "columns=", c)
                self.batiment = Batiment(n, r, c, t)

        def install_terrain():
            self.up()
            n = "Terrain"
            r = 4
            c = 4

            print("install> terrain")
            self.batiment = Terrain()

        combo_frame = tk.Frame(self)
        combo_frame.grid(row=1, column=0)

        row = 0
        nom = tk.StringVar()
        ttk.Label(combo_frame, text='Nom:').grid(column=0, row=row, sticky=tk.W)
        ttk.Entry(combo_frame, width=30, textvariable=nom).grid(column=1, row=row, columnspan=3, sticky=tk.W)

        row += 1

        rows = tk.StringVar()
        ttk.Label(combo_frame, text='rows:').grid(column=0, row=row, sticky=tk.W)
        ttk.Entry(combo_frame, width=8, textvariable=rows).grid(column=1, row=row, sticky=tk.W)

        columns = tk.StringVar()
        ttk.Label(combo_frame, text='columns:').grid(column=2, row=row, sticky=tk.W)
        ttk.Entry(combo_frame, width=8, textvariable=columns).grid(column=3, row=row, sticky=tk.W)

        row += 1

        types = tk.StringVar()
        ttk.Label(combo_frame, text='type:').grid(column=0, row=row, sticky=tk.W)
        combo = ttk.Combobox(combo_frame, textvariable=types)
        combo['values'] = Data['types']
        combo['state'] = 'readonly'
        combo.current(newindex=0)
        combo.grid(column=1, row=row, sticky=tk.W)

        row += 1

        terrain_button = ttk.Button(combo_frame, text="Terrain", command=install_terrain).grid(column=0, row=row, sticky=tk.W)
        install_button = ttk.Button(combo_frame, text="Install", command=install).grid(column=1, row=row, sticky=tk.W)

    def configure_quit(self):
        quit_frame = tk.Frame(self)
        quit_frame.grid(row=2, column=0)

        def quit():
            for id in Data['batiments']:
                print("bat[", id, "]=", Data['batiments'][id])
            jeu.destroy()

        def quit_save():
            with open('data.pickle', 'wb') as f:
                pickle.dump(Data, f, pickle.HIGHEST_PROTOCOL)
            jeu.destroy()

        row = 0
        ttk.Button(quit_frame, text="Quit", command=quit).grid(column=0, row=row, sticky=tk.W)
        ttk.Button(quit_frame, text="Quit & Save", command=quit_save).grid(column=1, row=row, sticky=tk.W)

    def configure(self):
        ##----- Création des boutons -----##

        self.configure_canvas()
        self.configure_combo()
        self.configure_quit()

    def case(self, row, column, line_color='black', fill_color=''):
        size = Data['size']
        margin = Data['margin']
        x1 = column * size + margin
        y1 = row * size + margin
        x2 = x1 + size
        y2 = y1 + size
        return self.dessin.create_rectangle(x1, y1, x2, y2, width=1, outline=line_color, fill=fill_color)

    def terrain(self, row, column, line_color='black', fill_color=''):
        size = Data['size']
        margin = Data['margin']
        x1 = 4 * column * size + margin
        y1 = 4 * row * size + margin
        x2 = x1 + 4 * size
        y2 = y1 + 4 * size
        self.dessin.create_rectangle(x1, y1, x2, y2, width=1, outline=line_color, fill=fill_color)
        for r in range(4):
            for c in range(4):
                self.case(row * 4 + r, column * 4 + c, line_color=line_color)
        self.dessin.create_rectangle(x1, y1, x2, y2, width=1, outline="red")

    def all_terrains(self):
        color = Data["color_terrain_vide"]
        line_color = Data["color_line"]

        rows = Data["rows"]
        columns = Data["columns"]
        terrains_possibles = Data["terrains_possibles"]

        for r in range(rows):
            for c in range(columns):
                i = r * columns + c
                if terrains_possibles[i] == 1:
                    self.terrain(r, c, line_color=line_color, fill_color=color)

    def terrains(self):
        color = Data["color_terrain"]
        line_color = Data["color_line"]

        rows = Data["rows"]
        columns = Data["columns"]
        terrains_vrais = Data["terrains_vrais"]

        for r in range(rows):
            for c in range(columns):
                i = r * columns + c
                if terrains_vrais[i] == 1:
                    self.terrain(r, c, line_color=line_color, fill_color=color)

    def draw_grid(self):
        color = Data['color_line']
        self.dessin.create_rectangle(1, 1, 1, 1, width=1, outline="red")

        self.all_terrains()
        self.terrains()

        for id in Data['batiments']:
            b = Data['batiments'][id]
            b.draw(self.dessin)

        self.dessin.addtag_all("all")

    def run(self):
        ##----- Programme principal -----##
        self.mainloop()  # Boucle d'attente des événements


if __name__ == '__main__':
    try:
        with open('data.pickle', 'rb') as f:
            Data = pickle.load(f)
        for id in Data:
            print(id)
    except:
        pass

    jeu = Jeu()
    jeu.run()

