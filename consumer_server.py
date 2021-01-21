from kafka import KafkaConsumer
import time


class ConsumerServer(KafkaConsumer):
    def __init__(self, topic, **kwargs):
        super().__init__(**kwargs)
        self.topic = topic
        self.consumer = KafkaConsumer(
                        bootstrap_servers="localhost:9092",
                        request_timeout_ms = 1000, 
                        auto_offset_reset="earliest", 
                        max_poll_records=10
        )
        self.consumer.subscribe(topics=self.topic)
        
    def consume_data(self):
        try:
            while True:
                for metadata, list_records in self.consumer.poll().items():
                    for record in list_records:
                        if record:
                            print(record.value)
                        else:
                            pass
            time.sleep(0.5)
        except:
            print("Error: Consumer is closed")
            self.consumer.close()       
        
def consume_kafka_data(topic="dsn.sfc.policecalls"):
    #topic = "test.topic"
    consumer = ConsumerServer(topic=topic)
    consumer.consume_data()

if __name__=='__main__':
    consume_kafka_data()
    
    

        
