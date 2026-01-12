from fastapi import FastAPI

app = FastAPI(title="BMI Calculator API")

@app.get("/health", tags=["Health"])
def health_check():
    """
    Simple health check endpoint to test connectivity.
    """
    return {
        "status": "ok",
        "message": "API is up and running"
    }

@app.get("/")
def root():
    return {"message": "Welcome to BMI Calculator API"}

@app.post("/bmi")
def calculate_bmi(weight: float, height: float):
    """
    weight: in kilograms
    height: in meters
    """
    if weight <= 0 or height <= 0:
        return {
            "error": "Weight and height must be greater than zero"
        }

    bmi = weight / (height ** 2)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    return {
        "weight": weight,
        "height": height,
        "bmi": round(bmi, 2),
        "category": category
    }
