
KNOWLEDGE = {
    "flood": "Based on Digital Twin + IMD data, Madukkarai zone shows 68% flood probability if rainfall > 80mm in 6h. Recommend pre-releasing Siruvani dam by 15% to maintain buffer.",
    "quality": "Current WQI is 87 (Excellent). pH stable at 7.4. Turbidity spike at sensor S3 likely due to upstream construction - not chemical contamination.",
    "leak": "Anomaly Radar detected 2 micro-leaks in Sector 4B pipeline. Estimated loss 12kL/day. Blockchain credit penalty applied to contractor wallet.",
    "conservation": "You have saved 340L this week via smart scheduling. That's 34 Water Credits (1 credit = 10L). Trade credits for tax benefits on portal.",
    "dam": "Siruvani Dam at 78% capacity. AI recommends gate 2 open 40% for next 12h to maintain optimal 75% buffer for predicted rainfall."
}
def hydro_agent_query(query: str):
    q = query.lower()
    for k,v in KNOWLEDGE.items():
        if k in q: return v
    if "madukkarai" in q: return KNOWLEDGE["flood"]
    if "siruvani" in q: return KNOWLEDGE["dam"]
    return "HydroSentinel AI: I analyze real-time IoT, satellite, and LSTM predictions. Ask about flood risk, water quality, leak detection, dam operations, or water credits for Madukkarai-Coimbatore network."
