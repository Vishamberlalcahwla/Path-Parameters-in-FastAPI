from fastapi import FastAPI
app = FastAPI()

@app.get('/myage/{age}')
def MyAgeis(age:int):
    if age > 18 :
        return "You are adult" 
    else :
        return " You are child"     
