import csv, json,os

input_csv = os.environ.get("INPUT_CSV")
output_json = os.environ.get("OUTPUT_JSON")

with open(input_csv, newline="", encoding="utf-8") as csvfile:
    reader= csv.DictReader(csvfile)
    data = list(reader)

with open(output_json, "w", encoding="utf-8") as jsonfile:
    json.dump(data, jsonfile, indent=4)
    print("Conversion terminée !")

