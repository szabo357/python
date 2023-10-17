import flet as ft
import random
import time

def main(page: ft.Page):

    def contenedores(count):
        items= []
        for _  in range(count):
            items.append(    
                ft.Container(
                    content=ft.Text( value=random.randint(1,200)),
                    alignment=ft.alignment.center,
                    width=50,
                    height=50,
                    bgcolor=ft.colors.ORANGE,
                    border_radius=25,
                )
            )
        return items

    def OrdenamientoBurbuja(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1 ):
                arr[j].bgcolor=ft.colors.YELLOW
                arr[j + 1].bgcolor=ft.colors.YELLOW
                time.sleep(2)
                page.update()
                if arr[j].content.value > arr[j + 1].content.value :
                    arr[j] , arr[j + 1] = arr[j + 1] , arr[j]    
                arr[j].bgcolor=ft.colors.ORANGE
                arr[j + 1].bgcolor=ft.colors.ORANGE
            arr[n-i-1].bgcolor=ft.colors.GREEN
        page.update()

    def reiniciar_click(e,value):
        value.clean()
        value = contenedores(10)
        page.update()

    def iniciar_click(e,value):
        OrdenamientoBurbuja(value)
        page.update()

    page.add(ft.Text("Algoritmo de Ordenamiento de Burbujas", size=16, weight=ft.FontWeight.BOLD,font_family="Roboto"))
    page.add(ft.Divider(thickness=5,color=ft.colors.BLUE))

    pelotas = contenedores(10)
    fila_lista = ft.Row(pelotas)
    
    page.add(fila_lista)
    page.add(
        ft.Row(
            [
            ft.ElevatedButton("Iniciar Ordenamiento",on_click=iniciar_click(pelotas)),
            ft.ElevatedButton("Reiniciar Ordenamiento",on_click=reiniciar_click(fila_lista))
            ]
        ),
    )

ft.app(target=main)