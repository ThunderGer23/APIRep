from fastapi import FastAPI
from routes.rep import rep
from notigram import ping

app = FastAPI()
# ping('daa39d53-6283-47a1-b945-b7ee6528dde0', f'APIRep Reportandose, Kawamonga')
app.include_router(rep)

