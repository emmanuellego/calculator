FROM python:2.7-slim
WORKDIR /calculator
ADD . /calculator
EXPOSE 80
ENV NAME World
CMD ["python", "calculator.py"]