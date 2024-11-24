from apps.base_entities.models import BaseEntity
from apps.users.models import User, UserEmail, UserCourse
from apps.courses.models import Course, CourseModule, ModuleLesson, LessonStep
from apps.mood_journals.models import MoodEntry, EmotionTag
from apps.submissions.models import Submission, SubmissionFeedback

from datetime import date
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

# Setting up the database engine and session
engine = create_engine('sqlite:///mydatabase.db')
Session = sessionmaker(bind=engine)
session = Session()

# Ensure that all tables exist
BaseEntity.metadata.create_all(engine)

# Mock data insertion
def populate_mock_data():
    # Ensure that data is inserted in the correct order and relationships are maintained
    user1 = User(name="Alice", date_of_birth=date(1990, 1, 1))
    user2 = User(name="Bob", date_of_birth=date(1995, 2, 2))
    user3 = User(name="Charlie", date_of_birth=date(2000, 3, 3))

    session.add_all([user1, user2, user3])
    session.commit()

    email1 = UserEmail(email="alice@example.com", user_id=user1.id)
    email2 = UserEmail(email="bob@example.com", user_id=user2.id)
    email3 = UserEmail(email="charlie@example.com", user_id=user3.id)

    session.add_all([email1, email2, email3])
    session.commit()

    course1 = Course(title="Math 101", description="Introduction to Algebra")
    course2 = Course(title="History 101", description="Ancient Civilizations")

    session.add_all([course1, course2])
    session.commit()

    user_course1 = UserCourse(user_id=user1.id, course_id=course1.id)
    user_course2 = UserCourse(user_id=user2.id, course_id=course2.id)

    session.add_all([user_course1, user_course2])
    session.commit()

    module1 = CourseModule(title="Algebra", course_id=course1.id)
    module2 = CourseModule(title="Ancient History", course_id=course2.id)

    session.add_all([module1, module2])
    session.commit()

    lesson1 = ModuleLesson(title="Lesson 1", module_id=module1.id)
    lesson2 = ModuleLesson(title="Lesson A", module_id=module2.id)

    session.add_all([lesson1, lesson2])
    session.commit()

    step1 = LessonStep(question="What is 2+2?", lesson_id=lesson1.id, right_answer="4")
    step2 = LessonStep(question="Who built the pyramids?", lesson_id=lesson2.id, right_answer="Ancient Egyptians")

    session.add_all([step1, step2])
    session.commit()

    mood1 = MoodEntry(user_id=user1.id, date=date(2021, 1, 1))
    mood2 = MoodEntry(user_id=user2.id, date=date(2021, 1, 2))

    session.add_all([mood1, mood2])
    session.commit()

    tag1 = EmotionTag(value="Joy")
    tag2 = EmotionTag(value="Sorrow")

    session.add_all([tag1, tag2])
    session.commit()

    submission1 = Submission(user_id=user1.id, step_id=step1.id, text="First Submission")
    submission2 = Submission(user_id=user2.id, step_id=step2.id, text="Second Submission")

    session.add_all([submission1, submission2])
    session.commit()

    feedback1 = SubmissionFeedback(submission_id=submission1.id, feedback="Good job!")
    feedback2 = SubmissionFeedback(submission_id=submission2.id, feedback="Needs improvement")

    session.add_all([feedback1, feedback2])
    session.commit()

# Populate the database with mock data
populate_mock_data()
