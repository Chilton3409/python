#!/usr/bin/env python3
# New file created
# create directory for html, css, and javascript that way I dont have to start from scratch for template projects.
#will convert to functions later, want to add more styling elements 
import os
import sys
project = sys.argv[1]
html_template = """<!Doctype html>\n<head>\n<link rel='stylesheet' href='style.css'>\n</head>\n
<header>\n<h1>\n</h1>\n</header>
<body>\n<div id="wrapper"></div></body>

</hmtl>"""
css_template = """#wrapper: {
    flex: auto;
    }
"""

if not os.path.exists(project):

    os.mkdir(project)

    os.chdir(project)
    os.mkdir("html")
    os.mkdir("CSS")
    os.mkdir("JS")
    os.chdir("html")

    with open("index.html", "w") as f:
        f.write(html_template)

    os.chdir("../CSS")
    with open("style.css", "w")as style:
        style.write(css_template)


else:
    print("Error, the project {} already exists".format(project))
