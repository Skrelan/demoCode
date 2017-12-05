import models.models as models
import utils.utils as utils
import logging
import json
import datetime

logging.basicConfig(
    level=logging.INFO, format="[%(asctime)s] | [%(levelname)s] | %(message)s")


def read_demographic(store):
    header = True
    fhand = open('demo.psv', 'r')
    for line in fhand:
        raw = line.rstrip().split('|')  # raw = [id,birth_date,gender]
        if not len(raw[0]) or not len(raw[1]) or raw[2] not in ['M', 'F']:
            logging.debug("Missing data in demo data | Skipping")
            continue
        if header:
            header = False
            continue
        patient = models.Patient(
            patient_id=raw[0], birth_date=raw[1], gender=raw[2])
        store[patient.patient_id] = patient.data


def read_events(store):
    header = True
    fhand = open('events.psv', 'r')
    for line in fhand:
        raw = line.rstrip().split('|')
        # raw = [patient_id,date,icd_version,icd_code]
        try:
            if not len(raw[0]) or not len(raw[1]) or not len(
                    raw[2]) or not len(raw[3]):
                continue
        except Exception as e:
            logging.debug("Missing data in events data | Skipping record")
            logging.error(e)
        if header:
            header = False
            continue
        if not raw[0] in store:  # if patient_id not in demo.psv, skip
            logging.debug(
                "Dropping event as it does not have demographic data")
            continue
        event = models.Event(
            patient_id=raw[0],
            date=raw[1],
            icd_version=raw[2],
            icd_code=raw[3])
        store[event.patient_id]["events"].append(event.data)


def clean_up(store):
    for (k, v) in store.items():
        if not len(v["events"]):
            store.pop(k, None)


def stats(store):
    patient_time_lines = []
    gender_tally = {"M": 0, "F": 0}
    patient_ages = []
    for (k, v) in store.items():
        # gender tallying
        gender_tally[store[k]["gender"]] = gender_tally.get(
            store[k]["gender"], 0) + 1

        # in the case where more than one event exsists
        if len(store[k]["events"]) > 1:
            first_date = store[k]["events"][0]["date"]
            last_date = store[k]["events"][0]["date"]
            for event in store[k]["events"]:
                first_date = min(event["date"], first_date)
                last_date = max(event["date"], last_date)

            # patient time stats
            time_line, err = utils.diff_in_days(first_date, last_date)
            if err:
                logging.warn("Skipping | {}".format(err))
                continue
            patient_time_lines.append(time_line)

            # age stats
            age, err = utils.diff_in_years(store[k]["birth_date"], last_date)
            if err:
                logging.warn("Skipping time stats | {}".format(err))
                continue
            patient_ages.append(age)

        else:
            patient_time_lines.append(0)  # because day A - day A = 0 days
            age, err = utils.diff_in_years(store[k]["birth_date"],
                                           store[k]["events"][0]["date"])
            if err:
                logging.warn("Skipping age stats| {}".format(err))
            patient_ages.append(age)

    min_time, median_time, max_time, err = utils.find_min_median_maximum(
        patient_time_lines)
    if err:
        logging.error("patient time stats failed | {}".format(err))
    min_age, median_age, max_age, err = utils.find_min_median_maximum(
        patient_ages)
    if err:
        logging.error("patient age stats failed | {}".format(err))

    result = """
    Total number of valid patients :{8}\n
    Gender stats : Male :{0}\t Female{1}\n
    Patient Time stats: Min: {2}\t Median: {3}\t Max: {4}\n
    Patient Age stats: Min: {5}\t Median: {6}\t Max: {7}""".format(
        gender_tally["M"], gender_tally["F"], min_time, median_time, max_time,
        min_age, median_age, max_age, len(store.keys()))

    return result


def write_to_file(store):
    ts = datetime.datetime.now().strftime("%d%m%Y-%I%M%p")
    with open('output/result' + ts + '.json', 'w') as fp:
        json.dump(store, fp)
