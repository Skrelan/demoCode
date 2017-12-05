class Patient:
    def __init__(self, patient_id, birth_date, gender):
        self.patient_id = patient_id
        self.data = {"birth_date": birth_date, "gender": gender, "events": []}


class Event:
    def __init__(self, patient_id, date, icd_version, icd_code):
        self.patient_id = patient_id
        self.data = {
            "date":
            date,
            "system":
            "http://hl7.org/fhir/sid/icd-9-cm"
            if icd_version == 9 else "http://hl7.org/fhir/sid/icd-10"
        }
