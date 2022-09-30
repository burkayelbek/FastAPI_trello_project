from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.models.user import UserModel
from src.service.job import (
    create_new_job,
    delete_selected_job,
    get_all_jobs,
    get_selected_job,
    update_selected_job
)
from src.base.database import get_db
from src.schemas.job import JobCreate, JobUpdate, JobOut
from src.trello_case_basic.routing.login_router import get_current_user_from_token
from src.trello_case_basic.schedule_conf import celery_task

router = APIRouter()


@router.post("/project/{id}/create-task", response_model=JobOut)
def create_task(
        id: int,
        job: JobCreate,
        db: Session = Depends(get_db),
        current_user: UserModel = Depends(get_current_user_from_token),
):
    task = create_new_job(id=id, job=job, db=db, job_owner_id=current_user.id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{id} - Job does not found.")
    return task


@router.get("/project/{id}/all-jobs", response_model=List[JobOut])
def get_all_jobs_projects(id: int, db: Session = Depends(get_db),
                          current_user: UserModel = Depends(get_current_user_from_token),):
    jobs = get_all_jobs(id=id, db=db, job_owner_id=current_user.id)
    if not jobs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{id} - Job does not found.")
    return jobs


@router.get(
    "/get-job/{id}", response_model=JobOut
)
def get_job_by_id(id: int, db: Session = Depends(get_db),
                  current_user: UserModel = Depends(get_current_user_from_token),):
    job = get_selected_job(id=id, db=db, owner_id=current_user.id)
    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{id} - Job does not found.")
    return job


@router.put("/update/{id}")
def update_job_by_id(id: int, job: JobUpdate, db: Session = Depends(get_db)):
    message = update_selected_job(id=id, job=job, db=db)
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{id} - Job does not found.")
    message = {"Status": "Successfully deleted."}
    return message


@router.delete("/delete/{id}")
def delete_job_by_id(id: int, db: Session = Depends(get_db), ):
    job = delete_selected_job(id=id, db=db)
    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{id} - Job does not found.")
    message = {"Status": "Successfully deleted."}
    return message


@router.get("/status_task_celery")
def celery_jobs(current_user: UserModel = Depends(get_current_user_from_token), ):
    jobs = celery_task.delay("status_task_celery", current_user.id)
    return jobs
