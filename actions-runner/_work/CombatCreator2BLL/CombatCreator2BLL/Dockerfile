FROM python:3.11-slim

WORKDIR /CombatCreator

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONPATH=/CombatCreator

EXPOSE 5000

CMD ["python", "combat_creator_1api/app.py"]