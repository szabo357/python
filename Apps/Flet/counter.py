import flet as ft

def main(page: ft.Page):
    page.title = "Contador con Flet"   
   # page.theme = theme
   # page.theme = theme.Theme(color_scheme_seed='green') 
    page.bgcolor="Blue_100"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    txt_Field = ft.TextField(value="0",text_align=ft.TextAlign.CENTER,width= 200,bgcolor="Yellow")

    def minus_click(e):
        txt_Field.value = str(int(txt_Field.value)-1)
        page.update()

    def plus_click(e):
        txt_Field.value = str(int(txt_Field.value)+1)
        page.update()

    page.add(
      ft.Row(
          [
              ft.IconButton(ft.icons.REMOVE,on_click = minus_click),
              txt_Field,
              ft.IconButton(ft.icons.ADD,on_click = plus_click)
          ],
        alignment=ft.MainAxisAlignment.CENTER
      )

    )       

ft.app(target=main) # Asi funciona como app de escritorio.
#ft.app(target=main, view=ft.AppView.WEB_BROWSER) Asi funciona como App Web