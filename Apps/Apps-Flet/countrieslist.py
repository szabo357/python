import flet as ft
import countriesdata as cd
world = cd.World.countries

def main(page: ft.Page):
    page.title = "Flet countries List"
    page.padding = 50
    page.theme_mode = ft.ThemeMode.LIGHT
    page.update()
   # page.vertical_alignment=ft.MainAxisAlignment.CENTER
    # Agregando elementos a la pagina.
    img = ft.Image(
        src=f"https://restcountries.eu/data/afg.svg",
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN,
    )
    images = ft.Row(expand=1,wrap=False,scroll="always")
    flags = ft.Row(expand=1,wrap=False,scroll="always")
    page.add(img,images,flags)

    for country in world[:30]:
        images.controls.append(
            ft.Image(
                src= country["flag"],
                width=200,
                height=200,
                fit=ft.ImageFit.NONE,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(10)
            )    
        )
        flags.controls.append(
            ft.Text(
                value=country["flag"],
                height=200,
                bgcolor="blue",
                selectable=True
            )
        )
    page.update()

ft.app(target=main)
#ft.app(target=main,view=ft.AppView.WEB_BROWSER)