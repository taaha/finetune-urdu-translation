import zipfile
import os

def unzip_file(zip_filepath, extract_to_dir):
    # Check if the file exists
    if not os.path.exists(zip_filepath):
        print(f"The file {zip_filepath} does not exist.")
        return

    # Create the extraction directory if it does not exist
    if not os.path.exists(extract_to_dir):
        os.makedirs(extract_to_dir)

    # Unzip the file
    with zipfile.ZipFile(zip_filepath, 'r') as zip_ref:
        zip_ref.extractall(extract_to_dir)
        print(f"File extracted to: {extract_to_dir}")

# Example usage
zip_filepath = 'englishurdu-parallel-corpus.zip'  # Replace with the path to your zip file
extract_to_dir = 'dataset'  # Replace with the directory you want to extract to

unzip_file(zip_filepath, extract_to_dir)
