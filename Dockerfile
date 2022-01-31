FROM python:3.8.10-slim as builder
# supress pip warning

SHELL ["/bin/bash", "-c"]
ADD requirements.txt /tmp
# suppress warning
ENV PATH=$PATH:/root/.local/bin

RUN apt-get -y update \
    && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    && pip install --user -r /tmp/requirements.txt

FROM python:3.8.10-slim as app
LABEL maintener="Xavier Petit <nuxion@gmail.com>"
RUN groupadd app -g 1000 \
    && useradd -m -d /home/app app -u 1000 -g 1000 \
    && apt-get update -y  \
    && apt-get install -y --no-install-recommends \
    ssh openssh-client rsync libopenblas-base
COPY --from=builder --chown=app:app /root/.local /home/app/.local/
COPY --chown=app:app . /app

USER app
WORKDIR /app
ENV PATH=$PATH:/home/app/.local/bin
ENV PYTHONPATH=/app
# RUN python /app/setup.py install --user
# CMD ["python3", "run.py"]
