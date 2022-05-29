from fastapi import FastAPI
app = FastAPI()

@app.get("/aboutuser/me")
def aboutme():
    return "It is me"

@app.get("/aboutuser/{userid}")
def aboutother(userid:str):
    return "This is employee of alnafi " + userid

