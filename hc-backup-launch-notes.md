<!-- 
Launch backup to 
python3 path/to/python_file.py
-->
cd Desktop/HC\ Backups/
python3 make_backup_custom.py

<!-- 
To get only published articles 
draft = False 

See: 
https://developer.zendesk.com/api-reference/help_center/help-center-api/articles/
-->

<!-- Testing Minify HTML in Sandbox Folder -->
cd /Users/lawrence/Desktop/HC Backups/Parser/Sandbox

<!-- Try -->
htmlmin --remove-all-empty-space input.html output.html
<!-- try -->
htmlmin --remove-empty-space input.html output.html

236115487.html
4635886341523.html
218002467.html
360041441674.html
115004898368.html
360042770734.html
217413737.html
10373254162707.html

# Convert symbols to HTML entities
symbol_replacements = {
    "¬†": "&nbsp;",
    "‚Äú": "&#8220;",
    "‚Äôt": "&#8217;",
    "¬Æ": "&reg;",
    "&amp;": "&",
    "&gt;": ">",
    "‚Äô": "'",
    "‚Äù": "",
    "&#8220;": "",
    <!-- ®™ -->
    "&reg;": "®",
    "&trade;": "™",
    "#8217;": "'t",
    "‚Äì": "-"
}

<!-- Output.csv  -->
<!-- this file gets generated after running html-parser. The file needs to be set to Delimited using the Text-Columns if the rows and html content come out as comma seperated instead of in their own cells -->
<!--  -->