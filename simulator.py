
import random
class DigitalTwinSimulator:
    def __init__(self):
        self.level = 45.0
        self.particles = [{"x": random.random(), "y": random.random(), "v": random.uniform(1,3)} for _ in range(100)]
    def step(self, rainfall, dam_gate):
        inflow = rainfall * 0.9
        outflow = dam_gate * 0.7
        self.level = max(0, self.level + (inflow - outflow)*0.1 + random.uniform(-0.5,0.5))
        for p in self.particles:
            p["x"] += p["v"]*0.02 * (1 + rainfall/100)
            if p["x"] > 1: p["x"] = 0
        return {"level": round(self.level,2), "particles": len(self.particles), "flow_rate": round(inflow,2)}
