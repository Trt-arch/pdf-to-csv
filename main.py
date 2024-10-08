# I made this to make my life easier since i needed info from a pdf

import tabula

# Function to convert PDF tables to CSV
def convert_pdf_to_csv(pdf_path, csv_path):
    # Extract tables from PDF into a list of dataframes
    tables = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)

    # Group extracted tables and write them into CSV
    with open(csv_path, mode='w', newline='', encoding='utf-8') as file:
        for table in tables:
            table.to_csv(file, mode='a', index=False)  # Append each table to the CSV

# Ask the user to input the path to the PDF file
pdf_file_path = input("Please enter the full path to the PDF file: ")

if pdf_file_path:
    # Define the output CSV file path by replacing .pdf with .csv
    csv_file_path = pdf_file_path.replace(".pdf", ".csv")

    # Convert the selected PDF tables into CSV
    convert_pdf_to_csv(pdf_file_path, csv_file_path)

    print(f"Tables from {pdf_file_path} have been written to {csv_file_path}")
else:
    print("No PDF file path provided.")
