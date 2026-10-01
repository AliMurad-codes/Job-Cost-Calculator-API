from fastapi import FastAPI
from pydantic import BaseModel

from decorators import log_execution, measure_time


app = FastAPI(
    title="Job Cost Calculator API",
    description="Mini project demonstrating Python decorators",
    version="1.0.0"
)


# --------------------------------
# Request Model
# --------------------------------

class JobCostRequest(BaseModel):
    hours: float
    hourly_rate: float
    parts: float


# --------------------------------
# Business Logic
# --------------------------------

@log_execution
@measure_time
def calculate_job_cost(hours, hourly_rate, parts):

    labor = hours * hourly_rate

    total = labor + parts

    return {
        "labor": labor,
        "parts": parts,
        "total": total
    }


# --------------------------------
# API Endpoint
# --------------------------------

@app.post("/jobs/calculate-cost")
def calculate_cost(request: JobCostRequest):

    result = calculate_job_cost(
        request.hours,
        request.hourly_rate,
        request.parts
    )

    return result