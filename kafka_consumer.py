from kafka import KafkaConsumer
from keyword_detection import count_keywords  # Importer la fonction de comptage des mots-clés

# Initialisation du consommateur Kafka
consumer = KafkaConsumer('text_stream', bootstrap_servers='localhost:9092', group_id='text_group')

# Liste des mots-clés à détecter
keywords = ["data science", "python", "MLops"]

# Fonction pour traiter chaque message
def process_message(text):
    print(f"Texte reçu : {text}")
    keyword_count = count_keywords(text, keywords)
    print(f"Mots-clés détectés: {keyword_count}")

if __name__ == "__main__":
    # Lire et traiter chaque message de Kafka
    for message in consumer:
        text = message.value.decode('utf-8')
        process_message(text)
