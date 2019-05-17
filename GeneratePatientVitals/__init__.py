import logging
import json
import hashlib
import time
import random

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    genders = ["F", "M"]

    selected_gender_index = random.randint(0, 1)
    selected_gender = genders[selected_gender_index]

    patient_age = random.randint(1, 75)

    # Retrieving temperature, pulse, diastolic and systolic pressure ranges
    request_information = req.get_json()

    patient_id = request_information.get("id")

    vitals = []

    # {"total": 5, "min_temperature": 98, "max_temperature": 99, "min_pulse": 80, "max_pulse": 85, "min_diastolic": 80, "max_diastolic": 85, "min_systolic": 120, "max_systolic":130 }
    num_records = request_information.get("total")

    for current_index in range(1, num_records, 1):
        
        logging.debug("Current Index is " + str(current_index))

        min_temperature = request_information.get("min_temperature")
        max_temperature = request_information.get("max_temperature")

        min_pulse = request_information.get("min_pulse")
        max_pulse = request_information.get("max_pulse")

        min_diastolic = request_information.get("min_diastolic")
        max_diastolic = request_information.get("max_diastolic")

        min_systolic = request_information.get("min_systolic")
        max_systolic = request_information.get("max_systolic")

        vital_temperature = round(random.uniform(min_temperature, max_temperature), 1)
        vital_pulse = random.randint(min_pulse, max_pulse)
        vital_diastolic = random.randint(min_diastolic, max_diastolic)
        vital_systolic = random.randint(min_systolic, max_systolic)

        current_vital={
            "temperature" : vital_temperature, 
            "pulse" : vital_pulse, 
            "diastolic" : vital_diastolic,
            "systolic": vital_systolic
        }

        vitals.append(current_vital)

    total_records = len(vitals)

    result = {"id": patient_id, "age" : patient_age, "gender": selected_gender, 
                "total": total_records, "vitals": vitals}

    response_string = json.dumps(result)

    return func.HttpResponse(response_string)

    
