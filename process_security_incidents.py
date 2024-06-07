import csv

# Define the input and output file paths
input_file = 'security_incidents.csv'
output_file = 'security_incidents_modified.csv'

# Read the CSV file and store the data in a list
data = []
with open(input_file, mode='r', newline='') as file:
    reader = csv.reader(file)
    headers = next(reader)  
    data.append(headers + ['Status'])  
    for row in reader:
        data.append(row + ['Pending'])  

# Save the modified data to a new CSV file
with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"Modified data has been saved to {output_file}")
