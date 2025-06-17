from fastapi import FastAPI, Request, Depends
from .models import SessionLocal, Feedback, Base, engine
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class FeedbackIn(BaseModel):
    message: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/submit-feedback")
def submit_feedback(data: FeedbackIn, db: Session = Depends(get_db)):
    feedback = Feedback(message=data.message, status="pending")
    db.add(feedback)
    db.commit()
    return {"status": "success"}

@app.get("/admin/pending")
def get_pending_feedback(db: Session = Depends(get_db)):
    feedbacks = db.query(Feedback).filter(Feedback.status == "pending").order_by(Feedback.id).all()
    return [{"id": f.id, "message": f.message} for f in feedbacks]

@app.get("/get-feedback")
def get_feedback(db: Session = Depends(get_db)):
    feedbacks = db.query(Feedback).filter(Feedback.status == "approved").order_by(Feedback.id.desc()).limit(20).all()
    return {"feedback": [f.message for f in feedbacks]}


@app.post("/admin/moderate/{feedback_id}")
def moderate(feedback_id: int, action: str, db: Session = Depends(get_db)):
    feedback = db.query(Feedback).filter(Feedback.id == feedback_id).first()
    if not feedback:
        return {"status": "error", "msg": "Not found"}

    if action == "approve":
        feedback.status = "approved"
    elif action == "reject":
        feedback.status = "rejected"
    else:
        return {"status": "error", "msg": "Invalid action"}

    db.commit()
    return {"status": "success"}

@app.get("/debug/all")
def get_all(db: Session = Depends(get_db)):
    return [{"id": f.id, "msg": f.message, "status": f.status} for f in db.query(Feedback).all()]
