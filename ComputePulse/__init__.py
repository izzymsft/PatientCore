import logging
import json
import azure.functions as func

from . import vital_utils as utils


def main(req: func.HttpRequest) -> func.HttpResponse:
    
    field_name = "pulse"

    logging.info('Generating Summaries for field name ' + field_name)

    patient_record = req.get_json()

    num_vitals = int(patient_record.get("total"))

    computer = utils.VitalsComputer()

    result = computer.computeFieldData(patient_record, field_name)

    response_body = json.dumps(result.toJson())

    if num_vitals > 0:
        return func.HttpResponse(response_body)
    else:

        response_body = "Please submit a patient record with at least one vital"
        status = 400
        
        return func.HttpResponse(body=response_body, status_code=status)
             
