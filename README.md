<img src="https://github.com/raktim74/msgQ/blob/master/img/msgQ_logo.png" alt="Logo" width="400" height="400">

# msgQ - A Lite Message Queue

msgQ is a simple and lightweight message queue implementation in Python. It provides a basic message queue system with the following features:

- Create topics
- Produce messages to topics
- Consume messages from topics
- Support for partitioning
- Support for message offset tracking
- Support for message persistence


## Run Locally

Clone the project
```bash
  git clone https://github.com/raktim74/msgQ.git
```

Install dependencies
```bash
  pip install -r requirements.txt
```
Start the producer
```bash
  python3 producer.py
```
Start the consumer(s)
```bash
  python3 consumer1.py, consumer2.py, ....
```
Create the topic (optional)
```bash
  python3 settings.py
```
- Create a folder msgQ_data in the root directory
- Use constants.py to change the values
- Modify the consumer1, consumer2, ... etc and producer (topic name) to test for multiple topics

## How it works?

![Diagram](https://github.com/raktim74/msgQ/blob/master/img/draw.io/msgQ.svg)


## Authors

- [@raktim74](https://www.github.com/raktim74) Raktim Nath

## License

[MIT](https://choosealicense.com/licenses/mit/)
