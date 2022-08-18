import sqlite3


class Leaderboard():
    def __init__(self, sqwfile):
        self.sqdb = sqlite3.connect(sqwfile, check_same_thread=False)
        self.c = self.sqdb.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS lboard (name PRIMARY KEY,wins int,lose int)''')

    def add_result(self, pname, win, loss):
        k = self.c.execute('''SELECT * FROM lboard WHERE name = ?''', (pname,))
        try:
            ft = k.fetchone()

            w = ft[1]
            l = ft[2]
        except:
            print("")
            w = 0
            l = 0

        w += win
        l += loss

        try:
            k = self.c.execute('''INSERT OR REPLACE INTO lboard VALUES (?,?,?)''', (pname, w, l))
            self.sqdb.commit()
        except:
            print("Database error, could not update value")

    def printlb(self):
        try:
            k = self.c.execute('''SELECT * FROM lboard ORDER BY wins DESC''')
            print("Leaderboard\n--------------------\nName\t\tWins\tLoss")
            pter = k.fetchall()
            for p in pter:
                print(p[0] + "\t\t" + str(p[1]) + "\t" + str(p[2]))

        except:
            print("Database error, could not update value")


lb = Leaderboard("lead.db")
symbols = ("O", "X", "U", "L")


class Terrain():
    def __init__(self):
        self.players = []
        self.terrain = {}  # Key =(colonne, ligne), Valeur 'O' ou 'X'
        self.NOMBREJOUEUR = int(input("How many players ?"))

        if (self.NOMBREJOUEUR > 4):
            print("Warning: More than 4 players selected, limiting to 4")
            self.NOMBREJOUEUR = 4
        for a in range(0, self.NOMBREJOUEUR): self.players.append(Player(len(self.players) + 1))

        self.NOMBREPUISSANCE = int(input("Choisissez la puissance de la partie."))
        self.COLONNES = int(input("Number of columns"))
        self.LIGNES = int(input("Number of lines "))
        self.CELLULES = self.COLONNES * self.LIGNES
        self.DIRECTIONS = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

    def colonneValide(self, colonne):
        if (colonne, 0) in self.terrain:
            return False
        if colonne >= 0 and colonne < self.COLONNES:
            return True

    def colonnePlusBasse(self, colonne):
        for ligne in reversed(range(self.LIGNES)):
            if (colonne, ligne) not in self.terrain:
                return ligne

    def printTerrain(self):
        for i in range(self.CELLULES):
            if i % self.COLONNES == 0:
                print()
            pos = (i % self.COLONNES, i // self.COLONNES)
            if pos in self.terrain:
                print("[" + self.terrain[pos] + "]", end='')
            else:
                print('[ ]', end='')
        print()

    def reset(self):
        self.terrain = {}

    def play(self, player):
        col = int(input(player.pname + ", enter a column from 1 to {} : ".format(self.COLONNES))) - 1
        if not self.colonneValide(col):
            print("Invalid col.")
            return
        ligne = self.colonnePlusBasse(col)
        self.terrain[(col, ligne)] = player.symbol

    def play_game(self):
        for p in self.players:
            self.play(p)
            self.printTerrain()
            w = self.check_winner(p.symbol)
            if (w):
                p.win()
                for l in self.players:
                    if (l.pname != p.pname): lb.add_result(l.pname, 0, 1)
                lb.printlb()
                self.reset()
                return True

    def check_winner(self, stein):
        for pos in self.terrain:
            for direction in self.DIRECTIONS:
                quatre_dans_une_ligne = True
                for i in range(self.NOMBREPUISSANCE):
                    colonne, ligne = pos
                    delta_colonne, delte_ligne = direction
                    p1 = (colonne + delta_colonne * i, ligne + delte_ligne * i)
                    if p1 in self.terrain and self.terrain[p1] == stein: continue
                    quatre_dans_une_ligne = False
                    break
                if quatre_dans_une_ligne:
                    return True


class Player():
    def __init__(self, player_id):
        self.pname = input("Enter name of player " + str(player_id))
        self.symbol = symbols[player_id - 1]
        ssym = input("Change symbol (" + self.symbol + ")? (enter to leave as-is)")
        if (len(ssym) > 1): self.symbol = ssym[0]

    def win(self):
        print(self.pname + " has won ! ")
        lb.add_result(self.pname, 1, 0)


if __name__ == "__main__":
    t = Terrain()
    while True:
        t.play_game()