from sqlalchemy.orm import Session

from db.models.course import Course
from pydantic_schemas.course import CourseCreate


def get_course(db: Session, course_id: int):
    return db.query(Course).filter(Course.id == course_id).first()


def get_courses(db: Session):
    return db.query(Course).all()


def get_user_courses(db: Session, user_id: int):
    courses = db.query(Course).filter(Course.user_id == user_id).all()
    return courses


def create_course(db: Session, course: CourseCreate):
    db_course = Course(
        title=course.title,
        description=course.description,
        user_id=course.user_id
    )
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course
