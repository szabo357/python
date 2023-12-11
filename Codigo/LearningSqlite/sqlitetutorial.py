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

# close connection to make sure db has been written to disk.
con.close()

new_con = sqlite3.connect("tutorial.db")
new_cur = new_con.cursor()
res = new_cur.execute("SELECT title, year FROM movie ORDER BY score DESC")
title, year = res.fetchone()
print(f'The highest scoring Monty Python movie is {title!r}, released in {year}')


chdir(savedpath)