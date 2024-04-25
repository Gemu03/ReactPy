
from reactpy import component, html
from reactpy.backend.fastapi import configure

@component
def HelloWorld():
    return html.div(
        html.h1("Lista de tareas!"),
        html.ul(
            Item("Tarea 1"),
            Item("Tarea 2"),
            Item("Tarea 3000"),
        )
    )

@component
def Item(text: str):
    return html.li(text)
