def pageStart(title, id, sub_dir):
    # This will generate the start of each html page including the <head></head>
    # Prefix will be put before each link, if a subdir is calling this function then prefix will be changed else empty
    prefix='../' if sub_dir else ''

    result = """
        <!DOCTYPE html>
        <html lang="en" id="%s">
            <head>
                <meta charset="utf-8" />
                <title>%s - YouAsk</title>

                <meta name-"viewport" content="initial-scale=1.0, width=device-width" />
            </head>
    """ % (id, title)
    # <link rel="stylesheet" href="styles/styles.css" />
    return result


def pageEnd():
    # This will generate the end of each html page, including the <footer>

    result = """
                <footer>
                </footer>
            </body>
        </html>"""

    return result


def generateNav(page, sub_dir):
    # This will generate the nav bar based on input for each page
    # Prefix will be put before each link, if a subdir is calling this function then prefix will be changed else empty
    prefix='../' if sub_dir else ''

    home = "%sindex.py" % prefix
    questions = "%squestions.py" % prefix
    profile = "%sprofile.py" % prefix
    support = "%ssupport.py" % prefix

    if page == "home":
        home = ""
    elif page == "questions":
        questions = ""
    elif page == "profile":
        profile = ""
    elif page == "support":
        support = ""

    return """
        <nav>
            <ul>
                <li><a href="%s">Home</a></li>
                <li><a href="%s">Questions</a></li>
                <li><a href="%s">Profile</a></li>
                <li><a href="%s">Support</a></li>
            </ul>
        </nav>
        """ % (home, questions, profile, support)


def loginToAccess():
    # If the user is not logged in this will be displayed
    error_msg = """
        <section
            <p class="Error">To submit a question you must be logged in, you may do so here: </p>
            <ul>
                <li><a href="register.py">Register</a></li>
                <li><a href="login.py">Log In</a></li>
            </ul>
        </section>
    """
    return error_msg


def alreadyLoggedIn():
    # If the user is already logged in and tries to log in
    error_msg = """
        <p class="Error">You are already logged in.</p>
        <p><a href="logout.py">Logout Here</a></p>
    """
    return error_msg


def generateQuestionForm(url, question, description, error):
    # Generate the question form to be used if the user is logged in
    result = """
        <form action="%s" method="post">
            <fieldset> <!-- Question, Description -->
                <legend>Submit a Question</legend>

                <label for="question">Question: </label>
                <input type="text" name="question" id="question" value="%s" maxlength="300"/>

                <label for="description">Description: </label>
                <input type="text" name="description" id="description" value="%s"/>

                <input type="submit" value="Submit Question"/>
            </fieldset
        </form>
        %s
    """ % (url, question, description, error)

    return result


def generateAnswerForm(url, answer, error):
    # Generate the answer form to be used
    result = """
        <section>
            <form action="%s" method="post">
                <fieldset> <!-- Answer -->
                    <legend>Submit an Answer</legend>

                    <label for="answer">Answer: </label>
                    <input type="text" name="answer" id="answer" value="%s"/>

                    <input type="submit" value="Submit Answer"/>
                </fieldset
            </form>
            %s
        </section>
    """ % (url, answer, error)

    return result


def generateBugreportForm(url, description, error):
    # Generate the question form to be used if the user is logged in
    result = """
        <form action="%s" method="post">
            <fieldset> <!--  Description -->
                <label for="description">Description: </label>
                <input type="text" name="description" id="description" value="%s"/>
                <input type="submit" value="Submit Bug"/>
            </fieldset
        </form>
        %s
     
    """ % (url, description, error)

    return result


def generateBugreportFormWithEmail(url, description, email, error):
    # Generate the question form to be used if the user is logged in
    result = """
        <form action="%s" method="post">
            <fieldset> <!--  Description -->
                <label for="description">Description: </label>
                <input type="text" name="description" id="description" value="%s"/>
                <label for="email">Your email: </label>
                 <input type="text" name="email" id="email" value="%s"/>
                <input type="submit" value="Submit Bug"/>
            </fieldset
        </form>
        %s

    """ % (url, description, email, error)

    return result
