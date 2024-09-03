import flet as ft

def main(page: ft.Page):
    page.title = "{{cookiecutter.project_name}} / {{cookiecutter.author_name}}"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    greeting_text = ft.Text(
        "",
        size=20,
        weight=ft.FontWeight.BOLD,
        color=ft.colors.BLUE
    )

    def on_submit(e):
        if name_input.value.strip() == "":
            page.snack_bar = ft.SnackBar(ft.Text("Please enter a name!"), bgcolor=ft.colors.RED)
            page.snack_bar.open = True
        else:
            greeting_text.value = f"Hello, {name_input.value}!"
            name_input.value = ""
            page.update()

    name_input = ft.TextField(
        label="Enter your name",
        width=300,
        autofocus=True,
        border_radius=8,
    )

    submit_button = ft.ElevatedButton(
        text="Submit",
        on_click=on_submit,
        bgcolor=ft.colors.BLUE,
        color=ft.colors.WHITE,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8)),
    )

    
    page.add(
        ft.Container(
            content=ft.Column(
                [
                    greeting_text,
                    name_input,
                    submit_button,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            alignment=ft.alignment.center,
        )
    )


ft.app(target=main)
