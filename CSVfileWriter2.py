import csv
import os


file_path = '/Users/stefan/Documents/Dev/Informatikk_HIOF/Databasesystemer V24/Oblig2/updated_patients.csv'
print(os.path.exists(file_path))  # This should print True if the file exists
# Load province data
provinces = {}
with open('/Users/stefan/Documents/Dev/Informatikk_HIOF/Databasesystemer V24/Oblig2/provins.csv',
          mode='r', encoding='utf-8') as infile:
    reader = csv.DictReader(infile, delimiter=';')
    for row in reader:
        provinces[row['provins_id']] = row['provins_navn']

# Update patients data with province names
with open('/Users/stefan/Documents/Dev/Informatikk_HIOF/Databasesystemer V24/Oblig2/updated_patients.csv',
          mode='r', encoding='utf-8') as infile, \
        open('final_patients.csv', mode='w', encoding='utf-8', newline='') as outfile:
    reader = csv.DictReader(infile, delimiter=',')

    # Insert 'provins_navn' right after 'provins_id'
    provins_id_index = reader.fieldnames.index('provins_id') + 1
    fieldnames = reader.fieldnames[:]
    if 'provins_navn' not in reader.fieldnames:
        fieldnames.insert(provins_id_index, 'provins_navn')

    writer = csv.DictWriter(outfile, fieldnames=fieldnames)

    writer.writeheader()
    for row in reader:
        # Retrieve the 'provins_id' from the current row
        provins_id = row['provins_id']
        # Use the 'provins_id' to add the 'provins_navn'
        row['provins_navn'] = provinces.get(provins_id, 'Unknown Province')

        writer.writerow(row)
