FROM projectriff/python3-function-invoker:latest
ARG FUNCTION_MODULE=sentiments.py
ARG FUNCTION_HANDLER=process
ADD ./sentiments.py /
ADD ./requirements.txt /
RUN  pip install --upgrade pip && pip install -r /requirements.txt
ENV FUNCTION_URI file:///${FUNCTION_MODULE}?handler=${FUNCTION_HANDLER}
