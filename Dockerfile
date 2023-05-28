FROM python:3.11.3-alpine

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

RUN chmod +x ./init_env.sh
RUN ./init_env.sh

EXPOSE 3000
CMD [ "python", "-m", "uvicorn", "main:app", "--port", "3000", "--workers", "4", "--worker-class" ]
