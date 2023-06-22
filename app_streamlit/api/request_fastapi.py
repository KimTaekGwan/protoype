import requests
import json


def req_doc2vec(file_name):
    headers = {'accept': 'application/json',
               'Content-Type': 'application/json'}

    url = f'http://127.0.0.1:8000/doc2vec/{file_name}'
    r = requests.post(url, headers=headers)
    rescode = r.status_code

    if rescode == 200:
        res = r.json()
        return res
    else:
        print(f"Error Code: {rescode}")
