import flet as ft


def main(page: ft.Page):
    # função do evento
    def mudar_conteudo(e):
        saida.value = texto.value
        saida.update()

    # propriedades da página
    page.title = "App Evento 01"
    page.scroll = "adaptive"

    # variáveis
    texto = ft.TextField(label="Insira aqui seu texto", on_change=mudar_conteudo)
    saida = ft.Text()

    page.add(
        ft.SafeArea(ft.Text("App Evento 01", size=30, weight="bold")),
        texto,
        saida
    )


ft.app(main)
