
import colonie


#
# bhavan, ruelle, rizière, basmati, canal, roupie, atelier de saris, shanti ghars, chatri, marchand d'épices
# épice, baldaquin, sari, femre de lotus, lotus, tchaharbach, haveli
#

class Bhavan(colonie.Habitat):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.dx = 2
        self.dy = 2


class Ruelle(colonie.Diplomatie):
    def __init__(self, jeu: colonie.Jeu, x: int, y: int):
        super().__init__(x, y)
        self.dx = 3
        self.dy = 2
        jeu.add_diplomatie(24)


if __name__ == '__main__':
    ruelles = []
    jeu = colonie.Jeu()
    ambassade = colonie.Ambassade(x=11, y=8)
    ambassade.install(jeu.grille)
    for x in range(7):
        for y in range(7):
            if (x, y) in [(0,5), (0,6), (1, 6), (5,6), (6,5), (6, 6)]:
                continue
            jeu.add_terrain(x*4, y*4)

    ruelles.append(Ruelle(jeu=jeu, x=8, y=8))
    ruelles.append(Ruelle(jeu=jeu, x=8, y=10))
    ruelles.append(Ruelle(jeu=jeu, x=8, y=12))
    ruelles.append(Ruelle(jeu=jeu, x=8, y=14))
    ruelles.append(Ruelle(jeu=jeu, x=8, y=16))

    print(jeu.diplomatie)


