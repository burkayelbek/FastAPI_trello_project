from src.trello_case_basic.routing import user_router
from src.trello_case_basic import index_page_router
from fastapi import APIRouter

router_base = APIRouter()

router_base.include_router(index_page_router.router)
router_base.include_router(user_router.router, prefix="/users")




