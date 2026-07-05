import flet as ft

class CalcButton(ft.ElevatedButton):
    def __init__(self, text, button_clicked, expand=1, color=ft.Colors.WHITE24):
        super().__init__()
        # Text'i bir kontrol olarak content içine koyuyoruz
        self.content = ft.Text(value=text, size=20, weight=ft.FontWeight.BOLD)
        self.expand = expand
        self.on_click = button_clicked
        self.style = ft.ButtonStyle(
            bgcolor=color,
            shape=ft.RoundedRectangleBorder(radius=8)
        )

def main(page: ft.Page):
    page.title = "Flet Hesap Makinesi"
    page.window_width = 350
    page.window_height = 500
    page.bgcolor = ft.Colors.BLACK
    
    # Text kontrolünü result için de kullanalım
    result = ft.Text(value="0", color=ft.Colors.WHITE, size=40)

    def button_clicked(e):
        # Butonun içindeki metni alalım
        data = e.control.content.value
        
        if data == "AC":
            result.value = "0"
        elif data == "=":
            try:
                result.value = str(eval(result.value.replace("x", "*")))
            except:
                result.value = "Hata"
        else:
            if result.value == "0" or result.value == "Hata":
                result.value = data
            else:
                result.value += data
        page.update()

    page.add(
        ft.Container(
            padding=20,
            content=ft.Column(
                controls=[
                    ft.Row(controls=[result], alignment=ft.MainAxisAlignment.END),
                    ft.Row(controls=[
                        CalcButton("AC", button_clicked, color=ft.Colors.ORANGE),
                        CalcButton("/", button_clicked, color=ft.Colors.ORANGE_700),
                    ]),
                    ft.Row(controls=[
                        CalcButton("7", button_clicked),
                        CalcButton("8", button_clicked),
                        CalcButton("9", button_clicked),
                        CalcButton("x", button_clicked, color=ft.Colors.ORANGE_700),
                    ]),
                    ft.Row(controls=[
                        CalcButton("4", button_clicked),
                        CalcButton("5", button_clicked),
                        CalcButton("6", button_clicked),
                        CalcButton("-", button_clicked, color=ft.Colors.ORANGE_700),
                    ]),
                    ft.Row(controls=[
                        CalcButton("1", button_clicked),
                        CalcButton("2", button_clicked),
                        CalcButton("3", button_clicked),
                        CalcButton("+", button_clicked, color=ft.Colors.ORANGE_700),
                    ]),
                    ft.Row(controls=[
                        CalcButton("0", button_clicked, expand=2),
                        CalcButton(".", button_clicked),
                        CalcButton("=", button_clicked, color=ft.Colors.GREEN_700),
                    ]),
                ]
            )
        )
    )

ft.app(target=main)
