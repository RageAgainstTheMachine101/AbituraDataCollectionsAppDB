from apps.base_entities.models import BaseEntity

from sqlalchemy import Column, Date, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship


class User(BaseEntity):
    __tablename__ = 'users'
    name = Column(String, nullable=False)
    date_of_birth = Column(Date, nullable=False)


class UserEmail(BaseEntity):
    __tablename__ = 'user_emails'
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    email = Column(String, unique=True, nullable=False)
    is_primary = Column(Boolean, default=False, nullable=False)

    user = relationship('User', back_populates='emails')


User.emails = relationship('UserEmail', order_by=UserEmail.id, back_populates='user')
