from dataclasses import dataclass
from typing import Optional, List, Dict
from topic import Topic
from constants import Constants as C

@dataclass
class Message:
    key: Optional[str]
    value: str
    timestamp: float
    partition: int
    offset: int

class Settings:
    def __init__(self, data_dir: str = C.DATA_DIR):
        self.topics: Dict[str, Topic] = {}
        self.data_dir = data_dir
        self.consumer_offsets: Dict[str, Dict[str, int]] = {}
        
    def create_topic(self, topic_name: str, num_partitions: int = C.NO_OF_PARTITION):
        """
            Create the topic
        """
        if topic_name in self.topics:
            raise ValueError(f"Topic {topic_name} already exists")
        self.topics[topic_name] = Topic(topic_name, num_partitions, self.data_dir)
    
    def produce(self, topic: str, key: Optional[str], value: str) -> Dict:
        """
            Produce message to topic
        """
        self.topics[topic] = Topic(topic, C.NO_OF_PARTITION, self.data_dir)
        if topic not in self.topics:
            raise ValueError(f"Topic {topic} does not exist")
        
        partition = self.topics[topic].get_partition(key)
        offset = partition.append(key, value)
        
        return {"topic": topic, "partition": partition.partition_id, "offset": offset}
    
    
    def consume(self, topic: str, group_id: str, partition_id: int = C.DEFAULT_PARTITION, max_messages: int = C.MAX_MESSAGES) -> List[Message]:
        """
            Consume the messages from the topic
        """
        self.topics[topic] = Topic(topic, C.NO_OF_PARTITION, self.data_dir)
        if topic not in self.topics:
            raise ValueError(f"Topic {topic} does not exist")
            return []
    
        partition = self.topics[topic].partitions[partition_id]
        
        # Get or initialize offset for this group/partition
        if group_id not in self.consumer_offsets:
            self.consumer_offsets[group_id] = {}
        if topic not in self.consumer_offsets[group_id]:
            self.consumer_offsets[group_id][topic] = {}
        if partition_id not in self.consumer_offsets[group_id][topic]:
            self.consumer_offsets[group_id][topic][partition_id] = 0
        
        offset = self.consumer_offsets[group_id][topic][partition_id]
        messages = partition.read(offset, max_messages)
        
        # Update offset
        new_offset = offset + len(messages)
        self.consumer_offsets[group_id][topic][partition_id] = new_offset 
        
        return messages

Settings().create_topic(C.TOPIC, C.NO_OF_PARTITION) #Create the topic