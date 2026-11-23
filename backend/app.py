# Import necessary libraries
import joblib
import pandas as pd
from flask import Flask, jsonify, request

# Initialize Flask app and load the trained model from the container image.
superkart_api = Flask("SuperKart")
model = joblib.load("superkart_model.joblib")


@superkart_api.get("/")
def home():
    return "Welcome to the SuperKart System"


@superkart_api.post("/v1/predict")
def predict_sales():
    data = request.get_json()
    feature_names = [
        "Product_Weight",
        "Product_Sugar_Content",
        "Product_Allocated_Area",
        "Product_MRP",
        "Store_Size",
        "Store_Location_City_Type",
        "Store_Type",
        "Product_Id_char",
        "Store_Age_Years",
        "Product_Type_Category",
    ]
    input_data = pd.DataFrame([{name: data[name] for name in feature_names}])
    prediction = model.predict(input_data).tolist()[0]
    return jsonify({"Sales": prediction})


@superkart_api.post("/v1/predictbatch")
def predict_sales_batch():
    uploaded_file = request.files["file"]
    input_data = pd.read_csv(uploaded_file)
    predictions = model.predict(input_data).tolist()
    return jsonify({str(index): round(prediction, 2) for index, prediction in enumerate(predictions)})


if __name__ == "__main__":
    superkart_api.run(host="0.0.0.0", port=7860)
