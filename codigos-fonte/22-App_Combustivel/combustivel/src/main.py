import flet as ft

def main(page: ft.Page):
    def mudar_tema(e):
        page.theme_mode = (
            ft.ThemeMode.DARK
            if page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        page.bgcolor = (
            ft.Colors.WHITE
            if page.theme_mode == ft.ThemeMode.LIGHT
            else ft.Colors.GREY_900
        )
        tema.name = (
            ft.Icons.SUNNY
            if page.theme_mode == ft.ThemeMode.LIGHT
            else ft.Icons.MODE_NIGHT
        )
        page.update()

    page.title = "Combustível"
    page.scroll = "adaptive"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.Colors.WHITE

    tema = ft.Icon(name=ft.Icons.SUNNY)
    interruptor = ft.Switch(on_change=mudar_tema)

    gasolina = ft.TextField(
        label="Valor da gasolina",
        prefix="R$",
        keyboard_type=ft.KeyboardType.NUMBER
    )
    etanol = ft.TextField(
        label="Valor da etanol",
        prefix="R$",
        keyboard_type=ft.KeyboardType.NUMBER
    )

    page.appbar = ft.AppBar(title=ft.Text("Combustível", size=16), actions=[tema, interruptor])

    page.add(
        ft.SafeArea(
            ft.Row(
                [ft.Text("\nCusto-benefício combustível\n", size=25, weight="bold")],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ),
        ft.ResponsiveRow(
            [
                ft.Container(gasolina, col={"sm": 6, "md": 4, "xl": 2}),
                ft.Container(etanol, col={"sm": 6, "md": 4, "xl": 2})
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

ft.app(main)