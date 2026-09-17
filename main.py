from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import Base, engine, SessionLocal
import models
import schemas


Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@app.post("/events", response_model=schemas.EventResponse)
def create_event(
    event: schemas.EventCreate,
    db: Session = Depends(get_db)
):
    db_event = models.Event(
        title=event.title,
        description=event.description,
        date=event.date,
        location=event.location,
        organizer=event.organizer,
        category=event.category
    )

    db.add(db_event)
    db.commit()
    db.refresh(db_event)

    return db_event


@app.get("/events", response_model=list[schemas.EventResponse])
def get_events(db: Session = Depends(get_db)):
    events = db.query(models.Event).all()
    return events


@app.put("/events/{event_id}", response_model=schemas.EventResponse)
def update_event(
    event_id: int,
    event: schemas.EventCreate,
    db: Session = Depends(get_db)
):
    db_event = db.query(models.Event).filter(models.Event.id == event_id).first()

    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")

    db_event.title = event.title
    db_event.description = event.description
    db_event.date = event.date
    db_event.location = event.location
    db_event.organizer = event.organizer
    db_event.category = event.category

    db.commit()
    db.refresh(db_event)

    return db_event

@app.delete("/events/{event_id}")
def delete_event(
    event_id: int,
    db: Session = Depends(get_db)
):
    db_event = db.query(models.Event).filter(models.Event.id == event_id).first()

    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")

    db.delete(db_event)
    db.commit()

    return {"message": "Event deleted successfully"}
