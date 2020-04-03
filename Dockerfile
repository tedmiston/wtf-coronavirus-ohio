FROM python:3.8.2-slim@sha256:c0281d8fe99edff517fcc748f088bc51822ae660bac9e4aba76a81fa987fe9e8

WORKDIR /usr/src/app

RUN pip install --upgrade pip
RUN pip install requests-html==0.10.0

COPY . .

CMD [ "python", "app.py" ]
