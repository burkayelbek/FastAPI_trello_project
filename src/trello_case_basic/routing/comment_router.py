from typing import List
from fastapi import (APIRouter, Depends, HTTPException, status)
from sqlalchemy.orm import Session
from src.trello_case_basic.routing.login_router import get_current_user_from_token
from src.models.user import UserModel
from src.service.comment import (
    create_new_comment,
    delete_comment_by_id,
    get_all_comments, get_comment_by_id,
    update_comment_by_id
)
from src.base.database import get_db
from src.schemas.comment import CommentCreate, CommentUpdate, CommentOut


router = APIRouter()


@router.post("/task/{id}/create_comment", response_model=CommentOut)
def create_comment(id: int,
                   comment: CommentCreate,
                   db: Session = Depends(get_db),
                   current_user: UserModel = Depends(get_current_user_from_token),
                   ):
    new_comment = create_new_comment(id=id, comment=comment, db=db, user_id=current_user.id)
    if not new_comment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{id} Comment does not found.")
    return new_comment


@router.get("/task/{id}/all", response_model=List[CommentOut])
def get_comments(id: int, db: Session = Depends(get_db),
                 current_user: UserModel = Depends(get_current_user_from_token)):
    comments = get_all_comments(db=db, id=id,user_id=current_user.id)
    if not comments:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"{id} Comment does not found.")
    return comments


@router.get("/get-comments/{id}", response_model=CommentOut)
def get_specific_comment(id: int, db: Session = Depends(get_db),):
    comment = get_comment_by_id(id=id, db=db)
    if not comment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"{id} Comment does not found.")
    return comment


@router.put("/update/{id}")
def update_comment(id: int, comment: CommentUpdate, db: Session = Depends(get_db),):
    selected_comment = update_comment_by_id(id=id, comment=comment, db=db)
    if not selected_comment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"{id} Comment does not found.")
    message = {"Status": "Successfully updated."}
    return message

@router.delete("/delete/{id}")
def delete_comment(id: int, db: Session = Depends(get_db),
                   current_user: UserModel = Depends(get_current_user_from_token)):
    selected_comment = delete_comment_by_id(id=id, db=db)
    if not selected_comment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{id} Job does not exist in system.")
    message = {"Status": "Successfully updated."}
    return message

