import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return[1,2,3]

@app.get('/contact', response_class=HTMLResponse)
def get_list():
    """ return{'name' : 'Platzi'} """
    return """ 
    
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            <h1>Title desde main.py</h1>
            <p> I a text in p </p>
        </body>
        </html>

     """

def run():
    store.get_categories()

if __name__ == '__main__':
    run()


    