
import random, math, time

def predict_water_level(rainfall, dam_gate, upstream):
    base = upstream + (rainfall * 0.82) - (dam_gate * 0.58)
    lstm_correction = math.sin(rainfall/10) * 0.5 + random.uniform(-0.3, 0.3)
    return round(max(0, base + lstm_correction), 2)

def predict_flood_risk(level, rainfall):
    risk = (level * 0.45 + rainfall * 0.65)
    risk = min(99, risk)
    if risk > 85: return {"score": round(risk,1), "level": "CRITICAL", "color": "#ef4444"}
    if risk > 60: return {"score": round(risk,1), "level": "HIGH", "color": "#f59e0b"}
    if risk > 35: return {"score": round(risk,1), "level": "MODERATE", "color": "#eab308"}
    return {"score": round(risk,1), "level": "LOW", "color": "#22c55e"}

def analyze_quality():
    return {
        "ph": round(random.uniform(6.8, 8.2),1),
        "turbidity": round(random.uniform(0.5, 4.5),1),
        "dissolved_o2": round(random.uniform(6, 9),1),
        "wqi": random.randint(78, 94),
        "status": "Excellent - Potable"
    }

def get_live_sensors():
    locations = ["Madukkarai Dam", "Siruvani Upstream", "Sector 4B Pipeline", "Coimbatore Inlet", "Perur Lake", "Irrigation Canal"]
    data = []
    for loc in locations:
        data.append({
            "id": f"S{random.randint(100,999)}",
            "location": loc,
            "ph": round(random.uniform(6.5,8.5),1),
            "turbidity": round(random.uniform(0.3,5),1),
            "flow": round(random.uniform(10,120),1),
            "temp": round(random.uniform(22,31),1),
            "status": random.choice(["Normal","Normal","Anomaly"]) if "4B" in loc else "Normal"
        })
    return data
