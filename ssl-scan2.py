import subprocess
import sys
import re

def run_nmap_ssl_cert_scan(ip, port):
    try:
        command = ["nmap", "--script", "ssl-cert", "-p", port, ip]
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error scanning {ip}:{port} - {e}"

def parse_nmap_output(output):
    # Extract specific fields using regex
    subject = re.search(r"Subject: (.+)", output)
    subject_alt_name = re.search(r"Subject Alternative Name: (.+)", output)
    issuer = re.search(r"Issuer: (.+)", output)
    public_key_type = re.search(r"Public Key type: (.+)", output)
    public_key_bits = re.search(r"Public Key bits: (.+)", output)
    signature_algorithm = re.search(r"Signature Algorithm: (.+)", output)
    not_valid_before = re.search(r"Not valid before: (.+)", output)
    not_valid_after = re.search(r"Not valid after: (.+)", output)

    # Formatting the result
    result = []
    if subject:
        result.append(f"Subject: {subject.group(1)}")
    if subject_alt_name:
        result.append(f"Subject Alternative Name: {subject_alt_name.group(1)}")
    if issuer:
        result.append(f"Issuer: {issuer.group(1)}")
    if public_key_type:
        result.append(f"Public Key type: {public_key_type.group(1)}")
    if public_key_bits:
        result.append(f"Public Key bits: {public_key_bits.group(1)}")
    if signature_algorithm:
        result.append(f"Signature Algorithm: {signature_algorithm.group(1)}")
    if not_valid_before:
        result.append(f"Not valid before: {not_valid_before.group(1)}")
    if not_valid_after:
        result.append(f"Not valid after: {not_valid_after.group(1)}")

    return "\n".join(result)

def main(file_name):
    try:
        with open(file_name, "r") as file:
            for line in file:
                parts = line.strip().split()
                port = parts[0]
                ip = parts[1]

                output = run_nmap_ssl_cert_scan(ip, port)
                parsed_output = parse_nmap_output(output)

                print(f"\033[34mHosts:\033[0m {ip}")
                print(f"\033[34mPort:\033[0m {port}")
                print(f"\033[34mOutput:\033[0m")
                if parsed_output:
                    print(f"{parsed_output}")
                else:
                    print("No relevant SSL information found.")
                print("-" * 40)

    except FileNotFoundError:
        print(f"File {file_name} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ssl_scan.py <hosts_file>")
    else:
        main(sys.argv[1])
