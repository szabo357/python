import os
import flet as ft

os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000"

def my_app(page: ft.Page):
    #r = ft.Row(wrap=True, scroll="always",expand=True)
    #page.add(r)
    gv = ft.GridView(expand=True, max_extent=150, child_aspect_ratio=1)
    page.add(gv)
    for i in range(5000):
        gv.controls.append(
            ft.Container(
                ft.Text(f"Item {i}"),
                alignment=ft.alignment.center,
                bgcolor=ft.colors.AMBER_100,
                border=ft.border.all(1, ft.colors.AMBER_400),
                border_radius=ft.border_radius.all(5),
            )
        )
        # send batch update to improve usability.Update page every 500 items are loaded.
        if i % 500 == 0:
            page.update()

    page.update()

"""     for i in range(5000):
        r.controls.append(
            ft.Container(
                ft.Text(f"Item {i}"),
                width=100,
                height=100,
                alignment=ft.alignment.center,
                bgcolor=ft.colors.AMBER_200,
                border=ft.border.all(1,ft.colors.AMBER_500),
                border_radius=ft.border_radius.all(10),
            )
        ) """
#ft.app(target=my_app)    
ft.app(target=my_app,view=ft.AppView.WEB_BROWSER)