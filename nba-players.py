from csv import DictWriter, reader, writer, DictReader

def addHeader(id, name, team, age, height, weight):
    with open("nba-players.csv", "a", encoding="utf-8", newline="") as csvFile:
        fields = {
        "Header1": id,
        "Header2" : name,
        "Header3" : team,
        "Header4" : age,
        "Header5" : height,
        "Header6" : weight
    }
        dWriter = DictWriter(csvFile, fieldnames=fields)
        dWriter.writerow(fields)

def addPlayer(id, name, team, age, height, weight):
    with open("nba-players.csv", "a", encoding="utf-8", newline="") as csvFile:
        datas = {
        "Id": id,
        "Name": name,
        "Team": team,
        "Age": age,
        "Height": height,
        "Weight": weight
    }
        dWriter = DictWriter(csvFile, fieldnames=datas)
        dWriter.writerow(datas)

def countPlayer():
    with open("nba-players.csv", encoding="utf-8", newline="") as csvFile:
        cReader = reader(csvFile)
        result = list(cReader)
        return len(result)


def getAllPlayers():
    with open("nba-players.csv", encoding="utf-8", newline="") as csvFile:
        dReader = DictReader(csvFile)
        for row in dReader:
            print(
                f"{row['Id']}\t{row['Name']}\t{row['Team']}\t{row['Age']}\t{row['Height']} mt.\t{row['Weight']} kg.")

print("-" * 30)
print("""
        Welcome to NBA Otomation,

        1- with Add Header
        2- with Add Player
        3- with Get All Players

        Quit('quit', 'q', 'Q')
""")

print("-" * 30)

while True:
    select = input("Please Select What Do you Want : ")
    if select == "q" or select == "quit" or select == "Q" or select == "Quit":
        print("Bye!")
        break
    elif select == "1":
        fields = {
            "Header1": input("Add Header: "),
            "Header2": input("Add Header: "),
            "Header3": input("Add Header: "),
            "Header4": input("Add Header: "),
            "Header5": input("Add Header: "),
            "Header6": input("Add Header: ")
        }
        addHeader(
            fields["Header1"],
            fields["Header2"],
            fields["Header3"],
            fields["Header4"],
            fields["Header5"],
            fields["Header6"]
        )
    elif select == "2":
        datas = {
        "Name": input("Enter the name information:  "),
        "Team": input("Enter the team information: "),
        "Age": input("Enter the age information: "),
        "Height": input("Enter the height information: "),
        "Weight": input("Enter the height information: ")
        }
        addPlayer(
            countPlayer()-1,
            datas["Name"],
            datas["Team"],
            datas["Age"],
            datas["Height"],
            datas["Weight"]
        )
    elif select== "3":
        getAllPlayers()