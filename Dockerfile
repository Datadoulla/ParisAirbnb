FROM python:3.10.13-slim
WORKDIR .
COPY requirements.txt ./ 
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
WORKDIR ./src
EXPOSE $PORT
CMD ["python", "model_api.py"]