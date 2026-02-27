from partition import Partition
from settings import Settings
import time
from constants import Constants as C

class Consumer3:
    def __init__(self, topic: str, group_id: str, data_dir: str = C.DATA_DIR):
        self.topic = topic
        self.group_id = group_id
        self.data_dir = data_dir
        self.settings = Settings()
    
    def consumer_trigger(self):
        """
            Read messages from the topic
        """
        while True:
            messages = self.settings.consume(self.topic, self.group_id, max_messages=C.MAX_MESSAGES)
            for msg in messages:
                print(f"Consumed: {msg.value} (offset: {msg.offset})")
            if not messages:
                time.sleep(2)
            else:
                time.sleep(0.5)

Consumer3(C.TOPIC2, C.GROUP_ID).consumer_trigger() #Call the consumer trigger