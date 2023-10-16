""" Base code for starting a Flet App.
    with Python.
"""
import flet as ft 

def main(page: ft.Page):
    page.controls.append( ft.Text(value="Este es un texto de entrada",color=ft.colors.DEEP_ORANGE, size=18, weight=ft.FontWeight.W_900))
    page.update()

ft.app(target=main)