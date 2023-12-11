from os import chdir, getcwd
import sqlite3

savedpath = getcwd()
workingpath = r"C:\Users\jmsa3\Documents\Curso Python\python\Codigo\LearningSqlite"
chdir(workingpath)

con = sqlite3.connect("tutorial.db")
cur = con.cursor()

#cur.execute("CREATE TABLE movie(title, year, score)")

res = cur.execute("SELECT name FROM sqlite_master")
print(res.fetchall())

# cur.execute("""
#         INSERT INTO movie VALUES
#             ('Monty Python and the Holy Grail',1975,8.2),
#             ('And Now for Something Completely Different', 1971, 7.5)
#             """)
# con.commit()

res = cur.execute("SELECT score FROM movie")
print(res.fetchall())


# data = [
#     ("Monty Python Live at Hollywood Bowl", 1982, 7.9),
#     ("Monty Python's The meaning of Life", 1983, 7.5),
#     ("Monty Python's Life of Brian", 1979, 8.0),
# ]
# cur.executemany("Insert INTO movie VALUES(?, ?, ?)", data)
# con.commit()

query = "SELECT year, title FROM movie ORDER BY year"
for row in cur.execute(query):
    print(row)



chdir(savedpath)