import os
import pyodbc
import numpy as np
import tiktoken

# Define the database connection details
server_name = '192.168.120.34'
database_name = 'TestBot'
username = 'DEVSRV01SQLUSER'
password = 'sql_123'

# Set the root path to the folders containing text files 
root_directory = 'C:\\WORK\\ChatBOT\\NEW'

# Path to the mapping text file that contains url and the corresponding text files
mapping_path = 'C:\\WORK\\ChatBOT\\url_file_mapping.txt'

# Function to insert the data into the sql table
def insert_into_sql(url, questions, answers):
    # Connect to SQL Database
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server_name + ';DATABASE=' + database_name + ';UID=' + username + ';PWD=' + password)
    cursor = conn.cursor()
    
    # Insert data into the table using parameterized query
    cursor.execute("INSERT INTO botData (URL, Questions, Answers) VALUES (?, ?, ?)", url, questions, answers)
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    
# Load the mapping file 
with open(mapping_path, "r", encoding='utf-8') as mapping_file:
    mapping_lines = mapping_file.readlines()
    
    
# #Define the function to calculate how many tokens to pass into OpenAi API
# def num_tokens_from_string(string: str, encoding_name: str) -> int:
#     """Returns the number of tokens in a text string."""
#     encoding = tiktoken.get_encoding(encoding_name)
#     num_tokens = len(encoding.encode(string))
#     return num_tokens
    
# Iterate through each line in the mapping file and process the corresponding text file
for line in mapping_lines:
    parts = line.strip().rsplit(':', 1) 

    # Check if the lines contain the expected number of values (URL and Text file)
    if len(parts) == 2:
        url, text_file_name = parts   
        # Remove any additional spaces in the URL and text file
        url = url.strip()
        text_file_name = text_file_name.strip()
        # Get the folders that contain the text files
        root_files = os.listdir(root_directory)
        # Construct the full path to the text file 
        text_file_path = os.path.join(root_directory, text_file_name)

        # Read the content in the text file
        with open(text_file_path, "r", encoding='utf-8') as file:
            lines = file.readlines()

        # Assuming the questions and answers
        questions = lines[::2]
        answers = lines[1::2]
        
        # print(len(questions))
        

        # # Iterate through questions and answers and insert them into the database
        # for question, answer in zip(questions, answers):  
        #     insert_into_sql(url, question.strip(), answer.strip())
        
        # tokens_count = num_tokens_from_string(questions[0], "cl100k_base")
        # print("Number of Tokens: ", tokens_count)
        
