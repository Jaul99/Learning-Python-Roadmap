from typing import Annotated
import typer
from rich import print


app = typer.Typer(help="A tiny calculator CLI for learning.")
Number = Annotated[float, typer.Argument(help="A number (int or float).")]


@app.command()
def add(a: Number, b: Number):
print(a + b)
