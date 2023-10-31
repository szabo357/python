import flet as ft

def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.bgcolor =
    txt_number = ft.TextField(value="0",text_align="center",width=100)
    
    def minus_click(e):
        txt_number.value = str(int(txt_number.value)-1)
        page.update()
    
    def add_click(e):
        txt_number.value = str(int(txt_number.value)+1)
        page.update()

    # Agregando elementos a la pagina.
    page.add(
        ft.Text(value="Hello Flet",font_family="Roboto",
            size=20,text_align=ft.MainAxisAlignment.CENTER,
            weight="Bold",color="blue"
        ),
        ft.Divider(height=50,color=ft.colors.BROWN_100),
        ft.Row(
          [
            ft.IconButton(icon=ft.icons.REMOVE,on_click=minus_click),
            txt_number,
            ft.IconButton(icon=ft.icons.ADD,on_click=add_click)    
          ],
          alignment=ft.MainAxisAlignment.CENTER              
        )            
    )
    


ft.app(target=main)
#ft.app(target=main,view=ft.AppView.WEB_BROWSER)