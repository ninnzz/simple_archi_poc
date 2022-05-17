"""Context crud."""
from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.database.models import Context, UserContext
from app.schema.schemas import CreateContext


def get_context_by_user(db: Session, user_id: int) -> list[Context]:
    """
    Get all users.

    Parameters
    ----------
    db : db session
    user_id : user_id

    Returns
    -------
    users : list of users
    """
    query = db.query(Context)\
        .join(UserContext, UserContext.context_id == Context.id)\
        .filter(UserContext.user_id == user_id)

    return query.all()


def create_context(db: Session, context: CreateContext) -> Context:
    """
    Create a new user context.

    Parameters
    ----------
    db :
    context :

    Returns
    -------

    """
    try:
        db_context = Context(
            name=context.name,
            image_url=context.image_url,
            active=context.active,
            auto_process=context.auto_process,
            mask_url=context.mask_url
        )

        db.add(db_context)
        db.flush()

        db.add(UserContext(
            user_id=context.user_id,
            context_id=db_context.id
        ))

        db.commit()

    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=401, detail="Some fields have constraints!")
    except BaseException:
        db.rollback()
        raise ValueError("Database problem encountered.")

    return db_context
