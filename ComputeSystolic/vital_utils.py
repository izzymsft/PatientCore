
import json 

class PatientDataPoint:
    def __init__(self, datapointLabel="", id="", min=0, max=0, average=0):
        self.label = datapointLabel
        self.id = id
        self.minimum = min
        self.maximum = max
        self.average = average

    def toJson(self):
        dictionary = {
            "label": self.label,
            "id": self.id,
            "minimum" : self.minimum,
            "maximum" : self.maximum, 
            "average" : self.average,  
        }
        return dictionary

class VitalsComputer:
    
    def __init__(self):
        self.name = "VitalsComputer"

    def computeFieldData(self, record, field_name):

        patient_id = record.get("id")
        # Retrieve the vitals list of vitals
        patient_vitals = record.get("vitals")

        mean=0.0
        maximum=0.0
        minimum=0.0
        total_sum=0.0
        total_count=0

        first_record = patient_vitals[0][field_name]
        minimum = first_record
        maximum = first_record

        for vital in patient_vitals:

            current_pulse = vital[field_name]

            if (current_pulse < minimum):
                minimum = current_pulse

            if (current_pulse > maximum):
                maximum = current_pulse
            
            total_sum = total_sum + current_pulse
            total_count = total_count + 1

            mean = total_sum / total_count

        return PatientDataPoint(field_name, patient_id, minimum, maximum, mean)
    