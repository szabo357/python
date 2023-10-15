'''En este ejemplo se agrega un control de Texto a la pagina que es almacenado en la variable "t".
   luego se crea una lista llamada "color" que almacena 10 colores predefinidos de Flet.
   Se itera todos los colores de la lista y se actualiza el color y valor del texto en cada iteracion.
'''
import time
import flet as ft 

def main(page: ft.Page):
    t = ft.Text(size=60)

    color = [ft.colors.AMBER,
             ft.colors.BLACK,
             ft.colors.BLUE,
             ft.colors.BLUE_GREY,
             ft.colors.BROWN,
             ft.colors.CYAN,
             ft.colors.DEEP_ORANGE,
             ft.colors.DEEP_PURPLE,
             ft.colors.ERROR,
             ft.colors.GREEN
            ]
    
    page.add(t) # it's a shortcut for page.controls.append(t) and then page.update()

    for i in range(len(color)): 
        t.color = color[i]
        t.value = f"Step {i}"
        page.update()
        time.sleep(1)

ft.app(target=main)