import flet as ft

def my_app(page: ft.Page):
    page.bgcolor="blue"

    lv = ft.ListView(expand=True, spacing=10)
    
    for i in range(5000):
        lv.controls.append(ft.Text(f"Line {i}"))
    page.add(lv)

ft.app(target=my_app,view=ft.AppView.WEB_BROWSER)
