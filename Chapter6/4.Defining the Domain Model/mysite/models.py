# importa itens comuns de sqlalchemy
from sqlalchemy import (
    Column,
    Integer,
    Text
)
from pyramid_sqlalchemy import BaseObject

# classe ToDo que representa a tabela 'todo' no banco de dados
class ToDo(BaseObject):
    __tablename__ = 'todo'
    id = Column(Integer, primary_key=True)
    title = Column(Text, unique=True)

sample_todos = [
    dict(title='Get Milk'),
    dict(title='Get Eggs')
]
