 #Crea una función que reciba días, horas, minutos y segundos (como enteros) y retorne su resultado en milisegundos.
 
def Convertir_A_Milisegundos(dias,horas,minutos,segundos):
        dias= dias*24*60*60*1000
        horas = horas*60*60*1000
        minutos = minutos*60*1000
        segundos = segundos*1000
        
        return int(dias+horas+minutos+segundos)

print("Los milisegundos son: ", Convertir_A_Milisegundos(1,0,0,0))
