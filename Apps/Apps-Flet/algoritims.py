import flet as ft
import random
import time

def main(page: ft.Page):
    page.title = "Algoritmo de ordenamiento"
    page.bgcolor = ft.colors.BLUE_100

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

    def ordenamiento_burbuja(arr):
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

    def ordenamiento_seleccion(arr):
        n = len(arr)
        for i in range( n - 1):
            menor = i
            for j in range(i + 1, n):
                if arr[j].content.value < arr[menor].content.value:
                    menor = j
                    time.sleep(2)
                    arr[menor].bgcolor = ft.colors.YELLOW
                    page.update()
            if menor != i:
                arr[menor], arr[i] = (arr[i], arr[menor])
                arr[menor].bgcolor = ft.colors.ORANGE
                time.sleep(2)
                page.update()
            time.sleep(2)
            arr[i].bgcolor = ft.colors.GREEN
            page.update()
        time.sleep(2)
        arr[j].bgcolor = ft.colors.GREEN
        page.update()
            


    def list_size_change(e):
        #list_size.value = list_size.value
        fila_lista.clean()
        pelotas = contenedores(int(list_size.value))
        fila_lista.controls = pelotas 
        page.update()

    def algoritmos_change(e):
        titulo.value = "Algoritmo de ordenamiento: "  + algoritmos.value
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
        pelotas = contenedores(int(list_size.value))
        fila_lista.controls = pelotas 
        page.update()

    def iniciar_click(e):
        pelotas = fila_lista.controls
        # if para elegir algoritmo de ordenamiento
        if algoritmos.value == "Bubble Sort":
            ordenamiento_burbuja(pelotas)
        elif algoritmos.value == "Selection Sort":
            ordenamiento_seleccion(pelotas)
        page.update()

    def dropdown_change(e):
        if dd_bgcolor.value == "Blue":
            page.bgcolor = ft.colors.BLUE_100
        elif dd_bgcolor.value == "Green":
            page.bgcolor = ft.colors.GREEN_100
        elif dd_bgcolor.value == "Purple":
            page.bgcolor = ft.colors.PURPLE_100
        elif dd_bgcolor.value == "Orange":
            page.bgcolor = ft.colors.ORANGE_100            
        elif dd_bgcolor.value == "Amber":
            page.bgcolor = ft.colors.AMBER_100
        page.update()
    
    algoritmos = ft.Dropdown(
        label= "Algoritmo de Ordenamiento: ",
        on_change= algoritmos_change,
        options= [
            ft.dropdown.Option("Bubble Sort"),
            ft.dropdown.Option("Selection Sort"),
            ft.dropdown.Option("Quick Sort"),
            ft.dropdown.Option("Double Sort"),
            ft.dropdown.Option("Merge Sort"),
            ft.dropdown.Option("Insertion Sort"),
        ],
        width=200,
        value="Bubble Sort"
    )    

    dd_bgcolor = ft.Dropdown(
        on_change=dropdown_change,
        options=[
            ft.dropdown.Option("Blue"),
            ft.dropdown.Option("Green"),
            ft.dropdown.Option("Purple"),
            ft.dropdown.Option("Orange"),
            ft.dropdown.Option("Amber"),
        ],
        value = "Blue",
        width=200,
    )
    
    titulo =ft.Text(
            value = "Algoritmo de ordenamiento: "+ algoritmos.value , 
            weight=ft.FontWeight.BOLD,
            font_family="Roboto",
            style=ft.TextThemeStyle.HEADLINE_MEDIUM
          )
    
    page.add(ft.Row([ titulo],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Divider(thickness=5,color=ft.colors.BLUE),
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
        ft.Row([ algoritmos, dd_bgcolor, list_size], ft.MainAxisAlignment.CENTER)
    )

ft.app(target=main)