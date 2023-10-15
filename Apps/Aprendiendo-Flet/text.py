import time
import flet as ft

def main(page: ft.Page):

    t = ft.Text(value="Hola Mundo!",size=60, color=ft.colors.CYAN,font_family="Roboto", 
                weight=ft.FontWeight.BOLD,bgcolor=ft.colors.LIME_100
                )
    
    
    page.add(t)
    page.update()

ft.app(target=main)