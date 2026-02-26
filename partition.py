from pathlib import Path
import json
import time
from typing import Optional, List
from dataclasses import dataclass
from constants import Constants as C


@dataclass
class Message:
    key: Optional[str]
    value: str
    timestamp: float
    partition: int
    offset: int

class Partition:
    def __init__(self, topic: str, partition_id: int, data_dir: str = C.DATA_DIR):
        self.topic = topic
        self.partition_id = partition_id
        self.path = Path(data_dir) / topic / f"partition-{partition_id}.log"
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._messages: List[Message] = []
        self._load_messages()
    
    def _load_messages(self):
        """
            Load existing messages from disk
        """
        if self.path.exists():
            with open(self.path, 'r') as f:
                for line in f:
                    try:
                        msg_data = json.loads(line.strip())
                        self._messages.append(Message(**msg_data))
                    except:
                        continue
    
    def append(self, key: Optional[str], value: str) -> int:
        """
            Append message and return offset
        """
        offset = len(self._messages)
        msg = Message(
            key=key,
            value=value,
            timestamp=time.time(),
            partition=self.partition_id,
            offset=offset
        )
        self._messages.append(msg)
        
        # Persist to disk
        with open(self.path, 'a') as f:
            f.write(json.dumps(msg.__dict__) + '\n')
        
        return offset
    
    def read(self, offset: int, max_messages: int = C.DEFAULT_MESSAGES) -> List[Message]:
        """
            Read messages from the offset
        """
        return self._messages[offset:offset + max_messages]