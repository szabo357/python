import flet as ft
import countriesdata as cd
world = cd.World.countries
flg = cd.World.flags

# def main(page: ft.Page):
#     page.title = "Flet countries List"
#     page.padding = 50
#     page.height = 500
#     page.width = 800
#     page.theme_mode = ft.ThemeMode.LIGHT
#     page.vertical_alignment=ft.MainAxisAlignment.CENTER
#     page.bgcolor= ft.colors.INDIGO_100
    
#     def check_item_clicked(e):
#         e.control.checked = not e.control.checked
    
#     page.update()

#     page.appbar = ft.AppBar(
#         leading=ft.Icon(ft.icons.PALETTE),
#         leading_width=40,
#         title=ft.Text("AppBar Example"),
#         center_title=False,
#         bgcolor=ft.colors.SURFACE_VARIANT,
#         actions=[
#             ft.IconButton(ft.icons.WB_SUNNY_OUTLINED),
#             ft.IconButton(ft.icons.FILTER_3),
#             ft.PopupMenuButton(
#                 items=[
#                     ft.PopupMenuItem(text="Item 1"),
#                     ft.PopupMenuItem(),  # divider
#                     ft.PopupMenuItem(
#                         text="Checked item", checked=False, on_click=check_item_clicked
#                     ),
#                 ]
#             ),
#         ],
#     )

#     # definiendo contenedores
#     # Agregando elementos a la pagina.
#     images = ft.Column(expand=1,wrap=False,scroll="always")
#     countries = ft.Row(expand=1,wrap=False,scroll="always")
#     page.add(images,countries)
    
#     honduras ="https://cdn.jsdelivr.net/gh/hampusborgos/country-flags@main/svg/hn.svg"
#     mycontainer =ft.Row([ ft.Column(
#         controls=[
#             ft.Image(
#                 src=honduras,
#                 width=100,
#                 height=100,
#                 fit=ft.ImageFit.CONTAIN,
#                 repeat=ft.ImageRepeat.NO_REPEAT,
#                 border_radius=ft.border_radius.all(10)
#             ),
#             ft.Text(value="Honduras",height=25,weight="Bold")
#         ],width=200, height=300,horizontal_alignment=ft.alignment.center
#      )])
    

#     for country in flg[:30]:
#         images.controls.append(
#             ft.Image(
#                 src=country["flag"],
#                 width=200,
#                 height=200,
#                 fit=ft.ImageFit.CONTAIN,
#                 repeat=ft.ImageRepeat.NO_REPEAT,
#                 border_radius=ft.border_radius.all(10)
#             )
#         )
#         countries.controls.append(ft.Text(value=country["country"],height=20,weight="Bold"))    
    
#     page.add(mycontainer)
#     page.update()

# ft.app(target=main)
# #ft.app(target=main,view=ft.AppView.WEB_BROWSER)