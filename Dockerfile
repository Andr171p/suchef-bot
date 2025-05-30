FROM python:3.11

WORKDIR /suchef_bot

COPY requirements.txt .

RUN  pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["/bin/bash", "-c", "python main.py"]