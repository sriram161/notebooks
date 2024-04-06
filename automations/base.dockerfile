from python:latest

RUN curl -sSL https://sdk.cloud.google.com > /tmp/gcl && bash /tmp/gcl --install-dir=/usr/local/bin --disable-prompts && pip install --upgrade pip
ENV PATH="$PATH:/usr/local/google-cloud-sdk/bin"
RUN pip install tensorflow-serving-api
RUN pip install --no-cache-dir -r requirements.txt