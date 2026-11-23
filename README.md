# SuperKart Sales Prediction

XGBoost sales-forecast model served by a Flask API (port 7860) with a Streamlit UI (port 8501).

## Run in a GitHub Codespace
```bash
cd backend  && docker build -t superkart-backend .  && cd ..
cd frontend && docker build -t superkart-frontend . && cd ..
docker network create superkart-net
docker run -d --name backend  --network superkart-net -p 7860:7860 superkart-backend
docker run -d --name frontend --network superkart-net -p 8501:8501 superkart-frontend
```
Then open the **Ports** tab, set port **7860** (and 8501) to **Public**, and copy the forwarded address for 7860.

## Test the API
```bash
curl https://<your-codespace>-7860.app.github.dev/
```
Endpoints: `POST /v1/predict` (JSON) and `POST /v1/predictbatch` (CSV file under key `file`).
