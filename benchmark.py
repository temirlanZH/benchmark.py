def benchmark(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print("Время выполнения функция: {} секунд".format(end - start))
        return return_value
    return wrapper

@benchmark

def fetch_webpage(url):
    import requests
    webpage = requests.get(url)
    return webpage.text

print(fetch_webpage("https://github.com/"))