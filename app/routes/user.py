"""User Related Routes."""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.setup import get_db
from app.crud.user import get_user
from app.schema.schemas import User, GetUsersFilter

router = APIRouter()


@router.get("/users", response_model=list[User])
def get_users(u_filter: GetUsersFilter = Depends(), db: Session = Depends(get_db)):
    """
    Get userlist function
    Parameters
    ----------
    u_filter : get user filter
    db : db session

    Returns
    -------

    """
    return get_user(db, u_filter)
