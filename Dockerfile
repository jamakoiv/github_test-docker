FROM debian:bookworm-slim

RUN apt-get update -y &&    \
    apt-get install -y procps python3 python3-yaml

# No pip in basic image.
# RUN  pip --no-input install pyyaml 

# Copy local src-folder to /src in container.
COPY src /src
WORKDIR /src

ENV PYTHONUNBUFFERED=x
CMD ["python3", "main.py", "-v"]