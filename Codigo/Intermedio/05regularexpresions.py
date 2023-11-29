import re

man = open("mbox.txt")
maillist = []

for linea in man:
    linea = linea.strip()
#    if re.search("^From:", linea):
    if re.search("From:", linea):
        linea = linea.lstrip("From: ")
        maillist.append(linea)

print("La cantidad de correos es: ", len(maillist))
maillist = set(maillist)
maillist = list(maillist)

print(maillist, len(maillist))