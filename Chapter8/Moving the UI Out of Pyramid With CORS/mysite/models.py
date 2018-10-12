from pyramid.httpexceptions import HTTPNotFound
from sqlalchemy import (
    Column,
    Integer,
    Text
)
from pyramid_sqlalchemy import Session, BaseObject

from .base_model import BaseModel


class ToDo(BaseObject, BaseModel):
    __tablename__ = 'todo'
    id = Column(Integer, primary_key=True)
    title = Column(Text, unique=True)


def todo_factory(request):
    todo_id = request.matchdict.get('id')
    if todo_id is None:
        # Return the class
        return ToDo
    todo = ToDo.by_id(request.matchdict.get('id'))
    if not todo:
        raise HTTPNotFound()
    return todo


sample_todos = [
    dict(title='Get Milk'),
    dict(title='Get Eggs')
]
