import json
from kafka import KafkaConsumer
from Schema import UserSchema
from mail import Mail


# Kafka Consumer
consumer = KafkaConsumer(
    ['send_mail', ],
    bootstrap_servers='localhost:9092',
)

for message in consumer:
    data = UserSchema().dump(message)
    email = data['mail']
    text_template = data['text']
    subject = data['subject']
    mail = Mail(email, subject, text_template)
    result = mail.send_mail()
