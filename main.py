import flet as ft
from PIL import Image
def main(page: ft.Page):
    img = ft.Image(src='image/nunes.jpg',
                   border_radius=50,
                   width=100,
                   tooltip='Logo da Nunes Sublimação'
                   )
    page.add(img)
    title = ft.Text(value='Nunes Sublimação', size=25)
    page.add(title)
    btn1 = ft.ElevatedButton(text='Click here')
    btn2 = ft.ElevatedButton(text='Like', icon=ft.icons.FAVORITE_BORDER,
                             icon_color=ft.colors.RED,
                             url='https://www.google.com/')
    style = ft.ButtonStyle(
        color = {
            ft.MaterialState.HOVERED: ft.colors.WHITE,
            ft.MaterialState.DEFAULT: ft.colors.BLACK,
        },
        bgcolor = {
            ft.MaterialState.HOVERED: ft.colors.PINK,
            '': ft.colors.AMBER,
        },
        padding = {
            ft.MaterialState.HOVERED: 20
        }
    )

    btn3 = ft.ElevatedButton(text='Botão personalizado', style=style)

    def button_clicked(e):
        btn4.data += 1
        text.value = f'Botão acionado {btn4.data} vezes'
        text.update()
        btn4.update()

    btn4 = ft.ElevatedButton(text='Contagem de cliques',
                             on_click = button_clicked,
                             data=0)
    text = ft.Text()
    page.add(btn1, btn2, btn3)
    page.add(btn4, text)
ft.app(target=main, assets_dir='assets')