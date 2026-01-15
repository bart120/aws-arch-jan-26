import time
import json
import random

def lambda_handler(event, context):
    # Simulation d'un appel base de données lent
    time.sleep(0.3)

    # Simulation d'un calcul inutile
    data = []
    for i in range(5000):
        data.append(i * random.random())

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Réponse API",
            "items": len(data)
        })
    }
