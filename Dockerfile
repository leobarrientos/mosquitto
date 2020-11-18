FROM eclipse-mosquitto:latest

RUN mkdir /mosquitto/certs
COPY config /mosquitto/config
COPY certs /mosquitto/certs

RUN chown -R mosquitto:mosquitto /mosquitto
#VOLUME ["/mosquitto/config", "/mosquitto/data", "/mosquitto/log"]

EXPOSE 1883 8883

CMD ["/usr/sbin/mosquitto", "-c", "/mosquitto/config/mosquitto.conf"]
