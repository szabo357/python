
def sortlist(args,order="Asc"):
    xlist =[]
    lcopy = args
    maximum = 0

    if order == "Asc":
        for arg in args:
            maximum = 0
            for litem in lcopy:
                if litem > maximum:
                    maximum = litem
            xlist.append(maximum)
        return xlist
    elif order == "Desc":    
        xlist = [1]
    



mylist = [20,4,10,5,8,15]

print(sortlist(mylist,"Asc"))