from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from scr.api.auth_router import router as router_auth
from scr.api.course_router import router as router_course
from scr.api.enrollment_router import router as router_enrollment
from scr.api.mentorship_router import router as router_mentorship
from scr.api.lesson_router import router as router_lesson
from scr.api.user_router import router as router_user
import uvicorn


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router_auth)
app.include_router(router_course)
app.include_router(router_enrollment)
app.include_router(router_mentorship)
app.include_router(router_lesson)
app.include_router(router_user)


if __name__ == "__main__":
    uvicorn.run("scr.main:app", reload = True)