from kafka import KafkaProducer
import json
import time


class ProducerServer(KafkaProducer):

    def __init__(self, input_file, topic, **kwargs):
        super().__init__(**kwargs)
        self.input_file = input_file
        self.topic = topic

    #TODO we're generating a dummy data
    def generate_data(self):        
        with open(self.input_file) as f:
            json_data = json.load(f)
            for data_item in json_data:
                # Alternatively one could implement value_serializer as class input in kafka_server.py
                message = self.dict_to_binary(data_item)
                print(type(message))
                # TODO send the correct data
                self.send(self.topic, value=message)
                #test = self.send(self.topic, value=data_item)
                #print(test.get().value)
                time.sleep(1)

    # TODO fill this in to return the json dictionary to binary
    def dict_to_binary(self, json_dict):
        return json.dumps(json_dict).encode('utf8')
        