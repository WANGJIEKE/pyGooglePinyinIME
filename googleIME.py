import requests

_API_URL: str = 'https://inputtools.google.com/request'

def get_words(input_: str, req_count: int=11) -> ([str], [int]):
    response = requests.post(_API_URL, data={
        'text': input_,
        'itc': 'zh-t-i0-pinyin',
        'num': req_count,
        'ie': 'utf-8'
    })
    if response.status_code != 200:
        response.raise_for_status()
    json = response.json()
    if isinstance(json, list) and len(json) == 1 and json[0] == 'FAILED_TO_PARSE_REQUEST_BODY':
        raise ValueError(str(json))
    return json[1][0][1], json[1][0][3]['matched_length']
