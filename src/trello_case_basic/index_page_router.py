from fastapi.responses import RedirectResponse
from src.trello_case_basic import (
    Request,
)
from fastapi import APIRouter

router = APIRouter()


@router.get("/", include_in_schema=False)
def docs_redirect():
    return RedirectResponse(url='/docs')
