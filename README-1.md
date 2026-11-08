# Peer Tutoring Platform

## Requirements

Make sure you have:

- Python 3.10+
- pip

## 1. Install Dependencies

Open a terminal in the project folder and run:

```bash
pip install -r requirements.txt
```

## 2. Run the Application

Run:

```bash
ADMIN_PASSWORD=choose-a-password uvicorn main:app --reload
```

Then open:

```text
http://127.0.0.1:8000
```

## 3. Admin Page

Open:

```text
http://127.0.0.1:8000/admin
```

The admin page can be used to:

- Review tutor applications
- Approve tutors
- Reject tutors
- Remove approved tutors
- Restore rejected tutors
- View tutoring requests
- Add impact stories
- Edit impact stories
- Delete impact stories

> Note: Log in with the username `admin` and the password from `ADMIN_PASSWORD`. The admin page stays locked if `ADMIN_PASSWORD` is not set.

## 4. API Documentation

FastAPI provides interactive API documentation at:

```text
http://127.0.0.1:8000/docs
```

## 5. Database

The project uses SQLite.

The database is initialized automatically when the application starts. You do not need to create the database manually.

## 6. Stop the Application

Press:

```text
CTRL + C
```

in the terminal to stop the server.
