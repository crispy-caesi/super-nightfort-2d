import csv

def decrease_numbers(input_file, output_file):
    with open(input_file, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)

    for row in data:
        for i, value in enumerate(row):
            try:
                row[i] = str(int(value) - 1)
            except ValueError:
                pass

    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

if __name__ == "__main__":
    input_file = "sprites/blocks/csv/level2_desert.csv"
    output_file = "sprites/blocks/csv/level2_desert.csv"
    decrease_numbers(input_file, output_file)


import csv

def update_numbers(input_file, output_file):
    replacements = {
        "2147483647": "0",
        "2147483648": "1",
        "2147483645": "2",
        "-2147483646": "3",
        "2147483638": "4",
        "2147483643": "5",
        "2147483642": "6",
        "2147483641": "7",
        "2147483640": "8",
        "-2147483639": "9",
        "2147483644": "10"
    }

    with open(input_file, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)

    for row in data:
        for i, value in enumerate(row):
            if value in replacements:
                row[i] = replacements[value]

    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

if __name__ == "__main__":
    input_file = input("Geben Sie den Dateipfad der Eingabedatei an: ")
    output_file = input("Geben Sie den Dateipfad der Ausgabedatei an: ")
    update_numbers(input_file, output_file)

