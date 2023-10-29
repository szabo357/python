import random

def create_house()->(list,list):
 
    house = [list(["⬜️"]*4) for _ in range(4)]

    if random.choice([True,False]):
        # columnas perimetro
        door = [ random.randint(0,3)  , random.choice([0,3])]
    else:
        # filas perimetro
        door = [ random.choice([0,3]) , random.randint(0,3)]

    house[door[0]][door[1]] = "🚪"

    for row in house:
        print("".join(map(str,row)))

    return house, door

house,door = create_house()

position = door
print(f"Posición inicial: {position}")