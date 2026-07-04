import datetime


def log(message, data=None):
    print("\n==============================")
    print(f"[LOG] {datetime.datetime.now()}")
    print(message)

    if data:
        print("DATA:", data)

    print("==============================\n")