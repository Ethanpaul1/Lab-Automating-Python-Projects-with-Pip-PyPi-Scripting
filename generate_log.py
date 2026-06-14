from datetime import datetime

def generate_log(log_entries):
    if not isinstance(log_entries, list):
        raise ValueError("Input must be a list")
    
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    
    with open(filename, "w") as f:
        for entry in log_entries:
            f.write(f"{entry}\n")
    
    print(f"Log file {filename} created successfully")
    return filename

if __name__ == "__main__":
    sample_data = ["User logged in", "User updated profile", "Report exported"]
    generate_log(sample_data)
