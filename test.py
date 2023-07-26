import os
import pyodbc

# with open("C:\\WORK\\ChatBOT\\NEW\\url_file_mapping.txt", "r", encoding='utf-8') as mapping_file:
#     mapping_lines = mapping_file.readlines()

# for line in mapping_lines:
#      parts = line.strip().replace(":", "").split('\t')
#      print(parts)
    
root_directory = 'C:\\WORK\\ChatBOT\\NEW'
root_files = os.listdir(root_directory)
print(root_files)


