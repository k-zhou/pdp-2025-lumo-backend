# https://www.geeksforgeeks.org/python/setting-up-docker-for-python-projects-a-step-by-step-guide/

FROM python:3.14-slim-bookworm

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

# --no-cache-dir
# should I keep it or not?
# https://stackoverflow.com/questions/45594707/what-is-pips-no-cache-dir-good-for

# Port number
EXPOSE 5000

CMD [ "flask", "--app", "app.py", "run", "--host=0.0.0.0" ]