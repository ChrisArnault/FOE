import requests
import re
import chardet

def find(title):
    recherche = "https://fr.wiki.forgeofempires.com/index.php?title=Sp%C3%A9cial:Recherche&search="
    # Tour+de+la+victoire

    r = recherche + title.replace(" ", "+")
    # print("r=", r)
    response = requests.get(r)
    s = str(response.content)

    tag1 = "Correspondances dans les titres des pages"
    tag2 = "Correspondances dans le texte des pages"
    try:
        i1 = s.index(tag1)
    except:
        return None
    i2 = s.index(tag2)
    if i1 < i2:
        s = s[i1:]
        # print("{", s[0:100], "}")

        k = 1
        tag = 'title="' + title
        s = s[len(tag):]
        while True:
            i1 = s.index(tag)
            if i1 < 0: break
            i2 = s.index(tag2)
            if i2 < i1: break
            # print(k, i1, "{", s[i1:i1 + 100], "}")
            s = s[i1:]
            f = s[7:100]
            quote = f.index('"')
            # print("trouvé: [{}]".format(f[:quote]))
            # f[:quote])
            return f[:quote]
            k += 1
            s = s[len(tag):]

    return found


class Batiment(object):
    def __init__(self, name):
        self.name = name
        self.rue = None
        self.size = None
        self.attributs(name)

    def attributs(self, title):
        def rue(s):
            i = s.index("Rue:")
            s = s[i:]
            j = None
            try:
                j = s.index("Aucune rue requise")
                self.rue = None
            except:
                i = s.index("</div>")
                s = s[i + 6:i + 20]
                i = s.index("\n")
                m = re.match("(\d+).(\d+)", s[:i].strip())
                self.rue = m.group(1)

        def taille(s):
            i = s.index("Taille:")
            s = s[i:]
            i = s.index("</div>")
            s = s[i + 6:]
            i = s.index("\n")
            m = re.match("(\d+).(\d+)", s[:i].strip())
            self.columns = m.group(1)
            self.rows = m.group(2)

        def type(s):
            i = s.index("Type:")
            s = s[i:]
            i = s.index("</div>")
            s = s[i + 6:]
            i = s.index("\n")
            t = s[:i].strip()
            print("type:", t)
            self.type = t

        t = find(title)
        if t is not None: title = t

        prefix = "https://fr.wiki.forgeofempires.com/index.php?title="

        response = requests.get(prefix + title)
        cd = chardet.detect(response.content)
        ttt = response.content.decode('utf-8')
        s = str(response.content)
        rue(ttt)
        taille(ttt)
        type(ttt)
        print("name='{}' rue='{}' RxC='{}x{}'".format(self.name, self.rue, self.rows, self.columns))


# The API endpoint
titles = ["Place échec et mat",
          "Cap Canaveral",
          "Tour de la victoire",
          "Sanctuaire du savoir",
          "Le Kraken",
          "Forgeron",
          "Yggdrasil",
          "Laboratoire C.R.A.B."]

for t in titles:
    b = Batiment(t)



