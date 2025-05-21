FROM python:3.11.9-slim

COPY req.txt req.txt
RUN pip install -r req.txt

COPY . .


CMD ["python", "-m", "src.main"]