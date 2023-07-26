# helpcenter_migration
ZenDesk to Drupal Help Center migration pipeline

## Part 1 - Backing up the Help Center
Run a custom script with make_backup_custom.py to extract a folder containing a CSV log and all contents of Published articles. 

Rename the folder to Backup and change necessary reference paths to it i.e. ../Backup/en/ etc

## Part 2 - Parse Data into a useable format 
Use the html-parser.py script and create an output.csv file. The file should encode in UTF-16 in order to preserve symbols and linebreaks within a CSV file. If the numbers for the IDs are getting rounded due to Excel's inherent settings, run the script twice (once as UTF-8 encoding for number preservation, and once as UTF-16 for the HTML) 

## Part 3 - Gather Sections and Categories (WIP)
Run section-category-list.py to generate CSV 
Run category_id_list.py to generate CSV 
Clean data and merge it into a combined Sheet using Pandas. (WIP)

## Part 4 - Cleaning up links (WIP)
Run script to extract all instances of links, text, etc. pointing to ZenDesk. Evaluate length of list and determine whether to run this automatically with a Find Replace or Pandas extract. 

## Part 5 - Putting it all together 
Combine the process from Parts 1-3 into one Combine so we can organize data by Section and Category. 

## Part 6 - Ready to Import 
Import modules from Dev main server into the new domain/server. Create Views Pipeline, Clean up CSS, and import. Create Menu, Logos, and cross-browser styling. Content Freeze! 
