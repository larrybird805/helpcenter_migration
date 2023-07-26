import os
import csv
import htmlmin
from pathlib import Path
from bs4 import BeautifulSoup

# Set the folder path to parse
folder_path = '../Backup/en-us'

# Create a new CSV file to write the results to
csv_file = open("output.csv", "w", newline="", encoding="utf-16")
writer = csv.writer(csv_file)
# Create CSV Headers
writer.writerow(["File Name", "Title", "Body"])

# Loop through all HTML files in the folder and extract the H1 title
for filename in os.listdir(folder_path):
    if filename.endswith(".html"):
        # Open the HTML file and create a Beautiful Soup object
        filepath = os.path.join(folder_path, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, "html.parser")

        # Extract the H1 title from the HTML file
        h1_title = soup.find("h1").text

        #Extract minified HTML using htmlmin to minify whitespace
        html_content = str(soup)
        minified_content = htmlmin.minify(html_content, remove_comments=True, remove_empty_space=True, convert_charrefs=False)

        # Write the file name and H1 title to the CSV file
        writer.writerow([filename, h1_title, minified_content])

# Close the CSV file
csv_file.close()