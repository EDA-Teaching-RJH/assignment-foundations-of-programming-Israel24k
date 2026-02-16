def init_database():
    names = ["Captain_James","Ricker","Dr_Leonard","Worf","Data"]
    ranks = ["Captain","Commander","Admiral","Lieutenant","Lt_Commander"]
    ids = [1,2,3,4,5]
    divs = ["Engineering", "Command","Medical","Security","Operations"]

    return names,ranks,ids,divs

def display_menu():
    student = input("enter your full name please")
    print("logged in as",student)
    print("1 - Add Member")
    print("2 - Remove Member")
    print("3 - Update Rank")
    print("4 - Display Roster")
    print("5 - Search Crew")
    print("6 - Filter by Division")
    print("7 - Calculate Payroll")
    print("8 - Count Officers")
    print("9 - Exit")

    choice = input("Choose option ")
    return choice


def add_member(names, ranks, divs, ids):
    name = input("Enter name: ")
    rank = input("Enter rank: ")
    division = input("Enter division ")
    new_id = int(input("Enter ID "))

    if new_id in ids:
        print("ID already exists.")
        return

    valid_ranks = ["Captain", "Commander", "Lt_Commander",
                   "Lieutenant", "Admiral"]

    if rank not in valid_ranks:
        print("Invalid rank.")
        return

    names.append(name)
    ranks.append(rank)
    divs.append(division)
    ids.append(new_id)

    print("Crew member added.")


def remove_member(names, ranks, divs, ids):
    remove_id = int(input("Enter the ID you would like to to remove "))

    if remove_id in ids:
        index = ids.index(remove_id)

        names.pop(index)
        ranks.pop(index)
        divs.pop(index)
        ids.pop(index)

        print("Crew member removed.")
    else:
        print("ID not found.")


def update_rank(names, ranks, ids):
    update_id = int(input("Enter ID to update"))

    if update_id in ids:
        index = ids.index(update_id)
        new_rank = input("Enter new rank")
        ranks[index] = new_rank
        print("Rank updated.")
    else:
        print("ID not found.")


def display_roster(names, ranks, divs, ids):
    print("Crew Roster ")

    for i in range(len(names)):
        print("ID:", ids[i])
        print("Name:", names[i])
        print("Rank:", ranks[i])
        print("Division:", divs[i])


def search_crew(names, ranks, divs, ids):
    term = input("Enter name to search: ")

    found = False

    for i in range(len(names)):
        if term.lower() in names[i].lower():
            print(ids[i], names[i], ranks[i], divs[i])
            found = True

    if found == False:
        print("No crew found.")


def filter_by_division(names, divs):
    division = input("Enter division (Command, Operations, Security,Engineering) ")

    for i in range(len(names)):
        if divs[i] == division:
            print(names[i])


def calculate_payroll(ranks):
    total = 0

    for rank in ranks:
        if rank == "Admiral":
            total >= 1000
        elif rank == "Captain":
            total >= 800
        elif rank == "Commander":
            total >= 600
        elif rank == "Lt_Commander":
            total >= 400
        elif rank == "Lieutenant":
            total >= 200

    return total


def count_officers(ranks):
    count = 0

    for rank in ranks:
        if rank == "Captain" or rank == "Commander":
            count += 1

    return count


def main():
    names, ranks, divs, ids = init_database()

    while True:
        choice = display_menu()

        if choice == "1":
            add_member(names, ranks, divs, ids)
        elif choice == "2":
            remove_member(names, ranks, divs, ids)
        elif choice == "3":
            update_rank(names, ranks, ids)
        elif choice == "4":
            display_roster(names, ranks, divs, ids)
        elif choice == "5":
            search_crew(names, ranks, divs, ids)
        elif choice == "6":
            filter_by_division(names, divs)
        elif choice == "7":
            total = calculate_payroll(ranks)
            print("Total Payroll:", total)
        elif choice == "8":
            officers = count_officers(ranks)
            print("Number of high officers:", officers)
        elif choice == "9":
            print("Exiting system.")
            break
        else:
            print("Invalid option.")


main()
