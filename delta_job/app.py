import logic
import logging

logging.basicConfig(
    level=logging.INFO, format="[%(asctime)s] | [%(levelname)s] | %(message)s")

store = {}

if __name__ == "__main__":
    logic.read_demographic(store)
    logic.read_events(store)
    logic.clean_up(store)
    logging.info(logic.stats(store))
    logic.write_to_file(store)
