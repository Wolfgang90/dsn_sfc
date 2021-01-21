import producer_server
import json


def run_kafka_server():
	# TODO get the json file path
    input_file = "./police-department-calls-for-service.json"
    
    value_serializer = lambda x:json.dumps(x).encode('utf-8')

    # TODO fill in blanks
    producer = producer_server.ProducerServer(
        input_file=input_file,
        topic="dsn.sfc.policecalls",
        bootstrap_servers="localhost:9092",
        client_id="dsn.sfc.broker",
        #value_serializer=value_serializer
    )

    return producer


def feed():
    producer = run_kafka_server()
    producer.generate_data()


if __name__ == "__main__":
    feed()
