# Stream_Keyword_Detection

This project listens to a Kafka stream, processes incoming text messages, and detects the presence of predefined keywords in each message. It utilizes the `kafka-python` library to connect to Kafka and a custom function to count keyword occurrences.

## Features

- **Kafka Consumer**: Reads messages from a Kafka stream (`text_stream` topic).
- **Keyword Detection**: Detects predefined keywords in the incoming text.
- **Real-time Processing**: Continuously listens for and processes messages from Kafka.

## Requirements

- Kafka (running locally or on a remote server)
- Python 3.x
- Required Python libraries:
  - `kafka-python`
  - `collections`

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/kafka-text-stream-processor.git
