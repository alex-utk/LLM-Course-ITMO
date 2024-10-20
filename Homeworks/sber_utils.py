import json
import requests


def get_access_token(client_id: str, auth_key: str) -> str:
    payload = 'scope=GIGACHAT_API_PERS'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'RqUID': client_id,
        'Authorization': f'Basic {auth_key}'
    }

    response = requests.request("POST",
                                "https://ngw.devices.sberbank.ru:9443/api/v2/oauth",
                                headers=headers, data=payload, verify=False)
    if response.status_code == 200:
        return json.loads(response.text)['access_token']
    else:
        raise Exception(f'Status code: {response.status_code}')
