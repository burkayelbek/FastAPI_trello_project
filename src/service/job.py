from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy import and_
from src.models.job import JobModel
from src.models.project import ProjectModel
from src.schemas.job import JobCreate
from src.base.database import SessionLocal


def create_new_job(job: JobCreate, db: Session, id: int, job_owner_id: int):
    project = db.query(ProjectModel).filter(
        and_(ProjectModel.id == id, ProjectModel.owner_id == job_owner_id))

    if project.first():
        new_job = JobModel(job_owner_id=job_owner_id,
                           project_id=id,
                           created_at=datetime.now().date(),
                           is_active=True,
                           **job.dict())
        db.add(new_job)
        db.commit()
        db.refresh(new_job)
        return new_job
    else:
        return False


def get_all_jobs(id: int, db: Session, job_owner_id: int):
    jobs = db.query(JobModel).filter(and_(JobModel.job_owner_id == job_owner_id, JobModel.project_id == id)).all()
    return jobs


def get_selected_job(id: int, db: Session, owner_id: int):
    selected_job = db.query(JobModel).filter(and_(JobModel.id == id, JobModel.job_owner_id == owner_id)).first()
    return selected_job


def update_selected_job(id: int, job: JobCreate, db: Session):
    selected_job = _get_existing_job(id=id, db=db)
    if not selected_job:
        return False
    selected_job.update(job.__dict__)
    db.commit()
    return True


def delete_selected_job(id: int, db: Session):
    selected_job = _get_existing_job(id=id, db=db)
    if not selected_job:
        return False
    selected_job.delete(synchronize_session=False)
    db.commit()
    return True


def _get_existing_job(id: int, db: Session):
    selected_job = db.query(JobModel).filter(JobModel.id == id)
    if selected_job.first():
        return selected_job


def status_task_celery(user_id: int):
    session = SessionLocal()
    jobs = session.query(JobModel).filter(JobModel.job_owner_id == user_id).all()
    message = {"Status": f"{jobs} completed successfully!"}
    return message
