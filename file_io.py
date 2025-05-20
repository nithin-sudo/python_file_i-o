import os

def display_menu():

    print("1.Display all student records\n2.Add a new student record"
        "\n3.Update a Student's score\n4.Delete a student record.\n5.Overwrite all records.\n6.Read + write combo.\n7.Exit")
    

def file_operations():
    while True:
        display_menu()
        choice = input("Enter your choice:")

        match choice:
            case "1":
                print("Displaying Students Records")
                f = open("students.txt", "r")
                data = f.read()
                print(data)
                f.close()

            case "2":
                print("Adding a new student")
                with open("students.txt","a+") as f:
                    f.seek(0)
                    data = f.read()
                    print(data)
                    data = input("Enter data:")
                    f.write(f"\n{data}")

            case "3":
                print("Updating a score")
                updated_lines = []
                with open("students.txt","r") as f:
                    data = f.read()
                    print(data)
                    roll_no = input("Select the Roll no. of the students you want to edit:")
                    f.seek(0)
                    while True:
                        line = f.readline()
                        print(line)
                        if not line:
                            break

                        parts = line.strip().split(',')
                        print(parts)
                        if parts[0] == roll_no:
                            new_score = input("Enter the new score:")
                            roll = parts[0].strip()
                            name = parts[1].strip()
                            updated_line = roll+","+ name + "," + new_score
                            updated_lines.append(updated_line)
                        else:
                            updated_lines.append(line)
                    
                with open("students.txt","w") as f:
                    for line in updated_lines:
                        f.write(line)
            case "4":
                print("Deleting a student record")

                updated_lines = []
                with open("students.txt","r") as f:
                    data = f.read()
                    print(data)
                    roll_no = input("Select the Roll no. of the students you want to delete:")
                    f.seek(0)
                    while True:
                        line = f.readline()
                        if not line:
                            break
                        parts = line.strip().split(',')
                        if(parts[0] == roll_no):
                            continue
                        else:
                            updated_lines.append(line)
                with open("students.txt","w") as f:
                    for line in updated_lines:
                        f.write(line)

            case "5":
                print("Overwriting all records")
                with open("students.txt","w") as f:
                    while True:
                        break_point = input("type 'STOP' to finish or hit enter to continue- ")

                        if break_point.lower() == 'stop':
                            break

                        roll_no = int(input("Enter Roll No:"))
                        student_name = input("enter student name:")
                        score = int(input("enter student score:"))
                        record = f"{roll_no},{student_name},{score}\n"
                        f.write(record)
                        
            case "6":
                print("Reading and adding")
                with open("students.txt", "a+")  as f:
                    f.seek(0)
                    data = f.read()
                    print(data)
                    while True:
                        break_point = input("type 'STOP' to finish or hit enter to continue- ")

                        if break_point.lower() == 'stop':
                            break

                        roll_no = int(input("Enter Roll No:"))
                        student_name = input("enter student name:")
                        score = int(input("enter student score:"))
                        record = f"{roll_no},{student_name},{score}\n"
                        f.write(record)

            case "7":
                print("Exiting...")
                break

            case _:                     # default case
                print("!!!!!!!!!!!!!   Select Valid Option   !!!!!!!!!!!!!!")
                                            
file_operations()