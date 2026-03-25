from confluent_kafka import Consumer, KafkaError
import json
import os

broker = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')

conf = {
    'bootstrap.servers': broker,
    'group.id': 'order_tracker',
    'auto.offset.reset': 'earliest',
}

consumer = Consumer(conf)
consumer.subscribe(['orders'])

print('Order Tracker running... (Ctrl+C to stop)')

try:
    while True:
        # 1. Poll and check if message exists
        if (msg := consumer.poll(1.0)) is None:
            continue

        # 2. Handle Errors (Captures the error object in 'err')
        if (err := msg.error()):
            if err.code() != KafkaError._PARTITION_EOF:
                print(f"Consumer error: {err}")
            continue

        # 3. Process Value safely
        if (val := msg.value()):
            try:
                order = json.loads(val.decode('utf-8'))
                print(f"TRACKER: Order #{order.get('order_id')} | Status: {order.get('status')}")
            except (json.JSONDecodeError, UnicodeDecodeError):
                print("Skipping malformed message")
        else:
            print("Received tombstone (empty) message")

except KeyboardInterrupt:  # Graceful shutdown on Ctrl+C i.e keyboard interrupt
    print ("Shutting down Order Tracker...")

finally:
    consumer.close()  #close consumer to commit final offsets and clean up resources