from typing import List
from src.base.database import get_db
from fastapi import (APIRouter, Depends, HTTPException,status)
from src.schemas.project import (ProjectCreate, ProjectUpdate, ShowProject)
from sqlalchemy.orm import Session
from src.trello_case_basic.routing.login_router import get_current_user_from_token
from src.models.user import UserModel
from src.service.project import (
    create_new_project,
    get_all_projects,
    delete_project_by_id,
    get_project_by_id,
    full_update_project_by_id,
)

router = APIRouter()


@router.post("/create-project/", response_model=ShowProject)
def create_project(
        project: ProjectCreate,
        db: Session = Depends(get_db),
        current_user: UserModel = Depends(get_current_user_from_token),
):
    new_project = create_new_project(project=project, db=db, owner_id=current_user.id)
    return new_project


@router.get("/get-all-projects", response_model=List[ShowProject])
def get_projects(db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user_from_token), ):
    projects = get_all_projects(db=db, owner_id=current_user.id)
    return projects


@router.get("/get-project-by-id/{id}", response_model=ShowProject)
def get_project(id: int, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user_from_token), ):
    project = get_project_by_id(id=id, db=db, owner_id=current_user.id)
    if not project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{id} - Project does not found")
    return project


@router.put("/update-project-by-id/{id}")
def update_project_put(id: int, project: ProjectUpdate, db: Session = Depends(get_db),
                   current_user: UserModel = Depends(get_current_user_from_token)):
    selected_project = full_update_project_by_id(id=id, project=project, db=db, owner_id=current_user)
    if not selected_project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{id} - Project does not found")
    return selected_project


@router.delete("/delete-project-by-id/{id}")
def delete_project(id: int, db: Session = Depends(get_db),
                   current_user: UserModel = Depends(get_current_user_from_token)):
    selected_project = delete_project_by_id(id=id, db=db)
    if not selected_project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{id} - Project does not found")
    message = {"Status": "Successfully deleted."}
    return message
