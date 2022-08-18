
class Terrain():

    def __init__(self, nombre_colonnes = 4, nombre_lines = 4):
        self.occupied_positions = {}
        self.COLONNES = nombre_colonnes
        self.LIGNES = nombre_lines
        self.CELLULES = self.COLONNES * self.LIGNES

    def colonneValide(self, colonne):
        if (colonne, 0) in self.occupied_positions:
            return False
        if colonne >= 0 and colonne < self.COLONNES:
            return True

    def colonnePlusBasse(self, colonne):
        for ligne in reversed(range(self.LIGNES)):
            if (colonne, ligne) not in self.occupied_positions:
                return ligne

    def reset(self):

        self.occupied_positions = {}