FROM python:3.9-slim
WORKDIR /app

# The build context is the repository root, so include the model stored there.
COPY backend/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY backend/app.py ./app.py
COPY superkart_model.joblib ./superkart_model.joblib

EXPOSE 7860
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:7860", "app:superkart_api"]
