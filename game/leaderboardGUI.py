import tkinter as tk
from tkinter import ttk
import sqlite3

def showGUI():
    conn=sqlite3.connect('lead.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM lboard''')

    tempList = c.fetchall()
    tempList.sort(key=lambda e: e[1], reverse=True)
    for item in tempList:
        listBox.insert("", 100, text="line1", values=item)


scores = tk.Tk()
label = tk.Label(scores, text="Leaderboard de puissance 4", font=("Arial",30)).grid(row=0, columnspan=3)

cols = ('Name', 'Wins', 'Loses')
listBox = ttk.Treeview(scores, columns=cols, show='headings')

for col in cols:
    listBox.heading(col, text=col)
listBox.grid(row=1, column=0, columnspan=2)

showScores = tk.Button(scores, text="Show scores", width=15, command=show).grid(row=4, column=0)
closeButton = tk.Button(scores, text="Close", width=15, command=exit).grid(row=4, column=1)

scores.mainloop()