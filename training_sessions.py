from datetime import datetime
from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field, ConfigDict
from starlette import status

app = FastAPI()
class Training:
    id: int
    name: str  
    sets: int  
    reps: int  
    weight: float  
    notes: str
    session_date: datetime

    def __init__(self, id,name, sets, reps, weight, notes, session_date):
        self.id = id
        self.name = name 
        self.sets = sets
        self.reps = reps
        self.weight = weight
        self.notes = notes
        session_date: datetime
        
class TrainingRequest(BaseModel):
    id: int
    name: str=Field(min_length=3)
    sets: int
    reps: int
    weight: float
    notes: str=Field(min_length=5)
    session_date: datetime
    
    model_config={
        "json_schema_extra":{
            "example":{
                "id": "the id",
                "name": "bench press",
                "sets": 2,
                "reps": 2,
                "weight": 10,
                "notes": "Some notes about the sesion",
                "session_date": "2025-06-12T15:30:00Z"
            }
        }
    }

TRAINING_SESSIONS = [
    Training(1, "Lat Pulldown", 3, 2, 89.52, "pull down", "2025-03-12T15:30:00Z"),
    Training(2, "Bench Press", 4, 3, 102.34, "push","2025-02-12T15:30:00Z" ),
    Training(3, "Deadlift", 3, 2, 140.25, "lift","2022-10-12T15:30:00Z" ),
    Training(4, "Squat", 5, 3, 120.78, "lower","2023-11-12T15:30:00Z"),
    Training(5, "Overhead Press", 3, 2, 75.60, "press","2023-11-12T15:30:00Z"),
    Training(6, "Barbell Row", 4, 3, 85.90, "pull","2022-11-12T13:00:00Z"),
    Training(7, "Leg Curl", 3, 2, 65.30, "curl","2023-11-12T15:00:00Z"),
    Training(8, "Bicep Curl", 3, 2, 45.80, "curl","2025-01-12T15:30:00Z")
]

@app.get("/training_sessions", status_code=status.HTTP_200_OK)
def training_sessions():
    return TRAINING_SESSIONS


@app.get("/training_sessions/{training_sersion_id}", status_code=status.HTTP_200_OK)
def training_sessions_by_id(training_sersion_id: int):
    for training in TRAINING_SESSIONS:
        if training.id == training_sersion_id:
            return training
    raise HTTPException(status_code=404, detail="Training not found")
        
@app.get("/training_sessions/",status_code=status.HTTP_200_OK)
def training_by_name(name: str):
    training_to_return = []
    for training in TRAINING_SESSIONS:
        if training.name == name:
            training_to_return.append(training)
        return training_to_return
    
@app.post("/training_sessions/create_session", status_code=status.HTTP_201_CREATED)
async def create_new_training(session_request: TrainingRequest):
        new_session = Training(**session_request.model_dump())
        TRAINING_SESSIONS.append(find_training_id(new_session))
        
def find_training_id(training: Training):
    training.id = 1 if len(TRAINING_SESSIONS) == 0 else TRAINING_SESSIONS[-1].id + 1
    
    # if len(TRAINING_SESSIONS) > 0:
    #     training.id = TRAINING_SESSIONS[-1].id + 1
    # else:
    #     training.id = 1
        
    return training

@app.put("/training_sessions/update_training_sessions", status_code=status.HTTP_204_NO_CONTENT)
async def update_training_session(session_request: TrainingRequest):
    training_session_changed = False
    for t in range(len(TRAINING_SESSIONS)):
        if TRAINING_SESSIONS[t].id == session_request.id:
            TRAINING_SESSIONS[t] = session_request
            training_session_changed = True
    if not training_session_changed:
        raise HTTPException(status_code=404, detail="Training not found")


@app.delete("/training_sessions/{session_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_training_session(session_id: int):
    training_session_changed = False
    for t in range(len(TRAINING_SESSIONS)):
        if TRAINING_SESSIONS[t].id == session_id:
            TRAINING_SESSIONS.pop(t)
            training_session_changed = True
            break
    if not training_session_changed:
        raise HTTPException(status_code=404, detail="Training not found")