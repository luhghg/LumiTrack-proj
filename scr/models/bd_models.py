from scr.db.session import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, ForeignKey, func
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    full_name: Mapped[str | None] = mapped_column()
    email: Mapped[str] = mapped_column(unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    role: Mapped[str] = mapped_column() 
    is_active: Mapped[bool] = mapped_column(default=True)

class Course(Base):
    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str | None]
    creator_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

class Enrollment(Base):
    __tablename__ = "enrollments"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id"), primary_key=True)
    enrolled_at: Mapped[datetime] = mapped_column(server_default=func.now())
    is_completed: Mapped[bool] = mapped_column(default= False)

class Modul(Base):
    __tablename__ = "modules"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str | None]
    order_index: Mapped[int]
    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id"))

class Lesson(Base):
    __tablename__ = "lessons"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str | None]
    content: Mapped[str| None]
    module_id: Mapped[int] = mapped_column(ForeignKey("modules.id"))

class MentorshipRequest(Base):
    __tablename__ = "mentorship_requests"

    id : Mapped[int] = mapped_column(primary_key=True)
    sender_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    mentor_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    status: Mapped[str]


