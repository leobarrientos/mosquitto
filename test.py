"""
MQTT subscriber for debugging/testing
"""
import logging
import ssl
import paho.mqtt.client as mqtt


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
consolehandler = logging.StreamHandler()
consolehandler.setFormatter(logging.Formatter("%(levelname)s - %(message)s"))
logger.addHandler(consolehandler)

client = mqtt.Client("test", protocol=mqtt.MQTTv5)
client.tls_set(
    ca_certs="./certs/CAleobarrientos.pem",
    certfile="./certs/asgard.pem",
    keyfile="./certs/asgard.private.pem",
    cert_reqs=ssl.CERT_REQUIRED,
    tls_version=ssl.PROTOCOL_TLS,
    ciphers=None,
)
client.enable_logger(logger)


def on_connect(client, userdata, flags, rc, properties=None):
    logger.info("Connected with result: %s", rc)
    if rc != 0:
        logger.error("Failed to connect (%s %s %s)", userdata, flags, properties)

client.username_pw_set(username="lbarrientos",password="leo1876")

client.on_connect = on_connect
client.connect("asgard", 8883, 60)
client.loop_forever()
