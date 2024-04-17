"""This Python script extracts URLs and IP addresses from text files within a specified directory and its subdirectories.
It recursively searches through each text file, identifying URLs and IP addresses present in non-commented lines. The extracted
URLs and IP addresses are then written to a file named all_URLs_IPs.txt, with each entry including the URL or IP address, the
type (URL or IP Address), the file path, and the line number where it was found. The script is executed by providing the path to
the directory containing the code files as input."""


import os
import re

def extract_urls_and_ips_from_directory(directory):
    results = []

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    lines = f.readlines()

                for line_num, line in enumerate(lines, start=1):
                    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', line)
                    ips = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', line)

                    for url in urls:
                        results.append((url, "URL", file_path, line_num))

                    for ip in ips:
                        results.append((ip, "IP Address", file_path, line_num))

    return results

def main(directory):
    results = extract_urls_and_ips_from_directory(directory)
    with open("all_URLs_IPs.txt", "w") as output_file:
        for item in results:
            output_file.write(f"{item[0]} found on line {item[3]} as {item[1]} in {item[2]}\n")

if __name__ == "__main__":
    directory = input("Enter the path to the directory containing the code files: ")
    main(directory)
