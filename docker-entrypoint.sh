#!/bin/bash

if [ ${APP_DEBUG}="1" ]
then
  uvicorn main:app --reload --host ${APP_HOST} --port ${APP_PORT} --workers 1
else
  gunicorn main:app --reload --bind ${APP_HOST}:${APP_PORT} -k uvicorn.workers.UvicornWorker --threads ${APP_N_THREADS}
fi