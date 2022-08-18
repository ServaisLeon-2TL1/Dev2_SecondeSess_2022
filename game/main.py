
import game


def main():

    nombre_jouers = int(input("How many players ? "))

    if nombre_jouers < 2:
        print("Warning: Less than 2 players selected, setting to 2")
        nombre_jouers = 2
    elif nombre_jouers > 4:
        print("Warning: More than 4 players selected, setting to 4")
        nombre_jouers = 4

    puissance = int(input("Choisissez la puissance de la partie "))

    nombre_colonnes = int(input("Number of columns "))

    if nombre_colonnes < puissance:
        print(f"Warning: Columns amount is less than the power, setting to {puissance}")
        nombre_colonnes = puissance

    nombre_lines = int(input("Number of lines "))

    if nombre_lines < puissance:
        print(f"Warning: Lines amount is less than the power, setting to {puissance}")
        nombre_lines = puissance

    g = game.Game(nombre_jouers, puissance, nombre_colonnes, nombre_lines, True)
    while True:
        g.play_game()


if __name__ == "__main__":
    main()