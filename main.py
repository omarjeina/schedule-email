import time
import schedule
from utils import schedule_email


def main():
    schedule_email()
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()
