#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle
import tkinter as tk
from tkinter import ttk
import requests
import re


"""
Data décrit toutes les données qui seront sauvegardées dans data.pickle
Si on veut modifier une des donnée:
1) ajouter immédiatement après avoir lu les données par 

        with open('data.pickle', 'rb') as f:
            Data = pickle.load(f)
            
    une ligne du style
    
    Data['size'] = 12
2) exécuter en sauvegardant
3) commenter la ligne ajoutée
"""
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
    'poped': {},
    'last_id': 0,

    # Configuration
    'geom_width': 1700,
    'geom_height': 1000,

    'rows': 18,
    'columns': 18,

    'essais_rows': 5,
    'essais_columns': 5,

'terrains_possibles': [
            #. .  .  .  |   .  .  .  .  |   .  .  .  .  |   .  .  .
            0, 0, 1, 1, 1,  1, 1, 1, 1, 1,  1, 0, 0, 0, 0,  0, 0, 0,  # (2, 9)
            0, 0, 1, 1, 1,  1, 1, 1, 1, 1,  1, 0, 0, 0, 0,  0, 0, 0,  # (2, 9)
            0, 1, 1, 1, 1,  1, 1, 1, 1, 1,  1, 1, 1, 1, 1,  1, 0, 0,  # (1, 15)
            0, 1, 1, 1, 1,  1, 1, 1, 1, 1,  1, 1, 1, 1, 1,  1, 0, 0,  # (1, 15)
            1, 1, 1, 1, 1,  1, 1, 1, 1, 1,  1, 1, 1, 1, 1,  1, 1, 1,  # (0, 16)

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

    'size': 10,
    'margin': 100,

    'realtypes': ['Bâtiments résidentiels',
                  'Bâtiments militaires',
                  'Bâtiments de production',
                  'Bâtiments de marchandises',
                  'Bâtiments culturels',
                  'Décorations',
                  'Route',
                  'Grand Monument',
                  'Hotel de Ville',
                  'Tour',
                  'Bâtiment à production aléatoire',
                  'Autre',
                  'Terrain'],

    'types': ['Habitation',
              'Militaire',
              'Production',
              'Marchandise',
              'Culture',
              'Décoration',
              'Route',
              'GM',
              'Hotel de Ville',
              'Autre',
              'Terrain'],
    'colors': ['cyan', 'orange', 'DodgerBlue2', 'yellow', 'snow', 'green2', 'gray50', 'hot pink', 'red', 'purple1', 'gray65'],

    'connection': ['oui', 'non'],
    'color_terrain': "gray65",
    'color_terrain_vide': "gray85",
    'color_line': "green",
}


def find_batiment(r, c):
    rows = Data['rows']
    columns = Data['columns']
    terrains_possibles = Data['terrains_possibles']

    if r < 0 or r >= rows * 4: return None
    if c < 0 or c >= columns * 4: return None

    tr = int(r / 4)
    tc = int(c / 4)

    i = rows * tr + tc

    if terrains_possibles[i] == 0: return None

    found = None
    for id in Data['batiments']:
        b = Data['batiments'][id]
        if not b.is_terrain():
            try:
                if r >= b.row and r < b.row + b.rows and c >= b.column and c < b.column + b.columns:
                    found = b
                    break
            except:
                # print("Erreur dans fin_batiment> id=", id)
                return None

    if found == None:
        for id in Data['batiments']:
            b = Data['batiments'][id]
            if b.is_terrain():
                if r >= b.row and r < b.row + b.rows and c >= b.column and c < b.column + b.columns:
                    found = b
                    break

    return found


class Batiment(object):
    def __init__(self, nom, rows, columns, type, connected):
        self.id = Data['last_id']
        Data['last_id'] += 1
        self.nom = nom           # le nom

        if type == "Terrain":
            self.type = Data['type'].index(type)
            self.rows = 4  # nombre de lignes occupées par ce bât
            self.columns = 4  # nombre de colonnes occupées par ce bât
        elif type == "route":
            self.type = Data['Route']
            self.rows = 1  # nombre de lignes occupées par ce bât
            self.columns = 1  # nombre de colonnes occupées par ce bât
        else:
            self.attributs(nom)

            self.type = Data['types'].index(type)
            self.rows = rows         # nombre de lignes occupées par ce bât
            self.columns = columns   # nombre de colonnes occupées par ce bât

        self.connected = connected
        self.row = None           # position d'installation
        self.column = None        # position d'installation
        self.graphs = None        # tous les graphiques utilisés pour dessiner le bât
                                  # nécessaire pour effacer ou déplacer

        self.saved = False
        self.att_rue = 0
        self.att_columns = 0
        self.att_rows = 0
        self.att_type = ""

    def is_terrain(self):
        return self.type == Data['types'].index('Terrain')


    def attributs(self, title):
        def rue(s):
            if "Rue:" in s:
                i = s.index("Rue:")
            elif "Rue requise:" in s:
                i = s.index("Rue requise:")
            else:
                self.att_rue = 0
                return

            s = s[i:]
            j = None
            if "Aucune rue requise" in s:
                j = s.index("Aucune rue requise")
                self.att_rue = 0
            else:
                i = s.index("</div>")
                s = s[i + 6:]
                i = s.index("\n")
                m = re.match("(\d+).(\d+)", s[:i].strip())
                self.att_rue = int(m.group(1))

        def taille(s):
            if "Taille:" in s:
                i = s.index("Taille:")
            else:
                self.att_rows = 0
                self.att_columns = 0
                return
            s = s[i:]
            i = s.index("</div>")
            s = s[i + 6:]
            i = s.index("\n")
            m = re.match("(\d+).(\d+)", s[:i].strip())
            self.att_columns = int(m.group(1))
            self.att_rows = int(m.group(2))

        def type(s):
            if "Type:" in s:
                i = s.index("Type:")
                s = s[i:]
                i = s.index("</div>")
                s = s[i + 6:]
                i = s.index("\n")
                t = s[:i].strip()
            else:
                t = "Autre"
            # print("type:", t)
            self.att_type = t

        """
        t = find_from_wiki(title)
        if t is not None:
            if t == "Erreur":
                print("Attributs inaccessibles nom=", title, "id=", self.id)
                return False
            title = t
        """

        prefix = "https://fr.wiki.forgeofempires.com/index.php?title="

        response = requests.get(prefix + title + " - Niv. 1")
        if response.status_code == 404:
            response = requests.get(prefix + title)
            if response.status_code == 404:
                print("Attributs inaccessibles nom=", title, "id=", self.id)
                return False

        s = response.content.decode('utf-8')
        rue(s)
        taille(s)
        type(s)
        print("Attributs> name='{}' rue='{}' RxC='{}x{}' Type={}".format(self.nom, self.att_rue, self.att_rows, self.att_columns, self.att_type))
        return True

    def __repr__(self):
        rue = 0
        if hasattr(self, "att_rue"): rue = self.att_rue
        type = Data['types'][self.type]
        if hasattr(self, "att_type"): type = self.att_type
        return "Batiment [{} id={} rs,cs=({},{}) r,c=({},{}) type=[{}] rue={}]".format(self.nom, self.id,
                                                                                self.rows, self.columns,
                                                                                self.row, self.column,
                                                                                type, rue)

    def is_route(self):
        route = Data['types'].index('Route')
        return self.type == route

    def is_connected(self):
        return self.connected

    def install(self, row, column):
        self.row = row
        self.column = column
        Data['batiments'][self.id] = self
        if self.is_terrain():
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
        """
        Lors d'un déplacement du bât, à la position (r, c) on vérifie si il y a une collision avec
        un autre bât other installé
        """
        # if self.row == None or self.column == None: return False
        # if other.row == None or other.column == None: return False

        def test_columns(c):
            # la colonne est en dehors du bât
            if c > self.column + self.columns: return False
            # le bât est en dehors de other
            if self.column > c + other.columns: return False
            # c est dans à l'intérieur du bât
            if c >= self.column and c < self.column + self.columns: return True
            # le bât se supperpose à other
            if self.column >= c and self.column < c + other.columns: return True

        def test_rows(r):
            if r > self.row + self.rows: return False
            if self.row > r + other.rows: return False
            if r >= self.row and r < self.row + self.rows: return True
            if self.row >= r and self.row < r + other.rows: return True

        collision_column =  test_columns(c)
        collision_row = test_rows(r)
        return collision_column and collision_row

    def must_connect(self, row, column):
        """
        on teste si il existe une route autour du bât à la position (r, c)
        """

        def test_is_route(r, c):
            b = find_batiment(r, c)
            if b is None: return False
            return b.is_route()

        # rangée au dessus du bât
        if test_is_route(row - 1, column - 1): return True
        for cc in range(self.columns + 1):
            if test_is_route(row - 1, column + cc): return True
        if test_is_route(row - 1, column + 1): return True

        # colonne à gauche du bât
        for rr in range(self.rows + 1):
            if test_is_route(row + rr, column - 1): return True

        # colonne à droite du bât
        for rr in range(self.rows + 1):
            if test_is_route(row + rr, column + self.columns + 1): return True

        # rangée en dessous du bât
        if test_is_route(row + self.rows + 1, column - 1): return True
        for cc in range(self.columns + 1):
            if test_is_route(row + self.rows + 1, column + cc): return True
        if test_is_route(row + self.rows + 1, column + 1): return True


    def set_tag(self, tag):
        pass

    def tag(self):
        return "tag{}".format(self.id)

    def draw(self, canvas, margin, x=None, y=None):
        # dessin d'un bâtiment
        size = Data['size']
        if x == None:
            x = margin + self.column * size
        if y == None:
            y = margin + self.row * size

        if self.is_terrain():
            color = Data['color_terrain']
        else:
            color = Data['colors'][self.type]

        # on trace le contour complet du bât
        rect = canvas.create_rectangle(x, y,
                                       x + self.columns * size,
                                       y + self.rows * size,
                                       width=1, outline="red", fill=color,
                                       tag=self.tag())

        # on accumule tous les éléments du dessin utilisés pour ce bât
        # ceci sere nécessaire pour effacer ou déplacer
        self.graphs = [rect]

        # on trace la grille de toutes les cases occupées par le bât
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

    def undraw(self, canvas):
        # pour effacer un bât il suffit d'effacer tous les graphs
        size = Data['size']
        margin = Data['margin']

        for obj in self.graphs:
            canvas.delete(obj)

        self.graphs = []

    def remove(self):
        # suppression du bât de la BdB
        if self.is_terrain():
            i = int(self.row/4) * Data['rows'] + int(self.column/4)
            Data['terrains_vrais'][i] = 0

        Data['batiments'].pop(self.id)


class Terrain(Batiment):
    def __init__(self):
        super().__init__("Terrain", 4, 4, "Terrain")


def draw_case_at(canvas, margin, row, column, line_color='black', fill_color=''):
    """
    dessine une case à la position (row, column)
    """
    size = Data['size']
    x1 = column * size + margin
    y1 = row * size + margin
    x2 = x1 + size
    y2 = y1 + size
    return canvas.create_rectangle(x1, y1, x2, y2, width=1, outline=line_color, fill=fill_color)


def draw_terrain_at(canvas, margin, row, column, line_color='black', fill_color=''):
    """
    dessine un terrain à la position (row, column)
    """
    size = Data['size']
    x1 = 4 * column * size + margin
    y1 = 4 * row * size + margin
    x2 = x1 + 4 * size
    y2 = y1 + 4 * size
    canvas.create_rectangle(x1, y1, x2, y2, width=1, outline=line_color, fill=fill_color)
    for r in range(4):
        for c in range(4):
            draw_case_at(canvas, margin, row * 4 + r, column * 4 + c, line_color=line_color)
    canvas.create_rectangle(x1, y1, x2, y2, width=1, outline="red")

"""
Plateau de jeu
"""
class Jeu(tk.Tk):
    def __init__(self):
        super().__init__()

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        self.title('ForgeOfEmpires')
        full_width = Data['rows'] * 4 * Data['size'] + 2 * Data['margin'] + 30
        full_height = Data['columns'] * 4 * Data['size'] + 2 * Data['margin'] + 30
        width = min(full_width, screen_width)
        height = min(full_height, screen_height)
        Data['geom_width'] = width
        Data['geom_height'] = height
        self.geometry("{}x{}".format(width, height))
        self.resizable(True, True)
        self.grid()
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=20)
        self.configure()

        self.batiment = None
        self.select_batiment = None
        self.moving = None
        self.moving_case = None
        self.essais_canvas = None

    def canvas_geometry(self):
        full_width = Data['geom_width']
        full_height = Data['geom_height']
        width = Data['geom_width'] - 30
        height = Data['geom_height'] - 200

        return width, height, full_width, full_height

    def up(self, r=None, c=None):
        """
        Click up
        """
        if self.batiment != None:
            # on est en train de déplacer un bâtiment
            objs = self.dessin.find_withtag(self.batiment.tag())
            # print("Moving2> tag=", self.batiment.tag(), "objs=", objs)
            for obj in objs:
                self.dessin.delete(obj)

            if r != None:
                # print("Install batiment> r=", r, "c=", c)
                self.batiment.install(r, c)

            self.batiment.draw(self.dessin, Data['margin'])

        # print("removing bat", n)
        self.batiment = None
        self.select_batiment = None
        # self.dessin.delete(self.moving)
        self.moving = None
        self.dessin.delete(self.moving_case)
        self.moving_case = None

    def open_essais(self):
        essais = tk.Toplevel(self)

        size = Data['size']

        essais_rows = Data['essais_rows']
        essais_columns = Data['essais_columns']

        height = 4 * essais_rows * size
        width = 4 * essais_columns * size

        essais.geometry("{}x{}".format(width + 30, height + 30))
        essais.title("Essais")

        self.essais_canvas = tk.Canvas(essais, bg="ivory", width=width + 20, height=height + 20)
        self.essais_canvas.pack()

        color = Data["color_terrain_vide"]
        line_color = Data["color_line"]

        for r in range(essais_rows):
            for c in range(essais_columns):
                draw_terrain_at(self.essais_canvas, 10, r, c, line_color=line_color, fill_color=color)

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

            if self.select_batiment != None:
                return
            elif self.batiment == None:
                result = get_case(x, y)

                if result == None: return
                r, c, tr, tc = result

                found = find_batiment(r, c)

                if found != None:
                    # print("moving...", found.id, found.nom)
                    self.combo_nom.set(found.nom)
                    self.combo_id.set(found.id)
                    self.combo_rows.set(found.rows)
                    self.combo_columns.set(found.columns)
                    self.combo_type.set(Data['types'][found.type])
                    self.combo_connected.set(Data['connection'][found.connected])
                    return

                self.combo_nom.set('')
                self.combo_id.set('')
                self.combo_rows.set('')
                self.combo_columns.set('')
                self.combo_type.set(Data['types'][0])
                self.combo_connected.set("non")

                return

            # animation sous la souris, anciennes valeurs
            global ex, ey

            if self.moving == None:
                self.moving = self.batiment.draw(self.dessin, Data['margin'], x, y)
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

            nonconnecte = Data['types'].index('Autre Non Connecté')

            if not self.batiment.is_terrain():
                # print("on positionne un batiment")
                tr_vrai, tc_vrai = get_terrain_vrai(tr, tc)
                if tr_vrai == None: return

                # on va tester les collisions avec des batiments existants
                for id in Data['batiments']:
                    b = Data['batiments'][id]
                    if b.is_terrain(): continue
                    if b.collision(self.batiment, r, c):
                        # print("collision entre ", b.id, b.nom, "et", self.batiment.id, self.batiment.nom)
                        return

                    if b.type != nonconnecte:
                        if not b.must_connect(r, c):
                            return

                # Mise en place d'un batiment normal
                if self.moving_case != None:
                    self.dessin.delete(self.moving_case)
                    self.moving_case = None

                self.moving_case = self.case(r, c, line_color='yellow')

                # print("action>", mode, "x=", x, "y=", y, "nom=", n, "r=", r, "c=", c, "tr=", tr, "tc=", tc)

                if mode == "up":
                    self.up(r, c)

            else:
                # print("on positionne un terrain")
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
                    """
                    Les contraintes de placements sont déjà validées
                    - r et c doivent multiples de 4
                    - r et c doivent se situer dans la zone des nouveaux terrains
                    - on ne peut placer un terrain que contre un terrain existant
                    Ensuite, on sa modifier la ligne de configuration
                    """

                    if self.moving_case != None:
                        self.dessin.delete(self.moving_case)

                    self.moving_case = self.case(r, c, line_color='yellow')

                    # print("action>", mode, "x=", x, "y=", y, "nom=", n, "r=", r, "c=", c, "tr=", tr, "tc=", tc)
                    if mode == "up":
                        self.up(r, c)

        def move(e):
            # print("Move")
            action("move", e)

        def button_up(e):
            # print("Button up")
            action("up", e)

        def leave(e):
            if self.select_batiment != None: return
            """
            self.combo_nom.set('')
            self.combo_id.set('')
            self.combo_rows.set('')
            self.combo_columns.set('')
            self.combo_type.set(Data['types'][0])
            self.combo_connected.set("non")
            """

        self.popup_event = None
        popup = tk.Menu(self, tearoff=0)

        # Adding Menu Items
        def command_move():
            x, y = scrolling(self.popup_event)
            result = get_case(x, y)
            if result == None: return
            r, c, tr, tc = result
            b = find_batiment(r, c)
            if not b.is_terrain():
                self.batiment = b
                b.row = None
                b.column = None
                b.undraw(self.dessin)
                b.remove()

        def command_copy():
            x, y = scrolling(self.popup_event)
            result = get_case(x, y)
            if result == None: return
            r, c, tr, tc = result
            b = find_batiment(r, c)
            if not b.is_terrain():
                b = Batiment(b.nom, b.rows, b.columns, Data['types'][b.type])
                self.batiment = b

        def command_change():
            x, y = scrolling(self.popup_event)
            result = get_case(x, y)
            if result == None: return
            r, c, tr, tc = result
            b = find_batiment(r, c)
            if not b.is_terrain():
                self.select_batiment = b
                self.combo_nom.set(b.nom)
                self.combo_id.set(b.id)
                self.combo_rows.set(b.rows)
                self.combo_columns.set(b.columns)
                self.combo_type.set(Data['types'][b.type])
                self.combo_connected.set(Data['connection'][b.connected])

        def command_pop():
            def find_pop_position(b):
                if len(Data['poped']) == 0: return (0, 0)
                for r in range(Data['essais_rows']*4):
                    if r + b.rows > Data['essais_rows']*4:
                        break

                    for c in range(Data['essais_columns']*4):
                        if c + b.columns > Data['essais_columns']*4:
                            break

                        # print("find_pop_position> test r,c:", "r=", r, "c=", c)
                        collision = False
                        for id in Data['poped']:
                            poped = Data['poped'][id]
                            # print("find_pop_position> test, id:", "r=", r, "c=", c, "id=", id, "nom=", poped.nom)
                            if not poped.collision(b, r, c):
                                # print("find_pop_position> pas de collision pour:", "r=", r, "c=", c, "id=", id, "nom=", poped.nom)
                                pass
                            else:
                                collision = True
                                break
                        if not collision:
                            return (r, c)

                return None

            if self.essais_canvas == None:
                self.open_essais()

            x, y = scrolling(self.popup_event)
            result = get_case(x, y)
            if result == None: return
            r, c, tr, tc = result
            b = find_batiment(r, c)
            if not b.is_terrain():
                # print("command_pop> id=", b.id)
                # b.row = None
                # b.column = None
                found = find_pop_position(b)
                if found != None:
                    r, c = found
                    # print("command_pop> il y a de la place", "r=", r, "c=", c)
                    b.row = r
                    b.column = c
                    Data['poped'][b.id] = b
                    b.undraw(self.dessin)
                    b.draw(self.essais_canvas, 10)
                    b.remove()

        def command_delete():
            x, y = scrolling(self.popup_event)
            result = get_case(x, y)
            if result == None: return
            r, c, tr, tc = result
            b = find_batiment(r, c)
            if b != None:
                self.batiment = None
                b.undraw(self.dessin)
                b.remove()
                # print("Remove batiment", b)
                b.row = None
                b.column = None
                Data['poped'][b.id] = b

        popup.add_command(label="Move", command=command_move)
        popup.add_command(label="Copy", command=command_copy)
        popup.add_command(label="Change", command=command_change)
        popup.add_command(label="Pop", command=command_pop)
        popup.add_command(label="Delete", command=command_delete)
        popup.add_separator()

        def menu_popup(event):
            # display the popup menu
            try:
                self.popup_event = event
                popup.tk_popup(event.x_root, event.y_root, 0)
                # print("Popup>", self.batiment, self.select_batiment)
            finally:
                # Release the grab
                popup.grab_release()

        self.dessin.bind("<Motion>", move)
        self.bind("<Button-3>", menu_popup)
        self.dessin.bind("<ButtonRelease>", button_up)
        self.dessin.bind("<Leave>", leave)

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
            n = self.combo_nom.get()
            try:
                r = int(self.combo_rows.get())
            except:
                r = 0
            try:
                c = int(self.combo_columns.get())
            except:
                c = 0

            t = self.combo_type.get()

            connected = self.combo_connected.get()

            if n != '' and r > 0 and c > 0:
                #print("install> ", "nom=", n, "rows=", r, "columns=", c)
                self.batiment = Batiment(n, r, c, t, connected)

        def install_terrain():
            self.up()
            n = "Terrain"
            r = 4
            c = 4

            # print("install> terrain")
            self.batiment = Terrain()

        def change_batiment():
            if self.select_batiment != None:
                b = self.select_batiment
                nom = self.combo_nom.get()
                # rows = self.combo_rows.get()
                # columns = self.combo_columns.get()
                type = self.combo_type.get()
                connected = self.combo_connected.get()
                b.nom = nom
                # b.rows = rows
                # b.columns = columns
                b.type = Data['types'].index(type)
                b.draw(self.dessin, Data['margin'])
            self.select_batiment = None
            self.batiment = None

        combo_frame = tk.Frame(self)
        combo_frame.grid(row=1, column=0)

        row = 0
        self.combo_nom = tk.StringVar()
        ttk.Label(combo_frame, text='Nom:').grid(column=0, row=row, sticky=tk.W)
        ttk.Entry(combo_frame, width=30, textvariable=self.combo_nom).grid(column=1, row=row, columnspan=3, sticky=tk.W)

        self.combo_id = tk.StringVar()
        ttk.Label(combo_frame, text='Id:').grid(column=4, row=row, sticky=tk.W)
        ttk.Entry(combo_frame, width=5, textvariable=self.combo_id).grid(column=5, row=row, sticky=tk.W)

        row += 1

        self.combo_rows = tk.StringVar()
        ttk.Label(combo_frame, text='rows:').grid(column=0, row=row, sticky=tk.W)
        ttk.Entry(combo_frame, width=8, textvariable=self.combo_rows).grid(column=1, row=row, sticky=tk.W)

        self.combo_columns = tk.StringVar()
        ttk.Label(combo_frame, text='columns:').grid(column=2, row=row, sticky=tk.W)
        ttk.Entry(combo_frame, width=8, textvariable=self.combo_columns).grid(column=3, row=row, sticky=tk.W)

        row += 1

        self.combo_type = tk.StringVar()
        ttk.Label(combo_frame, text='type:').grid(column=0, row=row, sticky=tk.W)
        combo = ttk.Combobox(combo_frame, textvariable=self.combo_type)
        combo['values'] = Data['types']
        combo['state'] = 'readonly'
        combo.current(newindex=0)
        combo.grid(column=1, row=row, sticky=tk.W)

        self.combo_connected = tk.StringVar()
        ttk.Label(combo_frame, text='connected:').grid(column=2, row=row, sticky=tk.W)
        combo = ttk.Combobox(combo_frame, textvariable=self.combo_connected)
        combo['values'] = ['Non', 'Oui']
        combo['state'] = 'readonly'
        combo.current(newindex=0)
        combo.grid(column=3, row=row, sticky=tk.W)

        row += 1

        ttk.Button(combo_frame, text="Terrain", command=install_terrain).grid(column=0, row=row, sticky=tk.W)
        ttk.Button(combo_frame, text="Install", command=install).grid(column=1, row=row, sticky=tk.W)
        ttk.Button(combo_frame, text="Change", command=change_batiment).grid(column=2, row=row, sticky=tk.W)
        # ttk.Button(combo_frame, text="Essais", command=self.open_essais).grid(column=3, row=row, sticky=tk.W)

    def configure_quit(self):
        quit_frame = tk.Frame(self)
        quit_frame.grid(row=2, column=0)

        def quit():
            """
            for id in Data['batiments']:
                print("bat[", id, "]=", Data['batiments'][id])
            """
            jeu.destroy()

        def save():
            with open('data.pickle', 'wb') as f:
                pickle.dump(Data, f, pickle.HIGHEST_PROTOCOL)

        row = 0
        ttk.Button(quit_frame, text="Quit", command=quit).grid(column=0, row=row, sticky=tk.W)
        ttk.Button(quit_frame, text="Save", command=save).grid(column=1, row=row, sticky=tk.W)

    def configure(self):
        ##----- Création des boutons -----##

        self.configure_canvas()
        self.configure_combo()
        self.configure_quit()

    def case(self, row, column, line_color='black', fill_color=''):
        margin = Data['margin']
        drawn = draw_case_at(self.dessin, margin, row, column, line_color=line_color, fill_color=fill_color)
        return drawn

    def terrain(self, row, column, line_color='black', fill_color=''):
        margin = Data['margin']
        draw_terrain_at(self.dessin, margin, row, column, line_color=line_color, fill_color=fill_color)

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
        # self.terrains()

        for id in Data['batiments']:
            b = Data['batiments'][id]
            if b.is_terrain():
                b.draw(self.dessin, Data['margin'])

        for id in Data['batiments']:
            b = Data['batiments'][id]
            if not b.is_terrain():
                b.draw(self.dessin, Data['margin'])

        self.dessin.addtag_all("all")

    def run(self):
        ##----- Programme principal -----##
        self.mainloop()  # Boucle d'attente des événements


if __name__ == '__main__':
    try:
        with open('data.pickle', 'rb') as f:
            Data = pickle.load(f)

        alltypes = []

        for id in Data['batiments']:
            b = Data['batiments'][id]

            print(b)

            """
            route = Data['types'].index('Route')
            if b.type == route or b.is_terrain():
                pass
            elif hasattr(b, "saved") and b.saved:
                # print("déjà configuré", b.nom, b.id, b.att_columns, b.att_rows, b.att_type)
                pass
            else:
                print(b)
                if b.attributs(b.nom):
                    b.saved = True
                    with open('data.pickle', 'wb') as f:
                        pickle.dump(Data, f, pickle.HIGHEST_PROTOCOL)
            """
        # print(alltypes)

        """
        Data['connection'] = ['non', 'oui']

        connected = Data['types'].index('Autre Connecté')
        notconnected = Data['types'].index('Autre Non Connecté')
        route = Data['types'].index('Route')
        hotel = Data['types'].index('Hotel de Ville')
        for id in Data['batiments']:
            b = Data['batiments'][id]
            if b.type == connected:
                b.connected = 1
            elif b.type == notconnected:
                b.connected = 0
            elif b.type == route:
                b.connected = 0
            elif b.type == hotel:
                b.connected = 0
            else:
                b.connected = 1

        for id in Data['batiments']:
            b = Data['batiments'][id]
            connecte = Data['types'].index('Autre Connecté')
            if b.rows == 1 and b.columns == 1 and b.type == connecte:
                b.type = Data['types'].index('Autre Non Connecté')

        Data['types'] = ['Habitation', 'Militaire', 'Production', 'Marchandise', 'Culture', 'Décoration', 'Route', 'GM',
                        'Hotel de Ville', 'Autre Connecté', 'Autre Non Connecté']
        Data['colors'] = ['cyan', 'orange', 'DodgerBlue2', 'yellow', 'snow', 'green2', 'gray50', 'hot pink', 'red',
                         'purple1', 'MediumPurple2',]
        Data['size'] = 16
        Data['margin'] = 30
        """

        """
        for id in Data:
            print(id)
        """
    except:
        pass

    # Data['colors'] = ['cyan', 'orange', 'DodgerBlue2', 'yellow', 'snow', 'green2', 'gray50', 'hot pink', 'red', 'purple1', ]

    jeu = Jeu()
    jeu.run()
    # jeu.draw_grid()

