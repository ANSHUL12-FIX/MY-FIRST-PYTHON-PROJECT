
import csv

def write_into_csv(info_list):
    with open('student_info.csv','a', newline='') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
            writer.writerow(["Name","Age","Contact number","E-mail id"])

        writer.writerow(info_list)

if __name__ == '__main__':
    condition = True

    while(condition):
        student_info = input("Enter student information for student #{} in the following format (Name Age Contact_Number E-mail_id): ")

        #split
        student_info_list = student_info.split(' ')

        print("\n The entered information is -\nName: {}\nAge: {}\nContact_number: {}\nE_mail id: {}"
            .format(student_info_list[0], student_info_list [1], student_info_list[2], student_info_list[3]))

        choice_check = input("Is the entered information correct? (yes/no): ")
        if choice_check == "yes":
            write_into_csv(student_info_list)

            condition_check = input("Enter (yes/no) if you want to enter information for other student:")
            if condition_check == "yes":
                condition = True
            elif condition_check == "no":
                condition = False
        elif choice_check == "no":
          print("\nplease re-enter the values!")
