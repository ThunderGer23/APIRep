from fastapi import FastAPI
from routes.rep import rep
from notigram import ping

Token = 'daa39d53-6283-47a1-b945-b7ee6528dde0'

app = FastAPI()
ping(Token, f'APIRep Reportandose, Kawamonga')
app.include_router(rep)

