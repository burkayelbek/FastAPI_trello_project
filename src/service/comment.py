from operator import and_
from datetime import datetime
from sqlalchemy.orm import Session
from src.models.comment import CommentModel
from src.models.job import JobModel
from src.schemas.comment import CommentCreate


def create_new_comment(comment: CommentCreate, db: Session, id: int, user_id: int):
    get_comment = db.query(JobModel).filter(and_(JobModel.id == id, JobModel.job_owner_id == user_id))
    if get_comment.first():
        new_comment = CommentModel(comment_id=id,
                                   created_at=datetime.now().date(),
                                   **comment.dict())
        db.add(new_comment)
        db.commit()
        db.refresh(new_comment)
        return new_comment
    else:
        return False


def get_all_comments(db: Session, id: int, user_id: int):
    get_comment = db.query(JobModel).filter(and_(JobModel.id == id, JobModel.job_owner_id == user_id))
    if get_comment.first():
        jobs = db.query(CommentModel).filter(CommentModel.comment_id == id).all()
        return jobs
    else:
        return False


def get_comment_by_id(id: int, db: Session):
    item = db.query(CommentModel).filter(CommentModel.id == id).first()
    return item


def update_comment_by_id(id: int, comment: CommentCreate, db: Session):
    selected_comment = db.query(CommentModel).filter(CommentModel.id == id)
    if not selected_comment.first():
        return False
    selected_comment.update(comment.__dict__)
    db.commit()
    return True


def delete_comment_by_id(id: int, db: Session):
    selected_comment = _get_existing_comment(id=id, db=db)
    if not selected_comment:
        return False
    selected_comment.delete(synchronize_session=False)
    db.commit()
    return True


def _get_existing_comment(db: Session, id:int):
    comment = db.query(CommentModel).filter(CommentModel.id == id)
    if comment.first():
        return comment
