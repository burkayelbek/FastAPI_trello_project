from fastapi import FastAPI, Request, HTTPException, status, responses
from dotenv import load_dotenv, find_dotenv
from src.trello_case_basic.base_router import router_base

load_dotenv(find_dotenv())

app = FastAPI()

app.include_router(router_base)
