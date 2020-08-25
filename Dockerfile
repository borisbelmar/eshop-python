FROM python:alpine
COPY [".", "/app"]
WORKDIR /app
RUN apk add --update musl-dev gcc libffi-dev
RUN pip install pipenv && pipenv sync
ENV FLASK_APP=run.py
CMD ["pipenv", "run", "flask", "run", "--host", "0.0.0.0"]