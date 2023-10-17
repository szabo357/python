import flet as ft
import random
import time

def main(page: ft.Page):
    page.title = "Algoritmos"
    page.add(ft.Row(
               [ ft.Text(
                    value="Algoritmo de Ordenamiento de Burbujas", 
                    weight=ft.FontWeight.BOLD,
                    font_family="Roboto",
                    style=ft.TextThemeStyle.HEADLINE_MEDIUM
                 ),
               ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Divider(thickness=5,color=ft.colors.BLUE),
    )

    def contenedores(count):
        items= []
        for _  in range(count):
            items.append(    
                ft.Container(
                    content=ft.Text( value=random.randint(1,200),
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        font_family="Roboto"
                    ),
                    alignment=ft.alignment.center,
                    width=80,
                    height=80,
                    bgcolor=ft.colors.ORANGE,
                    border_radius=40,
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

    def list_size_change(e):
        #list_size.value = list_size.value
        fila_lista.clean()
        pelotas = contenedores(int(list_size.value))
        fila_lista.controls = pelotas 
        page.update()

    list_size = ft.Dropdown(
        on_change=list_size_change,
        
        options=[
            ft.dropdown.Option("6"),
            ft.dropdown.Option("8"),
            ft.dropdown.Option("10"),
            ft.dropdown.Option("12"),
            ft.dropdown.Option("14"),
        ],
        width=200,
        value="6"
    )

    pelotas = contenedores(int(list_size.value))
    fila_lista = ft.Row(pelotas,alignment=ft.MainAxisAlignment.CENTER)

    def reiniciar_click(e):
        fila_lista.clean()
        pelotas = contenedores(list_size.value)
        fila_lista.controls = pelotas 
        page.update()

    def iniciar_click(e):
        pelotas = fila_lista.controls
        OrdenamientoBurbuja(pelotas)
        page.update()

    def dropdown_change(e):
        page.bgcolor= dd_bgcolor.value
        page.update()
    
    dd_bgcolor = ft.Dropdown(
        on_change=dropdown_change,
        options=[
            ft.dropdown.Option("Blue"),
            ft.dropdown.Option("Green"),
            ft.dropdown.Option("Purple"),
            ft.dropdown.Option("Orange"),
            ft.dropdown.Option("Amber"),
        ],
        width=200,
    )

    page.add(fila_lista,
        ft.Divider(thickness=5,color=ft.colors.BLUE),
        ft.Row(
            [
            ft.ElevatedButton("Iniciar Ordenamiento",on_click=iniciar_click),
            ft.ElevatedButton("Reiniciar Ordenamiento",on_click=reiniciar_click)
            ]
        ,alignment= ft.MainAxisAlignment.CENTER
        ),
        ft.Row([dd_bgcolor,list_size], ft.MainAxisAlignment.CENTER)
    )

ft.app(target=main)