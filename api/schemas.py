from pydantic import BaseModel

class ChatRequest(BaseModel):
    question: str

class ROIRequest(BaseModel):
    farm_size_acres: int

class FlightRequest(BaseModel):
    battery_percent: int
    battery_capacity_ah: float
    motors: int
    motor_current_a: float

class ComplianceRequest(BaseModel):
    drone_weight_kg: float
    zone: str
