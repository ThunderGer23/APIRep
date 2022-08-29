from fastapi import FastAPI
from routes.rep import rep

app = FastAPI()
app.include_router(rep)

