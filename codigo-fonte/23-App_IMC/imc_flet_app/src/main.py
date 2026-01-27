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

    def calcular_imc(e):
        if not peso.value:
            peso.error_text = "Peso não pode ficar vazio"
            page.update()
        else:
            peso.error_text = ""
            page.update()

        if not altura.value:
            altura.error_text = "Altura não pode ficar vazio"
            page.update()
        else:
            altura.error_text = ""

            peso.value = float(peso.value.replace(",", "."))
            altura.value = float(altura.value.replace(",", "."))

            imc = peso.value / (altura.value**2)

            dlg_modal.title.value = f"Seu IMC: {imc:.2f}."

            if imc < 17:
                dlg_modal.content.value = "Você está muito abaixo do peso. Procure um médico."
            elif imc < 18.5:
                dlg_modal.content.value = "Você está abaixo do peso."
            elif imc < 25:
                dlg_modal.content.value = "Você está no seu peso ideal. Parabéns!"
            elif imc < 30:
                dlg_modal.content.value = "Você está acima do seu peso ideal."
            elif imc < 35:
                dlg_modal.content.value = "Você está com Obesidade I."
            elif imc < 40:
                dlg_modal.content.value = "Você está com Obesidade II."
            else:
                dlg_modal.content.value = "Você está com Obesidade mórbida. Procure um médico."

            page.open(dlg_modal)

            peso.value = ""
            altura.value = ""

            page.update()

    page.title = "IMC"
    page.scroll = "adaptive"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.Colors.WHITE

    tema = ft.Icon(name=ft.Icons.SUNNY)
    interruptor = ft.Switch(on_change=mudar_tema)

    peso = ft.TextField(
        label="Peso",
        suffix_text="kg",
        keyboard_type=ft.KeyboardType.NUMBER
    )
    altura = ft.TextField(
        label="Altura",
        suffix_text="m",
        keyboard_type=ft.KeyboardType.NUMBER,
        on_submit=calcular_imc
    )
    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text(),
        content=ft.Text(size=20, weight="bold"),
        actions=[ft.TextButton("OK", on_click=lambda e: page.close(dlg_modal))],
        actions_alignment=ft.MainAxisAlignment.END
    )

    page.appbar = ft.AppBar(
        leading=ft.Image(src=f"https://img.icons8.com/color/48/bmi.png", fit=ft.ImageFit.CONTAIN),
        leading_width=48,
        title=ft.Text("IMC", size=16),
        actions=[tema, interruptor]
    )

    page.add(
        ft.SafeArea(
            ft.Row(
                [ft.Text("\nÍndice de Massa Corporal", size=25, weight="bold")],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ),
        ft.ResponsiveRow(
            [
                ft.Container(peso, col={"sm": 6, "md": 4, "xl": 2}),
                ft.Container(altura, col={"sm": 6, "md": 4, "xl": 2})
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                ft.Container(
                    ft.ElevatedButton("Verificar", on_click=calcular_imc),
                    padding=30
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

ft.app(main)

# TODO: para criar o executável, use o comando:
# NOTE - esse funciona: flet pack imc_flet_app/src/main.py --target=imc_flet_app.exe --name=imc_flet_app --icon assets/icone_app.png
# REVIEW - testar esse depois: flet build src/main.py --target=imc_flet_app.exe --name=imc_flet_app