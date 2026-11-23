# SuperKart Sales Prediction

XGBoost sales-forecast model served by a Flask API on port 7860, with a Streamlit UI on port 8501.

## Run in a GitHub Codespace

Run these commands from the repository root in the Codespace terminal:

```bash
docker build -f backend/Dockerfile -t superkart-backend .
docker build -f frontend/Dockerfile -t superkart-frontend .
docker network create superkart-net
docker run -d --name backend --network superkart-net -p 7860:7860 superkart-backend
docker run -d --name frontend --network superkart-net -p 8501:8501 superkart-frontend
```

In the **Ports** tab, set ports **7860** and **8501** to **Public**. Once the containers are running, Codespaces will show forwarded addresses for both ports. Open port 7860 to check for `Welcome to the SuperKart System`; open port 8501 for the Streamlit app.

## Test the API

```bash
curl https://<your-codespace>-7860.app.github.dev/
```

Endpoints: `POST /v1/predict` (JSON) and `POST /v1/predictbatch` (CSV file under key `file`).
