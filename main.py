from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from fastapi.staticfiles import StaticFiles
from database import init_database
from routers import pages, tutors, requests, admin

app = FastAPI(title='Peer Tutoring Platform')
app.mount('/static', StaticFiles(directory='static'), name='static')

@app.on_event('startup')
def startup():
    init_database()

# SQLite rejects IDs above 64 bits, and no such record can exist.
@app.exception_handler(OverflowError)
def id_too_large(request, exc):
    return PlainTextResponse('Not found', status_code=404)

app.include_router(pages.router)
app.include_router(tutors.router)
app.include_router(requests.router)
app.include_router(admin.router)
