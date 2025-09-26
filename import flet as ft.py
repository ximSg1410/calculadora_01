import flet as ft
import math


def main(page: ft.Page):
    page.title="Calculadora Simple"
    page.bgcolor=ft.Colors.PURPLE_ACCENT_400

    titulo=ft.Text(
        "🧧 Calculadora Basica",
        size=28,
        text_align="center",
        weight="bold"
    ) 
        label="Numero 1",
        width=200,
        text_style=ft.TextStyle(color=ft.colors.GREEN)
    )

    num2=ft.TextField(
        label="Numero 2",
        width=200,
        text_style=ft.TextStyle(color=ft.colors.GREEN)
    )

    resultado=ft.Text(
        value="Resultado",
        size=20,
        color=ft.Colors.GREEN,
        text_align="center"
    )
    
    info=ft.Container(
        content=ft.Text(
            "📊 para el boton de porcentaje: el campo de arriba es el numero de base y el de abajo es el porcentaje(%) que quieres calcular.",
            size=13,
            color=ft.Colors.GREEN,
            text_align="center",
            italic=True,
            max_lines=2,
            overflow="clip"

        )
        alignment=ft.alignment.center,
        widht=400,
        padding=5
    )

    #Funcion para mostrar el resultado
    def mostrar_resultado (valor):
        resultado.value = f"Resultado: {valor}"
        page.update ()

#Funciones de operaciones
    def suma(e):
        try:
            res = float(num.value) + float(num2.value)
            mostrar_resultado (res)
        except:
            mostrar_resultado("Error")

    def resta(e):
        try:
            res = float(num1.value) - float(num2.value)
            mostrar_resultado (res)
        except:
            mostrar_resultado("Error")

    def multiplicacion (e):
        try:
            res = float(num1.value) * float(num2.value)
            mostrar_resultado(res)
         except:
            mostrar_resultado("Error")
    def division (e):
        try:
            if float(numZvalue) == 0:
                mostrar_resultado("Division por cero")
            else:
                res = float(num1.value) / float(num2.value)
                mostrar_resultado(res)
        except:
            mostrar_resultado("Error")  

    def pocentaje(e):
        try:
            res = (float(num1.value) * float(num2.value)) / 100
            mostrar_resultado("Error")

    def raiz_cuadrada(e):
        try:
            res1 = math.sqrt(float(num1.value))
            res2 = math.sqrt(float(num2.value))
            mostrar_resultado(f"‼{num1.value}={res1:.2f} ¡ {num2.value}={res2:.2f}")
         except:
            mostrar_resultado("Error")

    # Layout general, todo centrado
    page.add(
        ft.Column(
            (
                ft.Row(titulo), alignment="center"),
                ft.Row(num1, alignment="center"),
                ft.Row(num2, alignment="center"),       
                    )
                      ft.ElevatedButton("➕ Sumar, on_click=suma, widht=120),
                      ft.ElevatedButton("➖ Restar", on_click=resta, widht=120),
                      ft.ElevatedButton("✖ Multiplicar", on_click=multiplicacion, widht=120),
                    (,
                     spacing=10,
                     algnment="center"
                    ),
                    ft.Row(resultado), alignment="center"),
                    ft.Row(info, alignment="center"), #Label informativo al final y centrado
                ),
                 alignment="center",
                 horizontal_alignment="center"
                 expand=True,
                 spacing=15
        )
    )     
ft.app(target=main, view=ft.WEB_BROWSER)
         




                                             
            
            
        
