#!/usr/local/bin/python3

from cgitb import enable

from model.model_functions import getQuestion

enable()

from controller.html_functions import *

list1 = []
page_name = "questions"
result = getQuestion()
for x in result:
    list1.append(result[x])

print('Content-Type: text/html')
print()

print("""
    %s
    <body>
        <header>    <!-- A header section displayed at the top of the page--->

        </header>
        <script>
        function Add(one) {
        for(var i=0; i<one.length;i++){
    var para = document.createElement("p");
    para.innerHTML=one[i];
    document.body.appendChild(para);}
    }
        
        </script>

        <main>      <!-- The main part of the website --->
            <h1>test page</h1>
           %s
        </main>

        <aside>     <!-- A small aside that contains information not related to the main --->

        </aside>

        %s
        %s
    """ % (pageStart("Questions", page_name), result, generateNav(page_name), pageEnd()))
