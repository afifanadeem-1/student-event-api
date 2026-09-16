from fastapi import FastAPI

app = FastAPI()


@app.get("/events")
def get_events():
    events = [
        {
            "id": 1,
            "title": "AI Workshop",
            "description": "Introduction to Artificial Intelligence",
            "date": "2026-10-15",
            "location": "CS Building, Room 204",
            "organizer": "CS Society",
            "category": "Workshop"
        },
        {
            "id": 2,
            "title": "Hackathon 2026",
            "description": "A 24-hour programming competition",
            "date": "2026-10-20",
            "location": "Innovation Lab",
            "organizer": "Tech Society",
            "category": "Hackathon"
        },
        {
            "id": 3,
            "title": "Freshers Social",
            "description": "An informal social event for students",
            "date": "2026-10-25",
            "location": "Courtyard",
            "organizer": "Student Affairs",
            "category": "Social"
        }
    ]

    return events
