import redis
import time

# Configuración de Redis
redis_host = 'redis-13829.c93.us-east-1-3.ec2.redns.redis-cloud.com'
redis_port = 13829  # Cambia al puerto correspondiente
redis_password = 'kCnclqk5gRZWJkPxNeIoAGPsTeFNQjVv'

# Conexión a Redis
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

# Publicador
def publisher():
    while True:
        message = input("Introduce un mensaje para publicar: ")
        redis_client.publish('canal_prueba', message)
        print(f"Publicado: {message}")

if __name__ == "__main__":
    publisher()
