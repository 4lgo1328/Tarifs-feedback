from application import run_app
from bot import parse_updates
from threading import Thread
if __name__ == '__main__':
    t1, t2 = Thread(run_app()), Thread(parse_updates())
    t1.start(), t2.start()
    t1.join(), t2.join()