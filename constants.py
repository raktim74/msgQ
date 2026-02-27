class Constants:
    TOPIC = "data-stream"
    TOPIC2 = "data-stream-2"
    GROUP_ID = "group-data-stream"
    DATA_DIR = "./msgQ_data"
    MAX_MESSAGES = 1 #No of messages per set; value cannot be 0
    NO_OF_PARTITION = 2 #Define how many partitions you want
    DEFAULT_MESSAGES = 10 #Default no of messages to be read; value cannot be 0
    DEFAULT_PARTITION = 0 #Default partition
