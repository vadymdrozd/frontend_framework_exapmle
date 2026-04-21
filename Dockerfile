FROM python

# COPY ./allurereport /app/allurereport/
COPY ./ /app/

WORKDIR /app
RUN python3 -m venv venv \
    && bash ./activation.sh

ENTRYPOINT ["bash", "/app/entrypoint.sh"]
