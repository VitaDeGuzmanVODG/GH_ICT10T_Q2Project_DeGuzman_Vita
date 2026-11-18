from pyscript import display,  document

club_members = {
    "Destiny Math Demon",
    "Francheesecake Dela Cruz",
    "Raver Espanol Pistachio",
    "Santiago Kuya",
    "MJ Bronzer",
    "Kenneth Cabinet",
    "Bombalean Kahoot",
    "Jia Tickles",
    "Chalanie Absent",
    "Enrique Ray Cis",
    "Jack Jesse All"
}


def check_member(e):

    first_name = document.getElementById("first_name").value.strip()
    last_name = document.getElementById("last_name").value.strip()

    full_name = f"{first_name} {last_name}".strip()

    if not first_name or not last_name:
        display(
            "Please enter your first name and last name.",
            target="result"
        )
        return

    member_checker = full_name.casefold() in [
        name.casefold() for name in club_members
    ]

    if member_checker:
        message = (
            f"Congratulations {full_name}, "
            "you are a member of the Monarch Club!"
        )
    else:
        message = (
            f"Sorry {full_name}, your name is not "
            "in the Monarch Club member list."
        )

    display(message, target="result", append=False)

non_metals = {
    "H":  {"name": "Hydrogen",   "number": 1,  "mass": 1.008},
    "He": {"name": "Helium",     "number": 2,  "mass": 4.003},
    "C":  {"name": "Carbon",     "number": 6,  "mass": 12.011},
    "N":  {"name": "Nitrogen",   "number": 7,  "mass": 14.007},
    "O":  {"name": "Oxygen",     "number": 8,  "mass": 15.999},
    "F":  {"name": "Fluorine",   "number": 9,  "mass": 18.998},
    "Ne": {"name": "Neon",       "number": 10, "mass": 20.180},
    "P":  {"name": "Phosphorus", "number": 15, "mass": 30.974},
    "S":  {"name": "Sulfur",     "number": 16, "mass": 32.06},
    "Cl": {"name": "Chlorine",   "number": 17, "mass": 35.45},
    "Ar": {"name": "Argon",      "number": 18, "mass": 39.948},
    "Se": {"name": "Selenium",   "number": 34, "mass": 78.971},
    "Br": {"name": "Bromine",    "number": 35, "mass": 79.904},
    "Kr": {"name": "Krypton",    "number": 36, "mass": 83.798},
    "I":  {"name": "Iodine",     "number": 53, "mass": 126.904},
    "Xe": {"name": "Xenon",      "number": 54, "mass": 131.293},
    "Rn": {"name": "Radon",      "number": 86, "mass": 222},
}


result_box = document.getElementById("result")


def search_element(event):
    
    symbol = document.getElementById("symbol").value.strip().capitalize()
    try:
        
        element = non_metals[symbol]
        result_box.innerText = (
            f"Symbol: {symbol}\n"
            f"Element: {element['name']}\n"
            f"Atomic Number: {element['number']}\n"
            f"Atomic Mass: {element['mass']}"
        )
    except KeyError:
        # The symbol is not in the dictionary
        result_box.innerText = f"Sorry, '{symbol}' does not exist in the non-metals list."
# Python finished loading
result_box.innerText = "The element details will show here."


def search_element(event):

    symbol = document.getElementById("symbol").value.strip().capitalize()

    if not symbol:
        document.getElementById("element-message").innerText = (
            "Please enter an element symbol."
        )
        return

    element = non_metals.get(symbol)

    if element:

        document.getElementById("result-symbol").innerText = symbol

        document.getElementById("result-name").innerText = (
            element["name"]
        )

        document.getElementById("result-atomic-number").innerText = (
            element["number"]
        )

        document.getElementById("result-atomic-mass").innerText = (
            element["mass"]
        )

        document.getElementById("element-message").innerText = (
            "Element successfully found!"
        )

    else:

        document.getElementById("result-symbol").innerText = "-"
        document.getElementById("result-name").innerText = "-"
        document.getElementById("result-atomic-number").innerText = "-"
        document.getElementById("result-atomic-mass").innerText = "-"

        document.getElementById("element-message").innerText = (
            f"Sorry, '{symbol}' does not exist in the non-metals list."
        )

grade_7 = {
    "Martin Edwards",
    "Eom Seonghyeon",
    "Ahn Keonho",
    "Kim Juhoon",
    "Zhao James",
}

grade_8 = {
    "Raver Estacio",
    "Kenneth Concepcion",
    "Miguel Jimenez",
    "Santiago Valdez",
    "Jesse Villante",
}

grade_9 = {
    "Destiny Reyes",
    "Franchesca Dela Rosa",
    "MJ Madrelejos",
}

grade_10 = {
    "Chalanie Lumbang",
    "Jia Hadji Gapor",
    "Gurleen Kaur",
}

all_members = grade_7 | grade_8 | grade_9 | grade_10

def update_results():

    names = "\n".join(sorted(all_members))

    document.getElementById("member-list").textContent = names

    document.getElementById("member-total").textContent = (
        f"Total members: {len(all_members)}"
    )


def add_member(event):

    first_name = document.getElementById("first-name").value.strip()
    last_name = document.getElementById("last-name").value.strip()

    if not first_name or not last_name:
        display(
            "Please enter both first name and last name.",
            target="member-message",
            append=False
        )
        return

    full_name = f"{first_name} {last_name}".strip()

    existing_names = {
        name.casefold() for name in all_members
    }

    if full_name.casefold() in existing_names:
        message = f"{full_name} is already a member."
    else:
        all_members.add(full_name)
        message = f"Member added: {full_name}"

    display(
        message,
        target="member-message",
        append=False
    )

    document.getElementById("first-name").value = ""
    document.getElementById("last-name").value = ""

    update_results()
