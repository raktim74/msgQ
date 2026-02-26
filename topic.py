from typing import Optional, List
from partition import Partition
from constants import Constants as C

class Topic:
    def __init__(self, topic_name: str, num_partitions: int = C.NO_OF_PARTITION, data_dir: str = C.DATA_DIR):
        self.topic_name = topic_name
        self.partitions = [Partition(topic_name, i, data_dir) for i in range(num_partitions)]
        self.num_partitions = num_partitions
    
    def get_partition(self, key: Optional[str] = None) -> Partition:
        """
            Hash-based partitioning
        """
        if key:
            partition_id = hash(key) % self.num_partitions
        else:
            partition_id = C.DEFAULT_PARTITION
        return self.partitions[partition_id]