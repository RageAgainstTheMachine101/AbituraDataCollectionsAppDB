from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey, Boolean, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Association table for many-to-many relationship between MoodEntry and EmotionTag
mood_entry_emotion_tag = Table(
    'mood_entry_emotion_tag', Base.metadata,
    Column('mood_entry_id', Integer, ForeignKey('mood_entries.id'), primary_key=True),
    Column('emotion_tag_id', Integer, ForeignKey('emotion_tags.id'), primary_key=True)
)

class BaseEntity(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True)


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


class EmotionTag(BaseEntity):
    __tablename__ = 'emotion_tags'
    value = Column(String, nullable=False)


class MoodEntry(BaseEntity):
    __tablename__ = 'mood_entries'
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    date = Column(Date, nullable=False)
    text = Column(Text)
    voice_record = Column(String)
    user = relationship('User', back_populates='mood_entries')
    emotion_tags = relationship('EmotionTag', secondary=mood_entry_emotion_tag, back_populates='mood_entries')


User.mood_entries = relationship('MoodEntry', order_by=MoodEntry.id, back_populates='user')


class Course(BaseEntity):
    __tablename__ = 'courses'
    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)


class CourseModule(BaseEntity):
    __tablename__ = 'course_modules'
    course_id = Column(Integer, ForeignKey('courses.id'), nullable=False)
    title = Column(String, nullable=False)
    course = relationship('Course', back_populates='modules')


Course.modules = relationship('CourseModule', order_by=CourseModule.id, back_populates='course')


class ModuleLesson(BaseEntity):
    __tablename__ = 'module_lessons'
    module_id = Column(Integer, ForeignKey('course_modules.id'), nullable=False)
    title = Column(String, nullable=False)
    module = relationship('CourseModule', back_populates='lessons')


CourseModule.lessons = relationship('ModuleLesson', order_by=ModuleLesson.id, back_populates='module')


class LessonStep(BaseEntity):
    __tablename__ = 'lesson_steps'
    lesson_id = Column(Integer, ForeignKey('module_lessons.id'), nullable=False)
    step_text = Column(Text, nullable=False)
    right_answer = Column(Text, nullable=False)
    lesson = relationship('ModuleLesson', back_populates='steps')


ModuleLesson.steps = relationship('LessonStep', order_by=LessonStep.id, back_populates='lesson')


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
