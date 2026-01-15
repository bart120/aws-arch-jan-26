import redis
import json
import time

redis_client = redis.Redis(
    host="REDIS_ENDPOINT",
    port=6379,
    decode_responses=True
)

def lambda_handler(event, context):
    cache_key = "response:test"

    cached = redis_client.get(cache_key)
    if cached:
        return {
            "statusCode": 200,
            "body": cached
        }

    time.sleep(0.3)  # traitement simulé
    # Simulation d'un calcul inutile
    data = []
    for i in range(5000):
        data.append(i * random.random())
    
    result = json.dumps({
            "message": "Réponse API",
            "items": len(data)
        })

    redis_client.setex(cache_key, 60, result)

    return {
        "statusCode": 200,
        "body": result
    }