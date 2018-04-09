FROM alpine

RUN apk update && apk upgrade
RUN apk add curl
RUN apk add nodejs

RUN apk add python2

RUN curl https://dl.google.com/dl/cloudsdk/release/google-cloud-sdk.tar.gz > /tmp/google-cloud-sdk.tar.gz
RUN mkdir -p /usr/local/gcloud
RUN tar -C /usr/local/gcloud -xvf /tmp/google-cloud-sdk.tar.gz
RUN /usr/local/gcloud/google-cloud-sdk/install.sh
ENV PATH $PATH:/usr/local/gcloud/google-cloud-sdk/bin

RUN apk add ffmpeg

WORKDIR /app

COPY app.js .
COPY app.yaml .
COPY package.json .
COPY test01.flac .

RUN npm install

ENTRYPOINT [ "npm", "start" ]
