from confluent_kafka import Producer
import json , uuid
import os

# 1. Configuration

broker = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')

conf = {
    'bootstrap.servers': broker,
    'client.id': 'order-service'
}

# 2. Create Producer Instance (lowercase 'p')
producer = Producer(conf)

def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

# 3. Simulate sending an order
order_data = {
    "order_id": str(uuid.uuid4()),
    "user_id": "sk_ali",
    "item": "Laptop",
    "quantity": 1,
    "status": "created"
}

print("Sending order...")
# Convert dict to JSON string, then to bytes
producer.produce(
    'orders', 
    key=str(order_data["order_id"]), 
    value=json.dumps(order_data).encode('utf-8'), 
    callback=delivery_report
)

# 4. Flush to ensure the message is actually sent before script ends
producer.flush()