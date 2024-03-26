!pip install odfpy
import csv
from odf import text, teletype
from odf.opendocument import load

def odt_to_csv(odt_file, csv_file):
    # Load the ODT file
    doc = load(odt_file)

    # Open CSV file in write mode
    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)

        # Iterate through each paragraph in the ODT file
        for paragraph in doc.getElementsByType(text.P):
            # Write each paragraph as a row in the CSV file
            csv_writer.writerow([teletype.extractText(paragraph)])

# Replace 'input.odt' with the path to your ODT file
# Replace 'output.csv' with the desired path for the CSV output
odt_to_csv('/content/dirty_dataset.odt', 'output.csv')



