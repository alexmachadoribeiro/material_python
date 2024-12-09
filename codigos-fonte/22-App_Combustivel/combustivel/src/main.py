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

    def calcular_combustivel(e):
        if not gasolina.value:
            gasolina.error_text = "Gasolina não pode ficar vazio"
            page.update()
        else:
            gasolina.error_text = ""
            page.update()

        if not etanol.value:
            etanol.error_text = "Etanol não pode ficar vazio"
            page.update()
        else:
            etanol.error_text = ""

            gasolina.value = float(gasolina.value.replace(",", "."))
            etanol.value = float(etanol.value.replace(",", "."))

            resultado = "Gasolina" if etanol.value >= gasolina.value*0.7 else "Etanol"

            dlg_modal.content.value = resultado
            gasolina.value = ""
            etanol.value = ""

            page.open(dlg_modal)

            page.update()

    page.title = "Combustível"
    page.scroll = "adaptive"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.Colors.WHITE

    tema = ft.Icon(name=ft.icons.SUNNY)
    interruptor = ft.Switch(on_change=mudar_tema)

    gasolina = ft.TextField(
        label="Valor da gasolina",
        prefix_text="R$ ",
        keyboard_type=ft.KeyboardType.NUMBER
    )
    etanol = ft.TextField(
        label="Valor da etanol",
        prefix_text="R$ ",
        keyboard_type=ft.KeyboardType.NUMBER,
        on_submit=calcular_combustivel
    )
    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Melhor combustível:"),
        content=ft.Text(size=20, weight="bold"),
        actions=[ft.TextButton("OK", on_click=lambda e: page.close(dlg_modal))],
        actions_alignment=ft.MainAxisAlignment.END
    )

    page.appbar = ft.AppBar(
        leading=ft.Image(src=f"https://img.icons8.com/fluency/48/gas-station.png", fit=ft.ImageFit.CONTAIN),
        leading_width=48,
        title=ft.Text("Combustível", size=16),
        actions=[tema, interruptor]
    )

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
        ),
        ft.Row(
            [
                ft.Container(
                    ft.ElevatedButton("Verificar", on_click=calcular_combustivel),
                    padding=30
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

ft.app(main)