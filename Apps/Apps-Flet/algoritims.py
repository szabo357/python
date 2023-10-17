import flet as ft
import random
import time

def main(page: ft.Page):
    
    def balls(count):
        items= []
        for _  in range(count):
            items.append(    
                ft.Container(
                    content=ft.Text( value=str(random.randint(1,200))),
                    alignment=ft.alignment.center,
                    width=50,
                    height=50,
                    bgcolor=ft.colors.ORANGE,
                    border_radius=25,
                )
            )
        return items
    
    pelotas = balls(10)

    page.add(ft.Row(pelotas))
    n = len(pelotas)

    for i in range(n):
        for j in range(0, n-i-1):
            pelotas[j].bgcolor=ft.colors.YELLOW
            pelotas[j + 1].bgcolor=ft.colors.YELLOW
            time.sleep(2)
            page.update()
            if pelotas[j].content.value > pelotas[j + 1].content.value:
                pelotas[j] , pelotas[j + 1] = pelotas[j + 1] , pelotas[j]    
            pelotas[j].bgcolor=ft.colors.ORANGE
            pelotas[j + 1].bgcolor=ft.colors.ORANGE
        pelotas[n-i-1].bgcolor=ft.colors.GREEN
    page.update()


ft.app(target=main)