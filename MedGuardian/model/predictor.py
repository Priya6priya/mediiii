import random

def predict_outbreak(data):
    trend = {
        "dates": ["Day 1", "Day 2", "Day 3", "Day 4"],
        "values": [random.uniform(0.1, 0.9) for _ in range(4)]
    }
    alerts = {
        "Asia": "High",
        "Europe": "Moderate",
        "US": "Low"
    }
    return {"trend": trend, "alerts": alerts}