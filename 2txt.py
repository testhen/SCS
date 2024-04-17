"""This script requires two input directories: the target directory containing the code repositories and another directory where
it will write its output. The output directory mirrors the structure of the target directory. It converts all files within the code
repositories to .txt format, facilitating subsequent analysis. This prepared output is then utilized by another script, specialized
in extracting URLs and IP addresses, as it specifically operates on .txt files."""


import os
import shutil

def convert_to_txt(input_directory, output_directory):
    for root, dirs, files in os.walk(input_directory):
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, input_directory)
            new_file_path = os.path.join(output_directory, os.path.splitext(relative_path)[0] + ".txt")
            os.makedirs(os.path.dirname(new_file_path), exist_ok=True)
            if file.endswith(".txt"):
                shutil.copyfile(file_path, new_file_path)
            else:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                with open(new_file_path, 'w', encoding='utf-8') as f:
                    f.write(content)

if __name__ == "__main__":
    input_directory = input("Enter the path to the cloned repository directory: ")
    output_directory = input("Enter the path to the output directory for .txt files: ")

    convert_to_txt(input_directory, output_directory)
