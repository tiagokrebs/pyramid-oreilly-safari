from pyramid_sqlalchemy import Session


class BaseModel:

    @classmethod
    def order_by(cls):
        return getattr(cls, 'title')

    @classmethod
    def by_id(cls, model_id):
        return Session.query(cls).filter_by(id=int(model_id)).first()

    @classmethod
    def list(cls):
        return Session.query(cls).order_by(cls.order_by()).all()

    @classmethod
    def add(cls, **kw):
        Session.add(cls(**kw))
        resource = Session.query(cls).filter_by(title=kw['title']).one()
        return resource

    @classmethod
    def delete(cls, resource):
        Session.delete(resource)

    def __json__(self, request):
        d = {}
        for col in self.__table__.columns:
            d[col.name] = getattr(self, col.name)
        return d

