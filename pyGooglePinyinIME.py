from typing import List
import requests

API_URL: str = 'https://inputtools.google.com/request'

class GooglePinyinIME:
    def __init__(self, req_count: int=11):
        self._pinyin: str = ''
        self._potential_hanzi_list: List[str] = []
        self._req_count = req_count
    
    def get_pinyin(self) -> str:
        return self._pinyin
    
    def get_potential_hanzi_list(self) -> List[str]:
        return self._potential_hanzi_list
    
    def add_pinyin_char(self, c: str) -> List[str]:
        if ord(c.lower()) not in range(ord('a'), ord('z') + 1):
            raise ValueError(f'invalid character {c} for pinyin')
        self._pinyin += c
        self._make_request()

    def remove_last_pinyin_char(self) -> List[str]:
        self._pinyin = self._pinyin[:-1]
        self._make_request()
    
    def set_pinyin(self, pinyin: str) -> None:
        if any(ord(c.lower()) not in range(ord('a'), ord('z') + 1) for c in pinyin):
            raise ValueError(f'invalid pinyin from input {pinyin}')
        self._pinyin = pinyin
        self._make_request()
    
    def set_req_count(self, req_count: int) -> None:
        self._req_count = req_count

    def _make_request(self) -> List[str]:
        response = requests.post(API_URL, data={
            'text': self._pinyin,
            'itc': 'zh-t-i0-pinyin',
            'num': self._req_count,
            'ie': 'utf-8'
        })
        if response.status_code == 200:
            self._potential_hanzi_list= response.json()[1][0][1]
        else:
            response.raise_for_status() 
