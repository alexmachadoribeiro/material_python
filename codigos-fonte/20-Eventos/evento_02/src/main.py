import flet as ft
from dataclasses import dataclass

# classe Pessoa
@dataclass
class Pessoa:
    nome: str
    cargo: str
    email: str

def main(page: ft.Page):
    # função do evento do botão
    def mostrar_dados(e):
        msg.value = "\nSegue os dados do usuário:\n"
        nome.value = f"Nome: {usuario.nome.value}."
        cargo.value = f"Cargo: {usuario.cargo.value}."
        email.value = f"E-mail: {usuario.email.value}."

        page.update()

    # instancia objeto
    usuario = Pessoa(nome="", cargo="", email="")

    # propriedades da página
    page.title = "App Evento 02"
    page.scroll = "adaptive"

    # seta os valores informados pelo usuário
    usuario.nome = ft.TextField(label="Nome")
    usuario.cargo = ft.TextField(label="Cargo")
    usuario.email = ft.TextField(label="E-mail", on_submit=mostrar_dados)

    # botão
    botao = ft.ElevatedButton("Cadastrar", on_click=mostrar_dados)

    # saída de dados
    msg = ft.Text(weight="bold")
    nome = ft.Text()
    cargo = ft.Text()
    email = ft.Text()

    page.add(
        ft.SafeArea(ft.Text("App Evento 02", size=30, weight="bold")),
        usuario.nome,
        usuario.cargo,
        usuario.email,
        botao,
        msg,
        nome,
        cargo,
        email
    )


ft.app(main)