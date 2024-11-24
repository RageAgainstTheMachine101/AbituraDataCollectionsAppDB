from apps.base_entities.models import BaseEntity

from sqlalchemy import Column, Date, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship


class UserSubmission(BaseEntity):
    __tablename__ = 'user_submissions'
    step_id = Column(Integer, ForeignKey('lesson_steps.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    submission_text = Column(Text, nullable=False)
    ai_feedback = Column(Text)
    user = relationship('User', back_populates='submissions')
    step = relationship('LessonStep', back_populates='submissions')


User.submissions = relationship('UserSubmission', order_by=UserSubmission.id, back_populates='user')
LessonStep.submissions = relationship('UserSubmission', order_by=UserSubmission.id, back_populates='step')