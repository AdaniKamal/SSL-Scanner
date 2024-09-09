# ssl-scan.py
This script is too check on ssl vulnerabilities such as
- SSL Expiry
- SSL weak hashing algorithm
- CN Name

## Usage
python ssl-scan.py hosts.txt

## Features

|No|Features|
|--|--------|
|1|This scanner will do the nmap scan.<br><b>Command:</b> `nmap --script ssl-cert -p <port> <IP>`|
|2|Output only the details|
|3||

## Result
![Screenshot 2024-09-09 at 9 48 18 PM](https://github.com/user-attachments/assets/7343fb78-28c4-4834-9fe2-fcfd1d88938d)

