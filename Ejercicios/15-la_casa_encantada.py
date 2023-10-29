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

    def generate_candy(door:list)->list:
        candy = [random.randint(0,3),random.randint(0,3)]
        if candy[0] == door[0] and candy[1] == door[1]:
            return generate_candy(door)
        return candy
    
    candy = generate_candy(door)

    house[candy[0]][candy[1]] = "🍭"

    for row in house:
        print("".join(map(str,row)))

    return house, door

def move(position: list)->list:
    row, col = position[0], position[1]

    movements = "N S E O"

    if row == 0: movements = movements.replace("N ","")
    if row == 3: movements = movements.replace("S ","")
    if row == 0: movements = movements.replace("O ","")
    if row == 3: movements = movements.replace("E ","")

    movement = input(f"¿Hacia dónde te quieres desplazar [ {movements}]?: ").upper()

    if movement in movements:
        if movement == "N": position =   [ row-1, col]
        elif movement == "S": position = [ row+1, col]
        elif movement == "E": position = [ row, col+1]
        elif movement == "O": position = [ row, col-1]

        return position 
    else:
        print("Desplazamiento incorrecto. Selecciona una de las opciones validas.")
        return move(position)



house,door = create_house()

position = door
print(f"Posición inicial: {position}")