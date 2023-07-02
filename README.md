# Processing Streaming Data via Apache Kafka
## Installation
**Prerequisites:**  
1. A postgres installation
  - With Database 'kafka\_tolldata'
  - And table 'livetolldata'
**Python Requirements:**
```
$ python -m pip install -r requirements.txt
```
**Download and extract Kafka:**
```
$ wget https://archive.apache.org/dist/kafka/2.8.0/kafka_2.12-2.8.0.tgz
$ tar --extract --file kafka_2.12-2.8.0.tgz;
```
**Run Zookeeper:**
```
$ ./kafka_2.12-2.8.0/bin/zookeeper-start-server.sh ./kafka_2.12-2.8.0/config/zookeeper.properties
```
**Run Kafka broker:**
```
$ ./kafka_2.12-2.8.0/kafka-server-start.sh ./kafka_2.12-2.8.0/server.properties
```
## Running
### Producer
```
$ python toll_traffic_generator.py
```
This generates a random stream of random tolldata.
### Consumer
```
$ python streaming_data_reader.py
```
The consumer consumes the data from `toll_data_traffic_generator` and writes
them to the "livetolldata" table. Verify this by checking `SELECT max(timestamp) FROM livetolldata;` in postgres periodically.

