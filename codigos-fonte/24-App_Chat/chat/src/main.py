import flet as ft
from dataclasses import dataclass

@dataclass
class Mensagem:
    usuario: str
    texto: str
    tipo_mensagem: str

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

    def enviar(e):
        page.pubsub.send_all(
            Mensagem(
                usuario=page.session.get('nome_usuario'),
                texto=nova_mensagem.value,
                tipo_mensagem="chat_message"
            )
        )
        nova_mensagem.value = ""
        page.update()

    def on_message(mensagem: Mensagem):
        if mensagem.tipo_mensagem == "chat_message":
            chat.controls.append(ft.Text(f"{mensagem.usuario}: {mensagem.texto}"))
        elif mensagem.tipo_mensagem == "login_message":
            chat.controls.append(
                ft.Text(mensagem.texto, italic=True, size=12)
            )
        page.update()

    def entrar(e):
        if not nome_usuario.value:
            nome_usuario.error_text = "Nome não pode ficar em branco!"
            nome_usuario.update()
        else:
            page.session.set("nome_usuario", nome_usuario.value)
            page.dialog.open = False
            page.pubsub.send_all(
                Mensagem(
                    usuario=nome_usuario.value,
                    texto=f"{nome_usuario.value} entrou no chat.",
                    tipo_mensagem="login_message"
                )
            )
            page.update()

    page.title = "Meu Flet Chat"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.Colors.WHITE
    page.scroll = "adaptive"

    tema = ft.Icon(name=ft.Icons.SUNNY)
    interruptor = ft.Switch(on_change=mudar_tema)
    chat = ft.Column()
    nova_mensagem = ft.TextField(label="Digite sua mensagem", on_submit=enviar)
    page.appbar = ft.AppBar(title=ft.Text("Meu Chat", size=16), actions=[tema, interruptor])
    nome_usuario = ft.TextField(label="Informe seu nome", on_submit=entrar)

    page.pubsub.subscribe(on_message)

    # REVIEW: DeprecationWarning: dialog is deprecated in version 0.23.0 and will be removed in version 0.26.0. Use Page.overlay.append(dialog) instead.
    page.dialog = ft.AlertDialog(
        open=True,
        modal=True,
        title=ft.Text("Bem Vindo!"),
        content=ft.Column([nome_usuario], tight=True),
        actions=[ft.ElevatedButton(text="Entrar no chat", on_click=entrar)],
        actions_alignment="end",
    )

    page.add(
        chat, ft.Row(controls=[nova_mensagem, ft.ElevatedButton("Enviar", on_click=enviar)])
    )

ft.app(main)