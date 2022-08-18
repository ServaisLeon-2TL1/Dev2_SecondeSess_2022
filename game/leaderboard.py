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