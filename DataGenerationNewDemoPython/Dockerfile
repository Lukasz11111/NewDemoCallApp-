# set base image (host OS)
ARG REVDEBUG_PYTHON_VERSION
FROM docker-test.revdebug.com/python-revdebug:${REVDEBUG_PYTHON_VERSION}

WORKDIR /app

RUN pip install tornado \
    pip install pyyaml \
    pip install requests

ARG REVDEBUG_HOST
ARG REVDEBUG_FORCE_TLS

ENV REVDEBUG_SOLUTION=IndexingMonthlyReports \
 REVDEBUG_APPLICATION=IndexingMonthlyReports \
 REVDEBUG_HOST=$REVDEBUG_HOST \
 REVDEBUG_APM=1 \
 REVDEBUG_MODE=Crash  \
 REVDEBUG_FORCE_TLS=$REVDEBUG_FORCE_TLS


CMD python DataGenerationNewDemoPython/app.py
