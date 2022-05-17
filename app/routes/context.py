"""Context Related Routes."""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.setup import get_db
from app.crud.context import create_context, get_context_by_user
from app.crud.user import get_user_by_id
from app.config import get_config
from app.schema.schemas import CreateContext, Context


router = APIRouter()


@router.get("/contexts/{user_id}", response_model=list[Context])
async def get_user_context(user_id: int, db: Session = Depends(get_db)):
    """
    Gets user context.

    Parameters
    ----------
    user_id :
    db :

    Returns
    -------

    """
    return get_context_by_user(db, user_id)


@router.post("/context", response_model=Context)
async def create_user_context(context: CreateContext, db: Session = Depends(get_db)):
    """
    Create context endpoint.

    Parameters
    ----------
    context : Context request schema
    db :

    Returns
    -------

    """
    config = get_config()

    user = get_user_by_id(db, context.user_id)
    if user is None:
        raise HTTPException(404, detail="User not found!")

    if len(user.context_list) == config.max_context_per_user:
        raise HTTPException(403, detail="Maximum number of contexts reached")

    # You can add other validation/business logic such as checking image/etc.

    return create_context(db, context)
