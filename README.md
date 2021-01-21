# SF Crime Statistics with Spark Streaming
(Udacity Datastreaming Nanodegree - Project 2)

## How to run the project
(Commands for starting up code in Udacity workspace or a Python conda environment (not tested))

### Initialize infrastructure (environment and kafka)

1) Open console and run `./start.sh` to setup environment.

2) Run

``` 
$ cd config
$ /usr/bin/zookeeper-server-start zookeeper.properties
```
to initialize zookeeper.

3) Open new console and run 
``` 
$ cd config
$ /usr/bin/kafka-server-start server.properties
```
to initialize kafka.

### Start and testkafka producer
4) Open new console and run `python kafka_server.py` to start kafka producer.
5) Open new console and run `python consumer_server.py` to test kafka producer with a kafka consumer.

### Start spark streaming
6) Open new console and run
```
$ spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.3.4 --master local[*] data_stream.py
```
to customize and start a spark streaming session.

## Output screenshots
(as requested by Udacity in project requirements)
