import time

from core.startup import startup

from core.shutdown import shutdown


def main():

    try:

        startup()

        while True:

            time.sleep(1)

    except KeyboardInterrupt:

        shutdown()


if __name__ == "__main__":

    main()