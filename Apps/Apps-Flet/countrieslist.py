import flet as ft
import countriesdata as cd
world = cd.World.countries
flg = cd.World.flags

def main(page: ft.Page):
    page.title = "Flet countries List"
    page.padding = 50
    page.theme_mode = ft.ThemeMode.LIGHT
    page.update()
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    # definiendo contenedores
    # Agregando elementos a la pagina.
    images = ft.Row(expand=1,wrap=False,scroll="always")
    countries = ft.Row(expand=1,wrap=False,scroll="always")
    page.add(images,countries)
    honduras ="https://cdn.jsdelivr.net/gh/hampusborgos/country-flags@main/svg/hn.svg"
    mycontainer =ft.Row([ ft.Column(
        controls=[
            ft.Image(
                src=honduras,
                width=200,
                height=100,
                fit=ft.ImageFit.CONTAIN,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(10)
            ),
            ft.Text(value="Honduras",height=20,weight="Bold")
        ],width=200, height=200,
     )])

    for country in flg[:30]:
        images.controls.append(
            ft.Image(
                src=country["flag"],
                width=200,
                height=200,
                fit=ft.ImageFit.CONTAIN,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(10)
            )
        )
    countries.controls.append(ft.Text(value=country["country"],height=20,weight="Bold"))
    
    page.update()

    page.add(mycontainer)
    page.update()

ft.app(target=main)
#ft.app(target=main,view=ft.AppView.WEB_BROWSER)