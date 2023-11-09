import flet as ft
import countriesdata as cd
world = cd.World.countries
flag = cd.World.flags

def main(page: ft.Page):
    page.title="Countries of the World"
    page.bgcolor=ft.colors.INDIGO_100
    page.window_min_width  = 300
    page.window_min_height = 400
    page.window_max_width  = 500
    page.window_max_height = 600

    def layout(countries,flags):    
        lv = ft.ListView(
            expand=1,  
            padding=5,
            spacing=10,
            divider_thickness=0
        )
        
        for country in countries:
            for flag in flags :    
                if country["name"] == flag["country"]:
                    lv.controls.append(ft.Container(
                        padding=10,
                        margin=10,
                        bgcolor=ft.colors.BLUE_100,
                        content= ft.Column(
                            controls=[
                                ft.Row([
                                    ft.Column([
                                        ft.Image(
                                            src=f'{ flag["flag"] }',
                                            width=180,
                                            height=150,
            #                               fit=ft.ImageFit.FIT_HEIGHT,
                                            fit=ft.ImageFit.FILL,
                                            repeat=ft.ImageRepeat.NO_REPEAT,
                                            border_radius=ft.border_radius.all(10)
                                        )
                                    ]),
                                    ft.Column([
                                        ft.Text(value=f'Country: {country["name"]}'),
                                        ft.Text(value=f'Capital: {country["capital"]}'),
                                        ft.Text(value=f'Population: {country["population"]}'),
                                        ft.Text(value=f'Currency: {country["currency"]}'),
                                        ft.Text(value=f'Languages: {country["languages"]}')
                                    ])
                                ])                  
                            ]
                        )
                    ))

        return lv
        
    page.add(layout(world,flag))
    
    print(f"World length: {len(world)}")
    print(f"Flags length: {len(world)}")
    page.update()

ft.app(target=main)
# #ft.app(target=main,view=ft.AppView.WEB_BROWSER)