import flet as ft

def main(page: ft.Page):
    # propriedades do app
    page.title = "Meu primeiro App"
    page.scroll = "adaptive"

    page.add(
        ft.SafeArea(ft.Text("Meu Primeiro Flet App", size=30, weight="bold")),
        ft.Image(
            src="https://alexmachadoribeiro.github.io/assets/png_transparente/minha_imagem.png",
            fit=ft.ImageFit.CONTAIN,
            error_content=ft.Text("Não foi possível carregar a imagem.")
        )
    )

ft.app(main)
