"""User crud."""
from sqlalchemy.orm import Session

from app.database.models import User
from app.schema.schemas import GetUsersFilter


def get_user(db: Session, user_filter: GetUsersFilter) -> list[User]:
    """
    Get all users.

    Parameters
    ----------
    db : db session
    user_filter : filter data class

    Returns
    -------
    users : list of users
    """
    query = db.query(User)

    if user_filter.name is not None:
        query = query.filter(User.name == user_filter.name)
    if user_filter.email is not None:
        query = query.filter(User.email == user_filter.email)

    return query.all()


def get_user_by_id(db: Session, user_id: int) -> User:
    """
    Filter user by id
    Parameters
    ----------
    db :
    user_id :

    Returns
    -------

    """
    return db.query(User).filter(User.id == user_id).first()


def populate_users(db: Session):
    users = [
        ["nin@hacarus.com", "ninz"],
        ["marlon@hacarus.com", "marlon"]
    ]

    # Delete everything first
    db.query(User).delete()
    
    for i, user in enumerate(users):
        db.add(User(id=i, email=user[0], name=user[1]))

    db.commit()
