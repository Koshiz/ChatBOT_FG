import os

def remove_duplicates(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Create a set to store unique sentences
    unique_sentences = set()

    # Filter out duplicate sentences and keep only unique ones
    unique_lines = []
    for line in lines:
        sentence = line.strip()  # Remove leading/trailing spaces and newlines
        if sentence not in unique_sentences:
            unique_sentences.add(sentence)
            unique_lines.append(sentence)

    # Write the unique sentences back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write('\n'.join(unique_lines))

def remove_duplicates_across_files(root_directory):
    # A set to store all encountered sentences across files
    all_sentences = set()

    # Iterate through each folder and process text files inside them
    for folder_name in os.listdir(root_directory):
        folder_path = os.path.join(root_directory, folder_name)
        if os.path.isdir(folder_path):
            for file_name in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file_name)
                if os.path.isfile(file_path):
                    with open(file_path, 'r', encoding='utf-8') as file:
                        lines = file.readlines()
                    for line in lines:
                        sentence = line.strip()
                        if sentence not in all_sentences:
                            all_sentences.add(sentence)

    # Iterate through each folder and remove duplicate sentences in each file
    for folder_name in os.listdir(root_directory):
        folder_path = os.path.join(root_directory, folder_name)
        if os.path.isdir(folder_path):
            for file_name in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file_name)
                if os.path.isfile(file_path):
                    remove_duplicates(file_path)

# Set the path to the root directory containing the folders with text files
root_directory = 'C://WORK//ChatBOT//NEW'
remove_duplicates_across_files(root_directory)
