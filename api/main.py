from fastapi import FastAPI
from api.schemas import ChatRequest, ROIRequest, FlightRequest, ComplianceRequest

from rag.retriever import retrieve_answer
from mcp_server.roi_calculator import calculate_roi
from mcp_server.flight_time_estimator import estimate_flight_time
from mcp_server.compliance_checker import check_compliance

app = FastAPI(title="Drone Intelligence System API")

@app.get("/")
def root():
    return {"status": "Drone Intelligence API running"}

# ---------------- RAG CHAT ----------------
@app.post("/chat")
def chat(req: ChatRequest):
    result = retrieve_answer(req.question)

    # If retriever returns only text
    if isinstance(result, str):
        return {
            "answer": result,
            "source": "RAG Knowledge Base"
        }

    # If retriever already returns dict
    return result


# ---------------- MCP TOOLS ----------------
@app.post("/roi")
def roi(req: ROIRequest):
    return {
        "result": calculate_roi(req.farm_size_acres)
    }

@app.post("/flight-time")
def flight_time(req: FlightRequest):
    return {
        "result": estimate_flight_time(
            req.battery_percent,
            req.battery_capacity_ah,
            req.motors,
            req.motor_current_a
        )
    }


@app.post("/compliance")
def compliance(req: ComplianceRequest):
    return {
        "result": check_compliance(req.drone_weight_kg, req.zone)
    }

