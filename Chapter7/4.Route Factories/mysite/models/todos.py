from pyramid.httpexceptions import HTTPNotFound
from pyramid.security import Allow, Everyone
from sqlalchemy import (
    Column,
    Integer,
    Text
)
from pyramid_sqlalchemy import BaseObject, Session


class ToDo(BaseObject):
    __tablename__ = 'todo'
    id = Column(Integer, primary_key=True)
    title = Column(Text)

    __acl__ = [
        (Allow, Everyone, 'view'),
        (Allow, 'group:editors', 'edit'),
        (Allow, 'group:admins', 'edit')
    ]


def todo_factory(request):
    todo_id = request.matchdict.get('id')
    if todo_id is None:
        # Return the class
        return ToDo
    todo_id_int = int(todo_id)
    todo = Session.query(ToDo).filter_by(id=todo_id_int).first()
    if not todo:
        raise HTTPNotFound()
    return todo

sample_todos = [
    dict(title='Get Milk'),
    dict(title='Get Eggs')
]
