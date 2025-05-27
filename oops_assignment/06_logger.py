class Logger:
    def __init__(self):
        print("Logger object initialized")

    def __del__(self):
        print("Logger object is being deleted")

log = Logger()
del log