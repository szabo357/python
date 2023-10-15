import flet as ft
  

def main(page: ft.Page):
    t = ft.Text(value="Hello-Flet !",size=60,color=ft.colors.CYAN_400)
    page.add(t)


ft.app(main)