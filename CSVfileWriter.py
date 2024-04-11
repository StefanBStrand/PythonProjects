import csv
import json

# Load admissions data
admissions = {}
with open('/Users/stefan/Documents/Dev/Informatikk_HIOF/Databasesystemer V24/Oblig2/innleggelser.csv',
          mode='r', encoding='utf-8') as infile:
    reader = csv.DictReader(infile, delimiter=';')
    print(reader.fieldnames)
    for row in reader:
        patient_id = row['pasient_id']
        # Create a dictionary for each admission record
        admission_record = {
            "innleggelsesdato": row['innleggelsesdato'],
            "utskrivningsdato": row['utskrivningsdato'],
            "diagnose": row['diagnose'],
            "lege_id": row['lege_id']
        }
        # Append the admission record to the list of admissions for each patient
        if patient_id not in admissions:
            admissions[patient_id] = []
        admissions[patient_id].append(admission_record)

# Update patients data with admissions
with open('/Users/stefan/Documents/Dev/Informatikk_HIOF/Databasesystemer V24/Oblig2/pasienter_med_provins.csv',
          mode='r', encoding='utf-8') as infile, open('updated_patients.csv', mode='w', encoding='utf-8',
                                                      newline='') as outfile:
    reader = csv.DictReader(infile, delimiter=';')
    fieldnames = reader.fieldnames + ['innleggelser']  # Add 'innleggelser' to field names
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)

    writer.writeheader()
    for row in reader:
        patient_id = row['pasient_id']
        # Serialize the admissions data and add it to the 'innleggelser' column
        row['innleggelser'] = json.dumps(admissions.get(patient_id, []))
        writer.writerow(row)
