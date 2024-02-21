from fastapi import Response, status, Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, models, oauth2
from ..database import get_db


router = APIRouter(
    prefix="/vote",
    tags=["Vote"]
)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def vote_for_post(vote: schemas.Vote, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id {vote.post_id} not found")

    vote_query = db.query(models.Vote).filter(
        models.Vote.post_id == vote.post_id, models.Vote.user_id == current_user.id)
    found_vote = vote_query.first()
    if found_vote:
        vote_query.delete(synchronize_session=False)
        db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        new_vote = models.Vote(user_id=current_user.id, **vote.model_dump())
        db.add(new_vote)
        db.commit()
        db.refresh(new_vote)
        return {"message": "Vote added"}
