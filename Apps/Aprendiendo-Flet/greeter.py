import flet as ft

def main(page: ft.Page):
    
    def clicked(e):
        if not txt.value :
           txt.error_text = "Please enter your name"
           page.update() 
        else:
            name = txt.value
            page.clean()
            page.add(ft.Text(f"Hello, {name}!"))
  
    txt = ft.TextField(label="escribe tu nombre",hint_text="Escribe tu nombre")
    btn = ft.ElevatedButton(text="Saluda!", tooltip="Saluda",on_click=clicked)
    page.add(txt,btn)
    
ft.app(target=main)