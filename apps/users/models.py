from apps.base_entities.models import BaseEntity

from sqlalchemy import Column, Date, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy


class User(BaseEntity):
    __tablename__ = 'users'
    name = Column(String, nullable=False)
    date_of_birth = Column(Date, nullable=False)

    # Updated relationship to connect to UserCourse
    user_courses = relationship('UserCourse', back_populates='user')

    # Define a proxy to get courses directly
    courses = association_proxy('user_courses', 'course')


class UserEmail(BaseEntity):
    __tablename__ = 'user_emails'
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    email = Column(String, unique=True, nullable=False)
    is_primary = Column(Boolean, default=False, nullable=False)

    user = relationship('User', back_populates='emails')


User.emails = relationship('UserEmail', order_by=UserEmail.id, back_populates='user')


class UserCourse(BaseEntity):
    __tablename__ = 'user_courses'
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    course_id = Column(Integer, ForeignKey('courses.id'), nullable=False)

    # Relationships back to User and Course
    user = relationship('User', back_populates='user_courses')
    course = relationship('Course', back_populates='user_courses')
