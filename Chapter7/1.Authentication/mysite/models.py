from sqlalchemy import (
    Column,
    Integer,
    Text
)
from pyramid_sqlalchemy import BaseObject


class ToDo(BaseObject):
    __tablename__ = 'todo'
    id = Column(Integer, primary_key=True)
    title = Column(Text)

sample_todos = [
    dict(title='Get Milk'),
    dict(title='Get Eggs')
]
