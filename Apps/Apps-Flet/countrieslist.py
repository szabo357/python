import flet as ft

def main(page: ft.Page):
    page.title = "Flet countries List"
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.bgcolor = ft.colors.INDIGO_100
    txt_number = ft.TextField(value="0",text_align="center",width=100)
    
    # Agregando elementos a la pagina.
    page.add(
        ft.Text(value="Hello Flet",font_family="Roboto",
            size=20,text_align=ft.MainAxisAlignment.CENTER,
            weight="Bold",color="blue"
        ),
        ft.Divider(height=50,color=ft.colors.BROWN_100),
        ft.Row(
          alignment=ft.MainAxisAlignment.CENTER              
        )            
    )
    
ft.app(target=main)
#ft.app(target=main,view=ft.AppView.WEB_BROWSER)