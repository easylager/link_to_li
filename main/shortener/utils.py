import pyshorteners
import random, string




def get_short_code():
    length = 6
    char = string.ascii_uppercase + string.digits + string.ascii_lowercase
    short_id = ''.join(random.choice(char) for x in range(length))
    return short_id


def short(url):
    endpoint = get_short_code()
    short_url = f'http://127.0.0.1:8000/{endpoint}'
    return short_url


print(short('https://proglib.io/p/a-mozhno-pokoroche-kak-rabotayut-sokrashchateli-ssylok-2020-02-24'))
char = string.ascii_uppercase + string.digits + string.ascii_lowercase
print(char)
print(get_short_code())