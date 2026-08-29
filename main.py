
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from database import init_db, create_user, get_user, verify_password
from ml_engine import predict_water_level, predict_flood_risk, analyze_quality
from agent_pipeline import hydro_agent_query
from simulator import DigitalTwinSimulator
import uvicorn

app = FastAPI(title="HydroSentinel AI - Advanced Edition")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
init_db()

class AuthRequest(BaseModel):
    email: str
    password: str
    name: str = ""

class PredictRequest(BaseModel):
    rainfall: float
    dam_gate: float
    upstream_level: float

sim = DigitalTwinSimulator()

@app.post("/api/signup")
def signup(req: AuthRequest):
    if get_user(req.email):
        raise HTTPException(400, "User already exists - Please login")
    create_user(req.email, req.password, req.name)
    return {"message": "Account created", "email": req.email}

@app.post("/api/login")
def login(req: AuthRequest):
    user = get_user(req.email)
    if not user or not verify_password(req.password, user['password_hash']):
        raise HTTPException(401, "Invalid email or password")
    return {"message": "Login successful", "email": req.email, "name": user['name'], "token": "hs_"+req.email}

@app.post("/api/google-auth")
def google_auth(req: AuthRequest):
    if not get_user(req.email):
        create_user(req.email, "google_oauth", req.name or "Google User")
    return {"message": "Google login successful", "email": req.email}

@app.post("/api/predict")
def predict(req: PredictRequest):
    level = predict_water_level(req.rainfall, req.dam_gate, req.upstream_level)
    flood_risk = predict_flood_risk(level, req.rainfall)
    quality = analyze_quality()
    sim_update = sim.step(req.rainfall, req.dam_gate)
    return {"water_level": level, "flood_risk": flood_risk, "quality": quality, "simulation": sim_update}

@app.post("/api/agent")
def agent(q: dict):
    return {"response": hydro_agent_query(q.get("query",""))}

@app.get("/api/sensors")
def sensors():
    from ml_engine import get_live_sensors
    return get_live_sensors()

# Serve frontend
app.mount("/", StaticFiles(directory="../frontend", html=True), name="frontend")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
