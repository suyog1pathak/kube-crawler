FROM public.ecr.aws/lambda/python:3.6
COPY . ${LAMBDA_TASK_ROOT}
RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
CMD [ "main.initiate" ] 