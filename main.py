import sys
from fpdf import FPDF


def convert_to_pdf():
    # Create instance of FPDF class
    pdf = FPDF()

    # Add a page
    pdf.add_page()

    # Set font
    pdf.set_font("Arial", size=12)

    # Open the file in read-binary mode
    with open("./main.txt", "rb") as file:
        # Read the content of the file
        for line in file:
            line = line.decode("utf-8")  # Convert bytes to string
            line = inject_variables(line)
            if line != "":
                pdf.multi_cell(190, 5, txt=line, align="J")

    file.close()

    # Save the pdf with name .pdf
    pdf.output("main.pdf")


def inject_variables(line):

    if to:
        line = line.replace("$to", to)
    else:
        line = line.replace("$to", "")

    # Replace the company name placeholder with the actual company name
    if company_name:
        line = line.replace("$company_name", company_name)
    else:
        line = line.replace("$company_name", "")

    if department:
        line = line.replace("$department", department)
    else:
        line = line.replace("$department", "")

    if full_address:
        line = line.replace("$full_address", full_address)
    else:
        line = line.replace("$full_address", "")

    

    # Replace the position name placeholder with the actual position name
    if position_name:
        line = line.replace("$position_name", position_name)
    else:
        line = line.replace("$position_name", "")

    if job_id:
        line = line.replace("$job_id", f"(Job ID: {job_id})")
    else:
        line = line.replace("$job_id", "")

    return line


if __name__ == "__main__":
    # Print the script name
    print(f"Script Name: {sys.argv[0]}")

    # Check if all arguments are provided
    if len(sys.argv) < 7:
        print("Please provide all arguments")
        print("Usage: python main.py <to> <company_name> <department> <full_address> <position_name> <job_id>")
        sys.exit(1)

    # Print all arguments
    to = sys.argv[1]
    company_name = sys.argv[2]
    department = sys.argv[3]
    full_address = sys.argv[4]
    position_name = sys.argv[5]
    job_id = sys.argv[6]

    convert_to_pdf()
