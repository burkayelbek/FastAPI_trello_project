from fastapi import FastAPI, Request, HTTPException, status, responses
from dotenv import load_dotenv


load_dotenv()

app = FastAPI()
