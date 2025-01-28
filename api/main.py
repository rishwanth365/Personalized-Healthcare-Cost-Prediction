from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import pandas as pd

# Load the saved model
model = joblib.load("model/healthcare_cost_model.pkl")

# Initialize FastAPI app
app = FastAPI()

# Enable CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins. Replace with a specific domain for production.
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

# Define the input data schema using Pydantic
class InputData(BaseModel):
    age: int
    sex: str  # "male" or "female"
    bmi: float
    children: int
    smoker: str  # "yes" or "no"
    region: str  # "northeast", "northwest", "southeast", "southwest"


@app.post("/predict")
def predict_charges(data: InputData):
    # Define encoding maps
    sex_category = {"female": 0, "male": 1}
    smoker_category = {"no": 0, "yes": 1}
    region_category = {"northeast": 0, "northwest": 1, "southeast": 2, "southwest": 3}

    # Transform categorical features to numeric values
    sex = sex_category[data.sex.lower()]
    smoker = smoker_category[data.smoker.lower()]
    region = region_category[data.region.lower()]

    # Prepare input array with feature names
    input_features = pd.DataFrame([{
        "age": data.age,
        "sex": sex,
        "bmi": data.bmi,
        "children": data.children,
        "smoker": smoker,
        "region": region
    }])

    # Make prediction
    prediction = model.predict(input_features)[0]

    return {"predicted_charges": round(prediction, 2)}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)