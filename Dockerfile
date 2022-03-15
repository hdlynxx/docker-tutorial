FROM

ENV APP_DIR
RUN mkdir -p ${APP_DIR}
WORKDIR ${APP_DIR}

COPY 
RUN pip install -r requirements.txt

COPY 

CMD [ "python", "src/geo_locate.py"]