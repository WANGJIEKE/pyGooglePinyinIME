# pyGooglePinyinIME

A Python 3 wrapper of [Google Input Tools](https://www.google.com/inputtools/) API for Pinyin.

## Notice

This is **NOT an official Google API** (I cannot find any official documentation) so use at your own risk.

## Requirement

```shell
python3 -m pip install requests
```

## Sample Usage

```python
>>> import googleIME as ime
>>> words, matched_lens = ime.get_words('nidazidaikongge')
>>> print(words)
['你打字带空格', '你', '尼达', '尼', '拟', '泥', '腻', '逆', '妮', '倪', '妳']
>>> print(matched_lens)
[15, 2, 4, 2, 2, 2, 2, 2, 2, 2, 2]
```

By some simple modification, it should support other languages that Google Input Tools support.
