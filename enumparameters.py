from enum import Enum 
from fastapi import FastAPI 

class Modelname(str,Enum):
    JAVA="JAVA"
    PYTHON="PYTHON"
    GO="GO"

app = FastAPI()

@app.get("/developer/{prg}")
def youaredeveloperof(prg:str):
    if Modelname.JAVA == prg:
        return "You are JAVA Developer"
    elif Modelname.PYTHON == prg:
        return "You are PYTHON Developer"
    elif Modelname.GO == prg:
        return "You are GO Developer"
    else:
        return "You are not developer for our need"    