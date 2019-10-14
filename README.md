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
ime = GooglePinyinIME()

ime.set_pinyin('nidazidaikongge')
print(ime.get_potential_hanzi_list())

# output: ['你打字带空格', '你', ...]

```

By some simple modification,it should support other languages that Google Input Tools support.
