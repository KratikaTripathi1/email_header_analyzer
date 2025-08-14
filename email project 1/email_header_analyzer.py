# email_header_analyzer.py

def analyze_email_header(file_path):
    # Open and read the header file
    with open(file_path, 'r', encoding='utf-8') as file:
        header_data = file.read()

    # Basic Info
    print("\n=== BASIC INFO ===\n")
    for line in header_data.split("\n"):
        if line.lower().startswith("from:") or line.lower().startswith("to:") or line.lower().startswith("subject:"):
            print(line)

    # Authentication Results
    print("\n=== AUTHENTICATION RESULTS ===\n")
    for line in header_data.split("\n"):
        if "spf=" in line.lower() or "dkim=" in line.lower() or "dmarc=" in line.lower():
            print(line)

    # Email Route
    print("\n=== EMAIL ROUTE ===\n")
    for line in header_data.split("\n"):
        if line.lower().startswith("received:"):
            print(line)

# Run the function
file_path = "sample_header.txt"  # Gmail se liya hua ya sample header
analyze_email_header(file_path)
