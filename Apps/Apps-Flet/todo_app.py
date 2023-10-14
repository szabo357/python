import flet as ft

def to_do(page: ft.Page):
    page.title="To-Do App"

    def add_clicked(e):
        tasks_view.controls.append(ft.Checkbox(label=new_task.value))
        new_task.value=""
        view.update()
    
    new_task = ft.TextField(hint_text="¿Qué tareas hay que hacer?",expand=True)
    tasks_view = ft.Column()
    view=ft.Column(
        width=600,
        controls=[
            ft.Row(
                controls=[
                    new_task, 
                    ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add_clicked)
                ],  
            ),
            tasks_view,
        ],
    )
    
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(view)
   
ft.app(target=to_do)
#ft.app(target=to_do,view=ft.AppView.WEB_BROWSER)

#Theres work in progress