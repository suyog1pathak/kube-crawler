# FROM python:3.6.14-alpine
# COPY . /app
# WORKDIR /app
# RUN python3 -m pip install -r requirements.txt
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1
# CMD [ "python3", "main.py" ]


FROM public.ecr.aws/lambda/python:3.6
COPY . ${LAMBDA_TASK_ROOT}
RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
CMD [ "main.initiate" ] 