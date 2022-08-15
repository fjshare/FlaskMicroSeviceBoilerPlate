# FROM 3.10.6-windowsservercore-1809 as base
# ARG POSTGRES_ENABLED=0

# RUN mkdir /app
# WORKDIR /app

# COPY requirements.txt requirements.txt

# RUN pip install --no-cache-dir -r requirements.txt

# COPY --chown=web:web ./docker/entrypoint.sh /usr/local/bin/entrypoint.sh
# RUN chmod +x /usr/local/bin/entrypoint.sh
# USER web
# ENTRYPOINT ["entrypoint.sh"]

# FROM base as dev
# WORKDIR /app
# COPY --from=build /app .
# ADD . /app

FROM python:3 as base

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# ENV POSTGRES_ENABLED $POSTGRES_ENABLED

# WORKDIR /usr/src/app

# COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt

# COPY . .

# CMD ["python", "run.py"]

RUN mkdir /src

WORKDIR /src

ADD requirements.txt /src

RUN \
    # Install curl
    # apk add --no-cache curl && \
    # Install postgres utilities which are required by `psycopg2` lib being used by app
    # apk add --no-cache postgresql-libs && \
    # apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
    # Install Python packages required by the app
    pip install --no-cache-dir -r requirements.txt 
    # apk --purge del .build-deps

ADD ./ /src

COPY . .

EXPOSE 5000

CMD ["python", "run.py", "flask", "run", "-h", "0.0.0.0", "-p", "5000"]