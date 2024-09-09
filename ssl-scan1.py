import subprocess
import sys

def run_nmap_ssl_cert_scan(ip, port):
    try:
        command = ["nmap", "--script", "ssl-cert", "-p", port, ip]
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error scanning {ip}:{port} - {e}"

def parse_nmap_output(output):
    # Customize this function to extract and format the desired information
    lines = output.splitlines()
    result = "\n".join(lines)
    return result

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
                print("Output:")
                print(parsed_output)
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
