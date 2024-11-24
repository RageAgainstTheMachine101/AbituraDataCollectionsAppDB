from apps.base_entities.models import BaseEntity
from apps.users.models import User
from apps.courses.models import LessonStep

from sqlalchemy import Column, Date, Integer, String, ForeignKey, Boolean, Text
from sqlalchemy.orm import relationship


class Submission(BaseEntity):
    __tablename__ = 'submissions'
    step_id = Column(Integer, ForeignKey('lesson_steps.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    text = Column(Text, nullable=False)

    user = relationship('User', back_populates='submissions')
    step = relationship('LessonStep', back_populates='submissions')


User.submissions = relationship('Submission', order_by=Submission.id, back_populates='user')
LessonStep.submissions = relationship('Submission', order_by=Submission.id, back_populates='step')


class SubmissionFeedback(BaseEntity):
    __tablename__ = 'submission_feedback'
    submission_id = Column(Integer, ForeignKey('submissions.id'), nullable=False)
    feedback = Column(Text, nullable=False)

    submission = relationship('Submission', back_populates='feedback')


Submission.feedback = relationship('SubmissionFeedback', back_populates='submission')
