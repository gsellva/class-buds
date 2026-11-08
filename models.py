from pydantic import BaseModel

class TutorCreate(BaseModel):
    name: str
    grade: str
    school: str
    subject: str
    bio: str
    availability: str
    contact: str

class TutoringRequestCreate(BaseModel):
    student_name: str
    tutor_id: int
    preferred_time: str
    message: str = ''
