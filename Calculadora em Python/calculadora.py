import flet as ft

def main(page: ft.Page):
    page.bgcolor = '#000'
    page.window_resizable = False
    page.window_width = 250
    page.window_height = 380
    page.title = 'Calculadora'
    page.window_always_on_top = True

ft.app(target = main)    