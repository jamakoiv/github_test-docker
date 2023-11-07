FROM debian:bookworm-slim

RUN apt-get update && apt-get 
RUN pip --no-input install pyyaml

ENV PYTHONUNBUFFERED=x
CMD [python main.py]