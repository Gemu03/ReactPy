from reactpy.backend.fastapi import configure
from fastapi import FastAPI
from components.components import HelloWorld

app = FastAPI()

""" @app.get("/")
 """









configure(app, HelloWorld)