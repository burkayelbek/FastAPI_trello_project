from fastapi import APIRouter
from fastapi.responses import RedirectResponse


router = APIRouter()


@router.get("/", include_in_schema=False)
def docs_redirect():
    return RedirectResponse(url='/docs')
