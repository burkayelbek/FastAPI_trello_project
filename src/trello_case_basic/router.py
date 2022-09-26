import logging

from src.trello_case_basic import (
    app,
    Request,
    responses,
    status
)


logger = logging.getLogger(__name__)


@app.get("/")
async def home():
    """
    This Method Get Home Page
    """
    return {"message": "Hello World"}
