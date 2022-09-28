from operator import and_
from src.models.project import ProjectModel
from src.schemas.project import ProjectCreate
from sqlalchemy.orm import Session
from datetime import datetime


def get_all_projects(db: Session, owner_id: int):
    all_projects = db.query(ProjectModel).filter(ProjectModel.owner_id == owner_id).all()
    return all_projects


def get_project_by_id(id: int, db: Session, owner_id: int):
    project = db.query(ProjectModel).filter(and_(ProjectModel.id == id, ProjectModel.owner_id == owner_id)).first()
    return project


def create_new_project(project: ProjectCreate, db: Session, owner_id: int):
    new_project = ProjectModel(is_active=True, owner_id=owner_id, date_posted=datetime.now().date(), **project.dict())
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project


def update_project_by_id(id: int, project: ProjectCreate, db: Session, owner_id):
    existing_project = db.query(ProjectModel).filter(ProjectModel.id == id)
    if not existing_project.first():
        return
    existing_project.update(project.__dict__)
    db.commit()
    return True


def delete_project_by_id(id: int, db: Session):
    existing_project = db.query(ProjectModel).filter(ProjectModel.id == id)
    if not existing_project.first():
        return False
    existing_project.delete(synchronize_session=False)
    db.commit()
    return True
