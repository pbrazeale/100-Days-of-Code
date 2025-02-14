def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You did not enter a first and/or last name"
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    return f"{formatted_f_name} {formatted_l_name}"

formatted_string = format_name("angela", "ANGELA")

print(formatted_string)