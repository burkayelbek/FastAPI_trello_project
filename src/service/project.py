from operator import and_
from src.models.project import ProjectModel
from src.schemas.project import ProjectCreate
from sqlalchemy.orm import Session
from datetime import datetime
from fastapi.encoders import jsonable_encoder


def create_new_project(project: ProjectCreate, db: Session, owner_id: int):
    new_project = ProjectModel(owner_id=owner_id,
                               created_at=datetime.now().date(),
                               is_active=True,
                               **project.dict())
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project


def get_project_by_id(id: int, db: Session, owner_id: int):
    project = db.query(ProjectModel).filter(and_(ProjectModel.id == id, ProjectModel.owner_id == owner_id)).first()
    return project


def get_all_projects(db: Session, owner_id: int):
    projects = db.query(ProjectModel).filter(ProjectModel.owner_id == owner_id).all()
    return projects


def full_update_project_by_id(id: int, project: ProjectCreate, db: Session, owner_id):
    selected_project = _get_existing_project(id=id, db=db)
    if not selected_project:
        return False
    selected_project.update(project.__dict__)
    db.commit()
    return True


def delete_project_by_id(id: int, db: Session):
    selected_project = _get_existing_project(id=id, db=db)
    if not selected_project:
        return False
    selected_project.delete(synchronize_session=False)
    db.commit()
    return True


def _get_existing_project(id: int, db: Session):
    project = db.query(ProjectModel).filter(ProjectModel.id == id)
    if project.first():
        return project
