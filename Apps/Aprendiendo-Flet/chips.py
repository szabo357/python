import flet as ft
# This is a chips example.
# Very easy to follow. 
def main(page: ft.Page):
    def amenity_selected(e):
        page.update()

    title = ft.Row([ft.Icon(ft.icons.HOTEL_CLASS), ft.Text("Amenities")])
    amenities = ["Washer / Dryer", "Ramp access", "Dogs OK", "Cats OK", "Smoke-free"]
    amenity_chips = []

    for amenity in amenities:
        amenity_chips.append(
            ft.Chip(
                label=ft.Text(amenity),
                bgcolor=ft.colors.GREEN_200,
                disabled_color=ft.colors.GREEN_100,
                autofocus=True,
                on_select=amenity_selected,
            )
        )

    page.add(title, ft.Row(amenity_chips))

ft.app(target=main)