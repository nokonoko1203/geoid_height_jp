import json
from geoid_height import get


def get_geoid_height(event, context):
    params = event.get('queryStringParameters')
    lat = params["lat"]
    lng = params["lng"]
    geoid = get(lng, lat)

    response = {
        "statusCode": 200,
        "body": json.dumps(
            {
                "geoid_height": geoid
            }
        )
    }

    return response
