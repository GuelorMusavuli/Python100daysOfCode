def format_name(f_name, l_name):
    """Take a first and last name and format it to return a version of the name where
    each word is title cased.More specifically words start with upper cased
    characters and all remaining cased characters have lower case."""
    # We can have multiple returns with a single functions
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    return f"{f_name.title()} {l_name.title()}"  # return tell the computer that, it's the end of function.


print(format_name(input("What is your first name? "), input("What is your last name? ")))

