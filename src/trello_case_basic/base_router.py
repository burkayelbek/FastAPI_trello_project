from fastapi import APIRouter
from src.trello_case_basic import index_page_router
from src.trello_case_basic.routing import (
    user_router,
    login_router,
    project_router,
    job_router,
    comment_router
)


router_base = APIRouter()

router_base.include_router(index_page_router.router)
router_base.include_router(user_router.router, prefix="/users", tags=["Users"])
router_base.include_router(login_router.router, tags=["Login"])
router_base.include_router(project_router.router, prefix="/project", tags=["Project"])
router_base.include_router(job_router.router, prefix="/job", tags=["Jobs"])
router_base.include_router(comment_router.router, prefix="/comment", tags=["Comments"])
