"""
Streaming data consumer
"""
from datetime import datetime
from kafka import KafkaConsumer
from postgres import Postgres

TOPIC='tolldata'
DATABASE = 'kafka_tolldata'
USERNAME = 'farzadsharifbakhtiar'
PASSWORD = ''

print("Connecting to the database")
try:
    db = Postgres(f'postgres://{USERNAME}@localhost/{DATABASE}')
    db.run('SELECT 1 FROM livetolldata');
except Exception:
    print("Could not connect to database. Please check credentials")
    raise
else:
    print("Connected to database")

print("Connecting to Kafka")
consumer = KafkaConsumer(TOPIC)
print("Connected to Kafka")
print(f"Reading messages from the topic {TOPIC}")
for msg in consumer:

    # Extract information from kafka

    message = msg.value.decode("utf-8")

    # Transform the date format to suit the database schema
    (timestamp, vehcile_id, vehicle_type, plaza_id) = message.split(",")

    dateobj = datetime.strptime(timestamp, '%a %b %d %H:%M:%S %Y')
    timestamp = dateobj.strftime("%Y-%m-%d %H:%M:%S")

    # Loading data into the database table

    sql = "insert into livetolldata values(%(timestamp)s,%(vehicle_id)s,%(type)s,%(plaza)s)"
    result = db.run(sql, {'timestamp': timestamp,
                           'vehicle_id': vehcile_id,
                           'type':  vehicle_type,
                           'plaza': plaza_id})
    print(f"A {vehicle_type} was inserted into the database")
