import requests
from bs4 import BeautifulSoup
import os

#Set the list of urls to scrape
urls = [
"https://foliogrow.com/",
"https://foliogrow.com/cannabis-cultivation-software-tour/",
"https://foliogrow.com/cannabis-cultivation-software-tour/cannabis-cultivation-software-for-stakeholders/",
"https://foliogrow.com/cannabis-cultivation-software-tour/cannabis-cultivation-software-grow-manager/",
"https://foliogrow.com/cannabis-cultivation-software-tour/cannabis-cultivation-software-team-members/",
"https://foliogrow.com/cannabis-cultivation-software-tour/cannabis-cultivation-software-sales-managers/",
"https://foliogrow.com/pricing/",
"https://foliogrow.com/cannabis-cultivation-software-team/",
"https://foliogrow.com/metrc/",
"https://foliogrow.com/metrc/alaska-metrc/",
"https://foliogrow.com/metrc/california-metrc/",
"https://foliogrow.com/metrc/colorado-metrc/",
"https://foliogrow.com/metrc/district-of-columbia-metrc/",
"https://foliogrow.com/metrc/louisiana-metrc/",
"https://foliogrow.com/metrc/maine-metrc/",
"https://foliogrow.com/metrc/maryland-metrc/",
"https://foliogrow.com/metrc/massachusetts-metrc/",
"https://foliogrow.com/metrc/metrc-michigan/",
"https://foliogrow.com/metrc/missouri-metrc/",
"https://foliogrow.com/metrc/metrc-montana/",
"https://foliogrow.com/metrc/nevada-metrc/",
"https://foliogrow.com/metrc/ohio-metrc/",
"https://foliogrow.com/metrc/oklahoma-metrc/",
"https://foliogrow.com/metrc/oregon-metrc/",
"https://foliogrow.com/cannabis-cultivation-software-partner/",
"https://foliogrow.com/cannabis-cultivation-software-news/",
"https://foliogrow.com/contact/",
"https://app.foliogrow.com/accountsetup.aspx",
]

#Custom Headers to inform the server to control the behavior of the request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
}

#Create a mapping(dictionary) to store the url and the corresponding scraped data
url_file_mapping = {}

#Loop through each url
for url in urls:
    #Send GET request to the URL
    response = requests.get(url, headers=headers)
    
    #Creating beautiful soup objects for each url to parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    #Extracting the meaningful content out of the pages (p, h1, h2, h3, a, li, div, span)
    content = soup.find_all(["h1", "h2", "h3", "p", "div", "span", 'li' ])
    
    #Creating a directory to store the extracted content for each url
    directory = os.path.join(os.getcwd(), url.split("/")[-2])
    os.makedirs(directory, exist_ok=True)
    
    #Creating an empty list to store the scraped content
    scraped_content = []
    
    #Looping through each element content and extract the text
    for item in content:
        scraped_content.append(item.get_text())
        
    #Saving the extracted content in a text file
        file_name = url.split("/")[-2] + ".txt"
        file_path = os.path.join(directory, file_name)
        with open(file_path, "w", encoding="utf-8") as file:
            for item in scraped_content:
                file.write(item + "\n")     
    
    #Adding the URL and its corresponding file name to the directory
    url_file_mapping[url] = file_name
        
#Saving the URL and file name mapping to a separate text file
    mapping_file_path = os.path.join(os.getcwd(), "url_file_mapping.txt")
    with open(mapping_file_path, "w", encoding="utf-8") as mapping_file:
     for url, file_name in url_file_mapping.items():
        mapping_file.write(f"{url}: {file_name}\n")

    
    

    
    
    
    
    



