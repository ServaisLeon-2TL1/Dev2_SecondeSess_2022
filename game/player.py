
class Player():

    def __init__(self, player_id, default_symbol, dbobj, customize = False):
        """ Créé un joueur sur base du player_id , et du symbol
                 PRE : L'id doit etre un nombre et ne doit pas etre le meme qu'un autre joueur, le symbol doit éxister
                 POST : Instancie les valeurs pname et symbol au player
              """
        self.pname = f"p{player_id}"
        self.symbol = default_symbol

        if customize:
            self.pname = input(f"Enter name of player {str(player_id)} : ")
            while dbobj.name_exists(self.pname):
                self.pname = input(f"{self.pname} already exists. Enter another name for player {str(player_id)} : ")
            dbobj.add_result(self.pname, 0, 0)
            ssym = input("Change symbol (" + self.symbol + ")? (enter to leave as-is)")
            if ssym:
                self.symbol = ssym[0]

    def win(self, db):
        """ Va inscrire dans la db que le joueur a gagné
                  PRE : la db doit exister
                  POST : inscris le nom du joueur et rajoute une victoire dans la db
               """
        db.add_result(self.pname, 1, 0)