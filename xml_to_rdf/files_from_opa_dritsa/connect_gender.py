import csv


def update_csv(first_csv_path, second_csv_path, output_csv_path):
    # Read the first CSV file
    with open(first_csv_path, 'r', encoding="utf8") as first_csv:
        first_reader = csv.reader(first_csv)
        first_data = list(first_reader)

    # Read the second CSV file
    with open(second_csv_path, 'r', encoding="utf8") as second_csv:
        second_reader = csv.reader(second_csv)
        second_data = list(second_reader)

    # Find the column names in both CSV files
    first_header = first_data[0]
    second_header = second_data[0]

    # Find the index of the last column in the second CSV
    last_column_index = len(second_header) - 1

    # Create a dictionary to store the values from the second CSV
    second_dict = {}
    for row in second_data[1:]:
        key = row[0]
        value = row[last_column_index]
        second_dict[key] = value

    # Append the value from the second CSV to the matching rows in the first CSV
    for row in first_data[1:]:
        key = row[0]
        if key in second_dict:
            value = second_dict[key]
            row.append(value)

    # Write the updated data to the output CSV file
    with open(output_csv_path, 'w', newline='', encoding="utf8") as output_csv:
        writer = csv.writer(output_csv)
        writer.writerows(first_data)

    print(f"Updated CSV saved to {output_csv_path}")


first = "./parl_members_activity_1989onwards_06_2023.csv"
second = "../out_files/parl_members_activity_1989onwards_with_gender.csv"
output = "./output.csv"
update_csv(first, second, output)
