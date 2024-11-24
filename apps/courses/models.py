from apps.base_entities.models import BaseEntity

from sqlalchemy import Column, Date, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship


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
