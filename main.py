from fastapi import FastAPI

app = FastAPI()


'''
Two Types of servers

ASGI - 

WSGI - 

uvicorn main:app  to run 
uvicorn main:app --reload to run with update on changes

'''

fruits = ["Apple","Grape","Orange"]

@app.get("/")
def home():
    return "Hello this is home page"

@app.get("/about")
def about():
    return {"msg":"hello this is about us"}

@app.get("/fruits")
def get_fruits():
    return fruits

@app.get("/fruits/{fruit_index}")
def get_fruit(fruit_index:int):
    return {"chosen_fruit":fruits[fruit_index]}

