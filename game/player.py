
class Player():

    def __init__(self, player_id, default_symbol, customize = False):
        self.pname = f"p{player_id}"
        self.symbol = default_symbol

        if customize:
            self.pname = input(f"Enter name of player {str(player_id)} : ")
            ssym = input("Change symbol (" + self.symbol + ")? (enter to leave as-is)")
            if ssym:
                self.symbol = ssym[0]

    def win(self, db):
        db.add_result(self.pname, 1, 0)