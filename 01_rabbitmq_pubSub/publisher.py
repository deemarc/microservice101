import pika, json

from pika import credentials
import sys
import json
# params = pika.URLParameters('amqps://admin:mypass@localhost')

# connection = pika.BlockingConnection(params)
credentials = pika.PlainCredentials('admin', 'mypass')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost',credentials=credentials))

channel = connection.channel()

channel.exchange_declare(exchange='hello_fanout2', exchange_type='fanout')

properties = pika.BasicProperties('dummyMethedGet')
message = {
    'message':'hello world'
}
channel.basic_publish(exchange='hello_fanout2', routing_key='', body=json.dumps(message))
print(" [x] Sent 'Hello World!'")
connection.close()
