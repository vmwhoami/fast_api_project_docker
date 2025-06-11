from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()
class Training:
    id: int
    name: str  
    sets: int  
    reps: int  
    weight: float  
    notes: str

    def __init__(self, id,name, sets, reps, weight, notes):
        self.id = id
        self.name = name 
        self.sets = sets
        self.reps = reps
        self.weight = weight
        self.notes = notes
        
class TrainingRequest(BaseModel):
    id: int
    name: str=Field(min_length=3)
    sets: int
    reps: int
    weight: float
    notes: str=Field(min_length=5)
    
    model_config={
        "json_schema_extra":{
            "example":{
                "id": "the id",
                "name": "bench press",
                "sets": 2,
                "reps": 2,
                "weight": 10,
                "notes": "Some notes about the sesion"
            }
        }
    }

TRAINING_SESSIONS = [
    Training(1, "Lat Pulldown", 3, 2, 89.52, "pull down"),
    Training(2, "Bench Press", 4, 3, 102.34, "push"),
    Training(3, "Deadlift", 3, 2, 140.25, "lift"),
    Training(4, "Squat", 5, 3, 120.78, "lower"),
    Training(5, "Overhead Press", 3, 2, 75.60, "press"),
    Training(6, "Barbell Row", 4, 3, 85.90, "pull"),
    Training(7, "Leg Curl", 3, 2, 65.30, "curl"),
    Training(8, "Bicep Curl", 3, 2, 45.80, "curl")
]

@app.get("/training_sessions")
def training_sessions():
    return TRAINING_SESSIONS


@app.get("/training_sessions/{training_sersion_id}")
def training_sessions_by_id(training_sersion_id: int):
    for training in TRAINING_SESSIONS:
        if training.id == training_sersion_id:
            return training
        
@app.get("/training_sessions/")
def training_by_name(name: str):
    training_to_return = []
    for training in TRAINING_SESSIONS:
        if training.name == name:
            training_to_return.append(training)
        return training_to_return
    
@app.post("/training_sessions/create_session")
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

@app.put("/training_sessions/update_training_sessions")
async def update_training_session(session_request: TrainingRequest):
    for t in range(len(TRAINING_SESSIONS)):
        if TRAINING_SESSIONS[t].id == session_request.id:
            TRAINING_SESSIONS[t] = session_request


@app.delete("/training_sessions/{session_id}")
async def delete_training_session(session_id: int):
    for t in range(len(TRAINING_SESSIONS)):
        if TRAINING_SESSIONS[t].id == session_id:
            TRAINING_SESSIONS.pop(t)
            break
        