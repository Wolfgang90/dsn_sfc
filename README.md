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

### kafka-consumer-console output
![alt text](https://github.com/Wolfgang90/dsn_sfc/blob/main/images/cli_consumer_screenshot.PNG "kafka-consumer-console output")

### spark UI
![alt text](https://github.com/Wolfgang90/dsn_sfc/blob/main/images/spark_ui.PNG "spark UI")

### progress reporter
![alt text](https://github.com/Wolfgang90/dsn_sfc/blob/main/images/micro_batch_screenshot1.PNG "progress reporter")
![alt text](https://github.com/Wolfgang90/dsn_sfc/blob/main/images/micro_batch_screenshot2.PNG "progress reporter")

## Project questions
1) How did changing values on the SparkSession property parameters affect the throughput and latency of the data?
*`maxOffsetsPerTrigger` limits the offsets processed per trigger interval to a maximum number (initially unlimited). One can see the effect of amending `maxOffsetsPerTrigger` in `processedRowsPerSecond`.* 

2) What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?
*Setting the `maxOffsetsPerTrigger` can improve efficiencies. I received good results with `maxOffsetsPerTrigger`=10. However, with more resources available this number could be increased to achieve better results.*
