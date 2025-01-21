import bot
import application
from threading import Thread


def main():
    t1, t2 = Thread(target=bot.parse_updates), Thread(target=application.run_app)
    t2.start(), t1.start()
    t2.join(), t1.join()


if __name__ == "__main__":
    main()
