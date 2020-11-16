FROM eclipse-mosquitto:latest

COPY config /mosquitto/config
RUN chown -R mosquitto:mosquitto /mosquitto
#VOLUME ["/mosquitto/config", "/mosquitto/data", "/mosquitto/log"]

EXPOSE 1883

CMD ["/usr/sbin/mosquitto", "-c", "/mosquitto/config/mosquitto.conf"]
