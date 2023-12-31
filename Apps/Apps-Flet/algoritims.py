import flet as ft
import random
import time

def main(page: ft.Page):
    page.title = "Sorting Algorithms"
    page.bgcolor = ft.colors.BLUE_100

    def containers(count):
        items= []
        for _  in range(count):
            items.append(    
                ft.Container(
                    content=ft.Text( value=random.randint(1,200),
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        font_family="Roboto"
                    ),
                    alignment=ft.alignment.center,
                    width=80,
                    height=80,
                    bgcolor=ft.colors.ORANGE,
                    border_radius=40,
                )
            )
        return items


# Sorting Algoritms
    def bubble_sort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1 ):
                arr[j].bgcolor=ft.colors.YELLOW
                arr[j + 1].bgcolor=ft.colors.YELLOW
                time.sleep(2)
                page.update()
                if arr[j].content.value > arr[j + 1].content.value :
                    arr[j] , arr[j + 1] = arr[j + 1] , arr[j]    
                arr[j].bgcolor=ft.colors.ORANGE
                arr[j + 1].bgcolor=ft.colors.ORANGE
            arr[n-i-1].bgcolor=ft.colors.GREEN

        page.update()


    def selection_sort(arr):
        n = len(arr)
        for i in range( n - 1):
            menor = i
            for j in range(i + 1, n):
                if arr[j].content.value < arr[menor].content.value:
                    menor = j
                    time.sleep(2)
                    arr[menor].bgcolor = ft.colors.YELLOW
                    page.update()
            if menor != i:
                arr[menor], arr[i] = (arr[i], arr[menor])
                arr[menor].bgcolor = ft.colors.ORANGE
                time.sleep(2)
                page.update()
            time.sleep(2)
            arr[i].bgcolor = ft.colors.GREEN
            page.update()
        time.sleep(2)
        arr[j].bgcolor = ft.colors.GREEN
        page.update()
    ##
    # 
    # Sorting Algoritms to implement.
    #       
    def quick_sort(arr):
        
        if len(arr) < 2:
            return arr
        pivot_index = random.randrange(len(arr))  # Use random element as pivot
        pivot = arr[pivot_index]
    
        greater: list[int] = []  # All elements greater than pivot
        lesser: list[int] = []  # All elements less than or equal to pivot
        
        for element in arr[:pivot_index]:
            (greater if element > pivot else lesser).append(element)

        for element in arr[pivot_index + 1 :]:
            (greater if element > pivot else lesser).append(element)

        return [*quick_sort(lesser), pivot, *quick_sort(greater)]
    
    
    def double_sort(arr):
        
        arrlen = len(arr)
        for _ in range(int(((arrlen - 1) / 2) + 1)):  
            # we don't need to traverse to end of list as
            for j in range(arrlen - 1):
                arr[j].bgcolor=ft.colors.YELLOW
                arr[j + 1].bgcolor=ft.colors.YELLOW
                time.sleep(2)
                page.update()
            # apply the bubble sort algorithm from left to right (or forwards)
                if arr[j + 1].content.value < arr[j].content.value:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                arr[j].bgcolor=ft.colors.GREEN
                arr[j + 1].bgcolor=ft.colors.GREEN
                # apply the bubble sort algorithm from right to left (or backwards)
                if arr[arrlen - 1 - j].content.value < arr[arrlen - 2 - j].content.value:
                    (
                        arr[arrlen - 1 - j],
                        arr[arrlen - 2 - j],
                    ) = (
                        arr[arrlen - 2 - j],
                        arr[arrlen - 1 - j],
                    )
                arr[arrlen - 2 - j].bgcolor=ft.colors.GREEN
                arr[arrlen - 1 - j].bgcolor=ft.colors.GREEN
            arr[arrlen - 1].bgcolor=ft.colors.GREEN
            
        page.update()


    def merge_sort(arr):
        page.update


    def insertion_sort(arr):
        page.update()


# Event Listeners
    def list_size_change(e):
        list_row.clean()
        balls = containers(int(list_size.value))
        list_row.controls = balls 
        page.update()


    def algoritms_change(e):
        title.value = "Sorting Algorithm: "  + algoritms.value
        page.update()


    def reset_click(e):
        list_row.clean()
        balls = containers(int(list_size.value))
        list_row.controls = balls 
        page.update()


    def start_click(e):
        balls = list_row.controls
        # if para elegir algoritmo de ordenamiento
        if algoritms.value == "Bubble Sort":
            bubble_sort(balls)
        elif algoritms.value == "Selection Sort":
            selection_sort(balls)
        elif algoritms.value == "Quick Sort":

            arr = []
            
            for i in range(len(balls)):
                arr.append(balls[i].content.value)

            arr2 = quick_sort(arr) 
            
            for i in range(len(balls)):
                balls[i].content.value = arr2[i]    
                balls[i].bgcolor = ft.colors.GREEN
        
        elif algoritms.value == "Double Sort":
            double_sort(balls)
        elif algoritms.value == "Merge Sort":
            merge_sort(balls)
        elif algoritms.value == "Insertion Sort":
            insertion_sort(balls)
        page.update()


    def bgcolor_dropdown_change(e):
        if bgcolor.value == "Blue":
            page.bgcolor = ft.colors.BLUE_100
        elif bgcolor.value == "Green":
            page.bgcolor = ft.colors.GREEN_100
        elif bgcolor.value == "Purple":
            page.bgcolor = ft.colors.PURPLE_100
        elif bgcolor.value == "Orange":
            page.bgcolor = ft.colors.ORANGE_100            
        elif bgcolor.value == "Amber":
            page.bgcolor = ft.colors.AMBER_100
        divider1.color = bgcolor.value
        divider2.color = bgcolor.value
        page.update()


    list_size = ft.Dropdown(
        label= "List Size",
        on_change=list_size_change,
        options=[
            ft.dropdown.Option("6"),
            ft.dropdown.Option("8"),
            ft.dropdown.Option("10"),
            ft.dropdown.Option("12"),
            ft.dropdown.Option("14"),
        ],
        width=200,
        value="6"
    )
        
    algoritms = ft.Dropdown(
        label= "Sorting Algorithm",
        on_change= algoritms_change,
        options= [
            ft.dropdown.Option("Bubble Sort"),
            ft.dropdown.Option("Selection Sort"),
            ft.dropdown.Option("Quick Sort"),
            ft.dropdown.Option("Double Sort"),
            ft.dropdown.Option("Merge Sort"),
            ft.dropdown.Option("Insertion Sort"),
        ],
        value = "Bubble Sort",
        width=200,
    )    

    bgcolor = ft.Dropdown(
        label= "Background Color:",
        on_change=bgcolor_dropdown_change,
        options=[
            ft.dropdown.Option("Blue"),
            ft.dropdown.Option("Green"),
            ft.dropdown.Option("Purple"),
            ft.dropdown.Option("Orange"),
            ft.dropdown.Option("Amber"),
        ],
        value = "Blue",
        width=200,
    )

    title =ft.Text(
            value = "Sorting Algoritm: "+ algoritms.value , 
            weight=ft.FontWeight.BOLD,
            font_family="Roboto",
            style=ft.TextThemeStyle.HEADLINE_MEDIUM
    )

    balls = containers(int(list_size.value))
    list_row = ft.Row(balls,alignment=ft.MainAxisAlignment.CENTER)
    divider1 = ft.Divider(thickness=5,color="blue")
    divider2 = ft.Divider(thickness=5,color="blue")
    btn_start = ft.OutlinedButton("Start Sorting",on_click=start_click,icon=ft.icons.PLAY_CIRCLE_OUTLINED,
                              style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)))
    btn_reset = ft.OutlinedButton("Reset",on_click=reset_click,icon=ft.icons.LOCK_RESET,
                              style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)))
    

    page.add(
        ft.Row([title],alignment=ft.MainAxisAlignment.CENTER),divider1, list_row, divider2,
        ft.Row([algoritms,list_size , bgcolor,btn_start,btn_reset],alignment= ft.MainAxisAlignment.CENTER)
    )


ft.app(target=main)