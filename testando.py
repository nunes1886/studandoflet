import flet as ft

def main(page: ft.Page):
    title = ft.Text(value='Botão de contagem de cliques',
                    size=25)
    page.add(title)
    def button_clicked(e):
        btn.data += 1
        text.value = f'Botão acionado {btn.data} vezes'
        text.update()
        btn.update()

    btn = ft.ElevatedButton(text='Contagem de cliques',
                            on_click=button_clicked,
                            data=0)
    text = ft.Text()
    page.add(text, btn)
ft.app(target=main, assets_dir='assets')