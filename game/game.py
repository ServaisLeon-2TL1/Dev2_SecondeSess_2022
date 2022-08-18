
import terrain
import player
import leaderboard


class Game:

    SYMBOLS = ["O", "X", "U", "L"]
    DIRECTIONS = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

    def __init__(self, nombre_jouers = 2, puissance = 4, nombre_colonnes = 4, nombre_lines = 4, customize = False):
        self.lb = leaderboard.Leaderboard("lead.db")
        self.terrain = terrain.Terrain(nombre_colonnes, nombre_lines)
        self.puissance = puissance
        self.players = [player.Player(pid, Game.SYMBOLS[pid - 1],
            self.lb, customize) for pid in range(1, nombre_jouers + 1)]

    def printTerrain(self):
        """ Affiche le terrain de jeu
               PRE : preconditions de init doivent etre réspecté
               POST : affiche le terrain avec modification si il y en a
               """
        for i in range(self.terrain.CELLULES):
            if i % self.terrain.COLONNES == 0:
                print()
            pos = (i % self.terrain.COLONNES, i // self.terrain.COLONNES)
            if pos in self.terrain.occupied_positions:
                print("[" + self.terrain.occupied_positions[pos] + "]", end='')
            else:
                print('[ ]', end='')
        print()

    def play(self, player):
        """ Annonce au joueur qu'il peut jouer + permet au joueur de placer un pion
               PRE : player doit exister
               POST : Va placer le pion du joueur dans le terrain
               """
        col = int(input(player.pname + ", enter a column from 1 to {} : ".format(self.terrain.COLONNES))) - 1
        if not self.terrain.colonneValide(col):
            print("Invalid col.")
            return
        ligne = self.terrain.colonnePlusBasse(col)
        self.terrain.occupied_positions[(col, ligne)] = player.symbol

    def play_game(self):
        """ Lance la partie en utilisans les méthodes de la classe
               PRE :preconditions de init doivent etre réspecté
               POST :Va boucler et activer les méthodes pour faire fonctionner la partie
               """
        for p in self.players:
            self.play(p)
            self.printTerrain()
            w = self.check_winner(p.symbol)
            if (w):
                print(p.pname + " has won !")
                p.win(self.lb)
                for l in self.players:
                    if (l.pname != p.pname):
                        self.lb.add_result(l.pname, 0, 1)
                self.lb.printlb()
                self.terrain.reset()
                return True

    def check_winner(self, stein = SYMBOLS[0]):
        """ Va vérifier apres chaque tour si il y a un gagnant
                PRE : stein doit etre un symbol existant et qui a aligner la puissance correct
                POST : Va soit stopper la partie si il y a un gagnant ou laisser continuer si personne ne gagne
                """
        for pos in self.terrain.occupied_positions:
            for direction in Game.DIRECTIONS:
                quatre_dans_une_ligne = True
                for i in range(self.puissance):
                    colonne, ligne = pos
                    delta_colonne, delte_ligne = direction
                    p1 = (colonne + delta_colonne * i, ligne + delte_ligne * i)
                    if p1 in self.terrain.occupied_positions and self.terrain.occupied_positions[p1] == stein:
                        continue
                    quatre_dans_une_ligne = False
                    break
                if quatre_dans_une_ligne:
                    return True