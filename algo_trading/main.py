import logging
import time
import trade

logger = logging.getLogger(__name__)
logging.basicConfig(filename='myapp.log',
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    level=logging.INFO,
                    datefmt='%Y-%m-%d %H:%M:%S')


def start(symbol, end_time=60 * 60 * 12, interval_in_seconds=60):
    t_end = time.time() + end_time  # Run for 12 hour
    while time.time() < t_end:
        if trade.is_market_open():
            trade.apply_sma_strategy(symbol)
        else:
            logging.info(f"Market is closed. Trying again in {interval_in_seconds} seconds.")
        time.sleep(interval_in_seconds)


def main():
    start("XTIUSD")
    mt5.shutdown()
    logging.info("Program terminated...")


if __name__ == '__main__':
    main()
