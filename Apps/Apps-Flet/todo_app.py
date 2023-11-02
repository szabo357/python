import flet as ft

class Task(ft.UserControl):
    def __init__(self, task_name, task_delete):
        super().__init__()
        self.task_name = task_name
        self.task_delete = task_delete

    def build(self):
        self.display_task = ft.Checkbox(value=False, label=self.task_name)
        self.edit_name = ft.TextField(expand=1)
        
        self.display_view = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.display_task,
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.CREATE_OUTLINED,
                            tooltip="Editar To-Do",
                            on_click=self.edit_clicked,
                        ),
                        ft.IconButton(
                            icon=ft.icons.DELETE_OUTLINED,
                            tooltip="Eliminar To-Do",
                            on_click=self.delete_clicked,
                        ),
                    ],
                ),
            ],
        )

        self.edit_view = ft.Row(
            visible= False,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.edit_name,
                ft.IconButton(
                    icon= ft.icons.DONE_OUTLINE_OUTLINED,
                    icon_color=ft.colors.GREEN,
                    tooltip="Update To-Do",
                    on_click = self.save_clicked,
                ),
            ],
        )
        return ft.Column(controls=[self.display_view,self.edit_view])
    
    def edit_clicked(self,e):
        self.edit_name.value = self.display_task.label
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()
    
    def save_clicked(self,e):
        self.display_task.label= self.edit_name.value
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()
        
    def delete_clicked(self,e):
        self.task_delete(self)

class TodoApp(ft.UserControl):
    def build(self):
        self.new_task = ft.TextField(hint_text="¿Qué tareas hay que hacer?",expand=True)
        self.tasks = ft.Column()

        # application's root control (i.e "view") containing all other controls
        return ft.Column(
            width=600,
            scroll=ft.ScrollMode.AUTO,
            controls=[
                ft.Row(
                    controls=[
                        self.new_task,
                        ft.FloatingActionButton(icon=ft.icons.ADD, on_click=self.add_clicked),
                    ],
                ),
                self.tasks,
            ],
        )        

    def add_clicked(self,e):
        task = Task(self.new_task.value,self.task_delete)
        self.tasks.controls.append(task)
        self.new_task.value =""
        self.update() 

    def task_delete(self,task):
        self.tasks.controls.remove(task)
        self.update()
    
def main(page: ft.Page):
    page.title = "ToDo App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    #create application instance
    todo = TodoApp()

    #add application's root control to the page
    page.add(todo)


ft.app(target=main)
#ft.app(target=to_do,view=ft.AppView.WEB_BROWSER)

#Theres work in progress