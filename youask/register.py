#!/usr/local/bin/python3

from cgitb import enable
enable()

from html_functions import *

page_name = "register"


print('Content-Type: text/html')
print()

print("""
    %s
    <body>
        <header>    <!-- A header section displayed at the top of the page--->
            <h1>HEADER</h1>
        </header>

        <main>      <!-- The main part of the website --->
            
        </main>

        <aside>     <!-- A small aside that contains information not related to the main --->

        </aside>

        %s
        %s
    """ % (pageStart("Register", page_name), generateNav(page_name), pageEnd()))
