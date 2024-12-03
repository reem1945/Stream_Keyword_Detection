from kafka import KafkaProducer
import time

# Initialisation du producteur Kafka
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Fonction pour envoyer du texte vers Kafka
def send_text_to_kafka(text):
    producer.send('text_stream', value=text.encode('utf-8'))
    producer.flush()
    print(f"Texte envoyé à Kafka: {text}")

if __name__ == "__main__":
    # Exemple de texte
    text = "Ceci est un exemple de flux de texte à analyser pour les mots-clés."
    
    # Envoi du message
    send_text_to_kafka(text)

    # Si tu veux envoyer plusieurs messages en boucle, tu peux faire :
    # while True:
    #     text = get_new_text()  # Remplace par un flux réel
    #     send_text_to_kafka(text)
    #     time.sleep(1)  # Attendre avant d'envoyer un nouveau message
