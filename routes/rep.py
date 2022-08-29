from fastapi import APIRouter

rep = APIRouter()

@rep.get('/')
def home():
    return 'This route from analize the docs with IA'