from datetime import datetime

def log(msg: str, source: str) -> None:
    print(f'[{datetime.now().strftime("%H:%M:%S")}]({source}) ---> {msg}')