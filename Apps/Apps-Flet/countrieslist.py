import flet as ft

def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment=ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="0",text_align="center",width=100)
    
    def minus_click(e):
        txt_number.value = str(int(txt_number.value)-1)
        page.update()
    
    def add_click(e):
        txt_number.value = str(int(txt_number.value)+1)
        page.update()

    page.add(
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