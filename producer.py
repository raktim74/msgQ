from typing import Optional, Dict
from partition import Partition 
import threading
import time
import uuid
from settings import Settings
from constants import Constants as C

class Producer:
    def __init__(self, topic: str, data_dir: str = C.DATA_DIR):
        self.topic = topic
        self.data_dir = data_dir
        self.partition = Partition(topic, C.DEFAULT_PARTITION, data_dir)
        self.topics = {topic: self.partition}
    
    
    def producer_trigger(self):
        """
            Trigger the producer to produce messages
        """
        for i in range(5):
            msg_id = str(uuid.uuid4())
            result = Settings().produce(self.topic, msg_id, f"Message {i}: Hello brother, I heard there are some discussion going on in the other topic!")
            print(f"Produced: {result}")
            time.sleep(1)

def run_producer():
    """
        Run the producer
    """
    producer = Producer(C.TOPIC2)
    producer.producer_trigger()


try:
    producer_thread = threading.Thread(target=run_producer)
    producer_thread.start()
    print("Main thread continues...")
    producer_thread.join() 
    print("Thread finished!")
except Exception as e:
    print(f"Error: {e}")
