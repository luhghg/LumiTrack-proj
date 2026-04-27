# SkillFlow — Corporate Learning & Mentorship Platform

A REST API for managing corporate training: courses, modules, lessons, and mentorship requests.

## Tech Stack

- **FastAPI** — web framework
- **SQLAlchemy 2.0** (async) — ORM
- **PostgreSQL** — database
- **Alembic** — database migrations
- **Pydantic v2** — data validation
- **JWT** — authentication (python-jose)
- **passlib + bcrypt** — password hashing

## Architecture

Layered architecture (Separation of Concerns):

```
src/
├── api/          # Routers — entry points (HTTP)
├── core/         # Config, JWT, password hashing
├── db/           # Database session
├── models/       # SQLAlchemy ORM models
├── repositories/ # Database queries (SELECT, INSERT)
├── schemas/      # Pydantic models (validation)
├── services/     # Business logic
└── main.py
```

## Database Schema

| Table | Description |
|---|---|
| `users` | Users with roles (admin/user) |
| `courses` | Courses created by admins |
| `enrollments` | Many-to-many: users ↔ courses |
| `modules` | Course modules (ordered) |
| `lessons` | Lessons inside modules |
| `mentorship_requests` | Mentorship request system |

## API Endpoints

### Auth
| Method | Endpoint | Description |
|---|---|---|
| POST | `/auth/register` | Register new user |
| POST | `/auth/login` | Login, get JWT token |

### Users
| Method | Endpoint | Description |
|---|---|---|
| GET | `/users/me` | Get current user profile |

### Courses
| Method | Endpoint | Description | Role |
|---|---|---|---|
| POST | `/courses/` | Create course | Admin |
| GET | `/courses/` | List all courses | Any |
| GET | `/courses/{id}` | Get course by ID | Any |

### Enrollments
| Method | Endpoint | Description |
|---|---|---|
| POST | `/enrollments/{course_id}` | Enroll in course |
| GET | `/enrollments/my` | My enrolled courses |

### Lessons & Modules
| Method | Endpoint | Description | Role |
|---|---|---|---|
| POST | `/lessons/courses/{id}/modules` | Add module | Admin |
| GET | `/lessons/courses/{id}/modules` | Get course modules | Any |
| POST | `/lessons/modules/{id}/lessons` | Add lesson | Admin |
| GET | `/lessons/modules/{id}/lessons` | Get module lessons | Any |

### Mentorship
| Method | Endpoint | Description |
|---|---|---|
| POST | `/mentorship/request` | Send mentorship request |
| PATCH | `/mentorship/request/{id}` | Accept/reject request |

## Setup & Run

**1. Clone the repository**
```bash
git clone https://github.com/yourusername/skillflow.git
cd skillflow
```

**2. Create virtual environment**
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

**3. Install dependencies**
```bash
pip install fastapi uvicorn[standard] sqlalchemy[asyncio] asyncpg psycopg[binary] alembic pydantic pydantic-settings "pydantic[email]" passlib[bcrypt] python-jose[cryptography] bcrypt==4.0.1
```

**4. Configure environment**

Create `.env` file:
```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=skillflow
DB_USER=postgres
DB_PASS=yourpassword
SECRET_KEY=your-secret-key-here
```

**5. Run migrations**
```bash
alembic upgrade head
```

**6. Start server**
```bash
uvicorn scr.main:app --reload
```

**7. Open docs**

Go to [http://localhost:8000/docs](http://localhost:8000/docs)

## Key Features

- JWT authentication with role-based access control (admin/user)
- Layered architecture — router → service → repository
- Async database queries with SQLAlchemy 2.0
- Alembic migrations for schema versioning
- Pydantic v2 for request/response validation
- Mentorship request system with status flow (pending → accepted/rejected)
