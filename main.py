import os
import re
from OOPS_Project import Admission, Student
import csv
import time
import pandas as pd

def clear(): return os.system('cls')

message = ""

# Names of all CSV files to access
data = {"BCA":["f_bca.csv","s_bca.csv","t_bca.csv"],"BCA in Analytics":["f_bca_ana.csv","s_bca_ana.csv","t_bca_ana.csv"],"BSc(PMCS)":["f_bsc(pmcs).csv","s_bsc(pmcs).csv","t_bsc(pmcs).csv"],"BSc(PME)":["f_bsc(pme).csv","s_bsc(pme).csv","t_bsc(pme).csv"],"BBA":["f_bba.csv","s_bba.csv","t_bba.csv"],"BBA in Aviation":["f_bba_avi.csv","s_bba_avi.csv","t_bba_avi.csv"],"BCom":["f_bcom.csv","s_bcom.csv","t_bcom.csv"],"BCom in Finance":["f_bcom_fin.csv","s_bcom_fin.csv","t_bcom_fin.csv"],"BCom in Tourism":["f_bcom_tou.csv","s_bcom_tou.csv","t_bcom_tou.csv"],"BA in English":["f_ba_eng.csv","s_ba_eng.csv","t_ba_eng.csv"],"BA in Sociology":["f_ba_soc.csv","s_ba_soc.csv","t_ba_soc.csv"],"BA in Economics":["f_ba_eco.csv","s_ba_eco.csv","t_ba_eco.csv"]}

def main_menu():
    counter = 0
    while counter == 0:
        clear()
        print(" Kristu Jayanti College ".center(146, '-'))
        print("\nWelcome to our Student_Buddy - Interface.")
        ans = input("\nPlease enter the option number you desrire to continue with\n\n1. Admissions\n2. ID Card\n3. Examinations\n4. Attendence\n5. Library\n6. Co-Curricular Activities\n7. Exit\n\nEnter your option: ")
        if ans.isalpha() or ans in "890`~!@#$%^&*()-_=+\{\}[]\|:;'\"<>,.?/\\":
            print("Invalid input")
            time.sleep(3)
        else:
            response(ans)
        

def response(n):
    if n == "1":
        admission()        
    elif n == "2":
        idcard()       
    elif n == "3":
        exam()
    elif n == "4":
        pass    
    elif n == "5":
        pass
    elif n == "6":
        pass           
    elif n == "7":
        exit()
         
def admission():
    # First step of admission process.
    def apply():
        clear()
        print(" Application Form ".center(133, '-'))
        print("\nPress 0 to go back to Admission main menu")
        fname = input("Enter your first name : ")
        if fname == "0":
            admission()

        lname = input("\nEnter your last name : ")
        if lname == "0":
            admission()

        ag = 0
        while (ag == 0):
            ans1 = input("\nEnter your gender \n1. Male \n2. Female\nEnter the option number : ")
            if ans1 == "1":
                gender = "Male"
                ag = 1
            elif ans1 == "2":
                gender = "Female"
                ag = 1
            elif ans1 == "0":
                admission()
            else:
                print("\nEnter a valid option number")

        adob = 0
        while (adob == 0):
            dob = input("\nEnter your DOB in DD/MM/YYYY format : ")
            p = r"^(3[01]|[1-2][0-9]|0?[1-9])/(1[0-2]|0?[1-9])/(([0-9]{4}))$"
            result = re.findall(p, dob)
            if len(result) > 0:
                adob = 1
            elif dob == "0":
                admission()
            else:
                print("\nInvalid format !")

        phoneno = input("\nEnter your Phone No. : ")
        if phoneno == "0":
            admission()

        while (len(phoneno) != 10 or phoneno.isdigit() == False):
            print("\nEnter a valid phome number")
            phoneno = input("\nEnter your Phone No. : ")

        emailid = input("\nEnter your Email-ID : ")
        if emailid == "0":
            admission()

        while (emailid.endswith(".com") == False or "@" not in emailid):
            print("\nPlease enter a valid Email ID")
            emailid = input("\nEnter your Email ID : ")

        address = input("\nEnter your address : ")
        if address == "0":
            admission()

        father_name = input("\nEnter your Father's name : ")
        if father_name == "0":
            admission()

        father_occupation = input("\nEnter your Father's occupation : ")
        if father_occupation == "0":
            admission()

        mother_name = input("\nEnter your Mother's name : ")
        if mother_name == "0":
            admission()

        mother_occupation = input("\nEnter your Mother's occupation : ")
        if mother_occupation == "0":
            admission()

        ac = 0
        while (ac == 0):
            ans2 = input(
                "\nSelect your Category \n1. General\n2. SC|ST\n3. 2B\n4. 3B\nEnter option number :  ")
            if ans2 == "0":
                admission()
            elif ans2 == "1":
                category = "General"
                ac = 1
            elif ans2 == "2":
                category = "SC|ST"
                ac = 1
            elif ans2 == "3":
                category = "2B"
                ac = 1
            elif ans2 == "4":
                category = "3B"
                ac = 1

        ts = 0
        while ts == 0:
            tenth_score = input("\nEnter your 10th grade marks (in percentage %) : ")
            if int(tenth_score) > 100:
                print("\nEnter marks ranging from 1 to 100")
            elif tenth_score == "0":
                admission()
            else:
                ts = 1 

        tws = 0
        while tws == 0:
            twelveth_score = input("\nEnter your 12th grade marks (in percentage %) :  ")
            if int(twelveth_score) > 100:
                print("\nEnter marks ranging from 1 to 100")
            elif twelveth_score == "0":
                admission()
            else:
                tws = 1 

        aps = 0
        while (aps == 0):
            ans3 = input("\nSelect your previous stream \n1. Science\n2. Commerce\n3. Arts\nEnter option number : ")
            if ans3 == "0":
                admission()
            elif ans3 == "1":
                previous_stream = "Science"
                aps = 1
            elif ans3 == "2":
                previous_stream = "Commerce"
                aps = 1
            elif ans3 == "3":
                previous_stream = "Arts"
                aps = 1
            else:
                print("\nEnter a valid option")

        aos = 0
        while (aos == 0):
            if previous_stream == "Science":
                ans4 = input("\nSelect the stream you want to opt for \n1. Science\n2. Commerce\n3. Arts\nEnter option number : ")
                if ans4 == "0":
                    admission()
                elif ans4 == "1":
                    stream_opting_for = "Science"
                    aos = 1
                elif ans4 == "2":
                    stream_opting_for = "Commerce"
                    aos = 1
                elif ans4 == "3":
                    stream_opting_for = "Arts"
                    aos = 1
                else:
                    print("\nEnter a valid option")

            elif previous_stream == "Commerce":
                ans4 = input("\nSelect the stream you want to opt for \n1. Commerce\n2. Arts \nEnter option number : ")
                if ans4 == "0":
                    admission()
                elif ans4 == "1":
                    stream_opting_for = "Commerce"
                    aos = 1
                elif ans4 == "2":
                    stream_opting_for = "Arts"
                    aos = 1
                else:
                    print("\nEnter a valid option")

            elif previous_stream == "Arts":
                ans4 = input("\nSelect the stream you want to opt for \n1. Arts\nEnter option number : ")
                if ans4 == "0":
                    admission()
                elif ans4 == "1":
                    stream_opting_for = "Arts"
                    aos = 1
                else:
                    print("\nEnter a valid option")

        if stream_opting_for == "Science":
            asc = 0
            while (asc == 0):
                ans5 = input("\nSelect the course your opting for : \n1. BCA\n2. BCA in Analytics\n3. BSc(PMCS)\n4. BSc(PME)\nEnter option number : ")
                if ans5 == "0":
                    admission()
                elif ans5 == "1":
                    course_opting_for = "BCA"
                    asc = 1
                elif ans5 == "2":
                    course_opting_for = "BCA in Analytics"
                    asc = 1
                elif ans5 == "3":
                    course_opting_for = "BSc(PMCS)"
                    asc = 1
                elif ans5 == "4":
                    course_opting_for = "BSc(PME)"
                    asc = 1
                else:
                    print("\nEnter a valid option")

        elif stream_opting_for == "Commerce":
            aco = 0
            while (aco == 0):
                ans6 = input("\nSelect the course your opting for : \n1. BBA\n2. BBA in Aviation\n3. BCom\n4. BCom in Finance\n5. BCom in Tourism\nEnter option number : ")
                if ans6 == "0":
                    admission()
                elif ans6 == "1":
                    course_opting_for = "BBA"
                    aco = 1
                elif ans6 == "2":
                    course_opting_for = "BBA in Aviation"
                    aco = 1
                elif ans6 == "3":
                    course_opting_for = "BCom"
                    aco = 1
                elif ans6 == "4":
                    course_opting_for = "BCom in Finance"
                    aco = 1
                elif ans6 == "5":
                    course_opting_for = "BCom in Tourism"
                    aco = 1
                else:
                    print("Enter a valid option")

        elif stream_opting_for == "Arts":
            aar = 0
            while (aar == 0):
                ans7 = input("\nSelect the course your opting for : \n1. BA in Sociology\n2. BA in Economics\n3. BA in English\nEnter option number : ")
                if ans7 == "0":
                    admission()
                elif ans7 == "1":
                    course_opting_for = "BA in Sociology"
                    aar = 1
                elif ans7 == "2":
                    course_opting_for = "BA in Economics"
                    aar = 1
                elif ans7 == "3":
                    course_opting_for = "BA in English"
                    aar = 1
                else:
                    print("\nEnter a valid option")

        achievements = input("\nEnter any achievements achieved : ")
        if achievements == "0":
            admission()

        a = Admission(fname, lname, gender, dob, phoneno, emailid, address, father_name, father_occupation, mother_name,
                      mother_occupation, category, tenth_score, twelveth_score, previous_stream, stream_opting_for, course_opting_for, achievements)
        print(
            f"\nThank you for applying. Your application number is {a.get_app_no()} \nPlease note down the application number for future reference and wait as we process your application and check your eligibility for the chosen course.\nIf any changes/updates has to be made, go to update option in the main menu.\n\n")
        time.sleep(15)
        selection_process(a)

    # Second step of admission process.

    def selection_process(a):
        # Importing methods from Admission class
        # Checking course availability
        if Admission.check_course_availability(a) == True:
            # Checking eligibility
            if Admission.check_eligibility(a) == True:
                a.set_status("Selected")
                message = "Selected"
            else:
                a.set_status("Not selected")
                message = Admission.check_eligibility(a)

        review(message, a)

    # Third step of admission process.
    def review(m, a):
        print("Applicant's result".center(146, '-'))
        if m == "Selected":
            print("\n\nCongratulations on getting selected ! Please proceed with document submission and fee payment process to end the admission formalities.\n\n")
        else:
            print(m)

        document_submission(m, a)

    # Forth step of admission process.
    def document_submission(m, a):
        time.sleep(3)
        print("Document Submission".center(146, '-'))
        if m != "Selected":
            Admission.set_documents(a, "NA")
        else:
            Admission.document_submission(a)
         # Getting all the info in a dictionary.
        old_info = a.__dict__
        new_info = {}
        for i, j in old_info.items():
            key = i.replace("_Admission__", "")
            new_info[key] = j
            data = [new_info]

            # Writing the info dictionary to a csv file.
        fields = ["appno", "first_name", "last_name", "gender", "dob", "phone_no", "email_id", "address", "father_name", "father_occupation", "mother_name",
                  "mother_occupation", "category", "tenth_score", "twelveth_score", "previous_stream", "stream_opting_for", "course_opting_for", "achievements", "status", "documents"]
        with open('applications.csv', 'a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writerows(data)

        fee_process(a)

    # Fifth step of admission process.
    def fee_process(a):
        print("\n")
        print("Fee Payment".center(146, '-'))
        Admission.fee_payment(a)
        print("\nThanks for taking admission in our college. We wish you all the best on your journey with us.")
        time.sleep(5)
        main_menu()

    # Updating applicant's information
    def update_app():
        clear()
        appln_no = []
        csv_file_reader = csv.reader(
            open("C:\\Users\\2145644\\OOPS Project\\applications.csv", "r"))
        for row1 in csv_file_reader:
            if row1[0] == 'appno':
                continue
            appln_no.append(row1[0])

        print(" Update Application ".center(146, '-'))
        print("\nPress 0 to go back to main menu")
        status = 0
        while (status == 0):
            appno = input("\nEnter your application number : ")
            if appno == "0":
                admission()
            elif appno in appln_no:
                status = 1
            else:
                print(
                    "\nApplication entered is incorrect. Please enter the right application number.")

        columns = ["Application No.", "First name", "Last name", "Gender", "DOB", "Phone Number", "Email-ID", "Address", "Father name", "Father occupation",
                   "Mother name", "Mother occupation", "Category", "10th score", "12th score", "Previous stream", "Opting stream", "Opting course", "Achievements", "Status", "Documents"]
        row_pos = 0
        index = 0
        csv_file_reader2 = csv.reader(
            open("C:\\Users\\2145644\\OOPS Project\\applications.csv", "r"))
        for row in csv_file_reader2:
            if row[0] == appno:
                for i in range(len(row)):
                    if i == 19:
                        continue
                    print(f"\n{index} . {columns[i]} : {row[i]}")
                    index += 1
                break
            else:
                row_pos += 1

        counter = 0
        df = pd.read_csv("applications.csv")
        while (counter == 0):
            option = input("\nEnter the option number to change : ")
            if int(option) > 19:
                print("Invalid input")
                time.sleep(3)

            elif option == "0":
                counter = 1
                admission()

            elif option == "1":
                u_fname = input("\nEnter your first name : ")
                df.loc[(row_pos - 1), 'first_name'] = u_fname

            elif option == "2":
                u_lname = input("\nEnter your last name : ")
                df.loc[(row_pos - 1), 'last_name'] = u_lname

            elif option == "3":
                counter = 0
                while counter == 0:
                    ans1 = input("\nEnter your gender \n1. Male \n2. Female\nEnter the option number : ")
                    if ans1 == "1":
                        u_gender = "Male"
                        counter = 1
                    elif ans1 == "2":
                        u_gender = "Female"
                        counter = 1
                    else:
                        print("\nInvalid input")
                df.loc[(row_pos - 1), 'gender'] = u_gender

            elif option == "4":
                u_dob = input("\nEnter your DOB in DD/MM/YYYY format : ")
                condition = True
                while (condition):
                    p = r"^(3[01]|[1-2][0-9]|0?[1-9])/(1[0-2]|0?[1-9])/(([0-9]{4}))$"
                    result = re.findall(p, u_dob)
                    if len(result) > 0:
                        break
                    else:
                        print("\nInvalid format !")

                df.loc[(row_pos - 1), 'dob'] = u_dob

            elif option == "5":
                u_phoneno = input("\nEnter your Phone No. : ")
                while (len(u_phoneno) != 10 or u_phoneno.isdigit() == False):
                    print("\nEnter a valid phome number")
                    u_phoneno = input("\nEnter your Phone No. : ")
                df.loc[(row_pos - 1), 'phone_no'] = u_phoneno

            elif option == "6":
                u_emailid = input("\nEnter your Email-ID: ")
                while (u_emailid.endswith(".com") == False or "@" not in u_emailid):
                    print("\nPlease enter a valid Email-ID")
                    u_emailid = input("\nEnter your Email-ID : ")
                df.loc[(row_pos - 1), 'email_id'] = u_emailid

            elif option == "7":
                u_address = input("\nEnter your address : ")
                df.loc[(row_pos - 1), 'address'] = u_address

            elif option == "8":
                u_fathername = input("\nEnter your Father's name : ")
                df.loc[(row_pos - 1), 'father_name'] = u_fathername

            elif option == "9":
                u_fatheroccupation = input(
                    "\nEnter your Father's occupation: ")
                df.loc[(row_pos - 1), 'father_occupation'] = u_fatheroccupation

            elif option == "10":
                u_mothername = input("\nEnter your Mother's name : ")
                df.loc[(row_pos - 1), 'mother_name'] = u_mothername

            elif option == "11":
                u_motheroccupation = input(
                    "\nEnter your Mother's occupation: ")
                df.loc[(row_pos - 1), 'mother_occupation'] = u_motheroccupation

            elif option == "12":
                a = 0
                while (a == 0):
                    ans2 = input("\nSelect your Category \n1. General\n2. SC|ST\n3. 2B\n4. 3B\nEnter option number :  ")
                    if ans2 == "1":
                        u_category = "General"
                        a = 1
                    elif ans2 == "2":
                        u_category = "SC|ST"
                        a = 1
                    elif ans2 == "3":
                        u_category = "2B"
                        a = 1
                    elif ans2 == "4":
                        u_category = "3B"
                        a = 1
                    else:
                        print("\nEnter a valid option number")

                df.loc[(row_pos - 1), 'category'] = u_category

            elif option == "13":
                ts = 0
                while ts == 0:
                    u_tenth = input("\nEnter your 10th grade marks : ")
                    if int(u_tenth) > 10:
                        print("\nEnter marks ranging from 1 to 100")
                    else:
                        ts = 1
                df.loc[(row_pos - 1), 'tenth_score'] = u_tenth

            elif option == "14":
                tws = 0
                while tws == 0:
                    u_twelve = input("\nEnter your 10th grade marks : ")
                    if int(u_twelve) > 10:
                        print("\nEnter marks ranging from 1 to 100")
                    else:
                        tws = 1
                df.loc[(row_pos - 1), 'twelveth_score'] = u_twelve
            
            elif option == "15":
                a = 0
                while (a == 0):
                    ans3 = input("\nSelect your previous stream \n1. Science\n2. Commerce\n3. Arts\nEnter option number : ")
                    if ans3 == "1":
                        u_previous_stream = "Science"
                        a = 1
                    elif ans3 == "2":
                        u_previous_stream = "Commerce"
                        a = 1
                    elif ans3 == "3":
                        u_previous_stream = "Arts"
                        a = 1
                    else:
                        print("\nEnter a valid option")
                df.loc[(row_pos - 1), 'previous_stream'] = u_previous_stream

            elif option == "16":
                a = 0
                while (a == 0):
                    ans4 = input("\nSelect the stream you want to opt for \n1. Science\n2. Commerce\n3. Arts\nEnter option number : ")
                    if ans4 == "1":
                        u_stream_opting_for = "Science"
                        a = 1
                    elif ans4 == "2":
                        u_stream_opting_for = "Commerce"
                        a = 1
                    elif ans4 == "3":
                        u_stream_opting_for = "Arts"
                        a = 1
                    else:
                        print("\nEnter a valid option")

                df.loc[(row_pos - 1), 'stream_opting_for'] = u_stream_opting_for

            elif option == "17":
                u_stream_opting_for = df.loc[(
                    row_pos - 1), 'stream_opting_for']
                if u_stream_opting_for == "Science":
                    a = 0
                    while (a == 0):
                        ans5 = input("\nSelect the course your opting for : \n1. BCA\n2. BCA in Analytics\n3. BSc(PMCS)\n4. BSc(PME)\nEnter option number : ")
                        if ans5 == "1":
                            u_course_opting_for = "BCA"
                            a = 1
                        elif ans5 == "2":
                            u_course_opting_for = "BCA in Analytics"
                            a = 1
                        elif ans5 == "3":
                            u_course_opting_for = "BSc(PMCS)"
                            a = 1
                        elif ans5 == "4":
                            u_course_opting_for = "BSc(PME)"
                            a = 1
                        else:
                            print("\nEnter a valid option")

                elif u_stream_opting_for == "Commerce":
                    a = 0
                    while (a == 0):
                        ans5 = input("\nSelect the course your opting for : \n1. BBA\n2. BBA in Aviation\n3. BCom\n4. BCom in Finance\n5. BCom in Tourism\nEnter option number : ")
                        if ans5 == "1":
                            u_course_opting_for = "BBA"
                            a = 1
                        elif ans5 == "2":
                            u_course_opting_for = "BBA in Aviation"
                            a = 1
                        elif ans5 == "3":
                            u_course_opting_for = "BCom"
                            a = 1
                        elif ans5 == "4":
                            u_course_opting_for = "BCom in Finance"
                            a = 1
                        elif ans5 == "5":
                            u_course_opting_for = "BCom in Tourism"
                            a = 1
                        else:
                            print("Enter a valid option")

                elif u_stream_opting_for == "Arts":
                    a = 0
                    while (a == 0):
                        ans5 = input("\nSelect the course your opting for : \n1. BA in Sociology\n2. BA in Economics\n3. BA in English\nEnter option number : ")
                        if ans5 == "1":
                            u_course_opting_for = "BA in Sociology"
                            a = 1
                        elif ans5 == "2":
                            u_course_opting_for = "BA in Economics"
                            a = 1
                        elif ans5 == "3":
                            u_course_opting_for = "BA in English"
                            a = 1
                        else:
                            print("\nEnter a valid option")
                df.loc[(row_pos - 1), 'course_opting_for'] = u_course_opting_for

            elif option == "18":
                u_achievements = input("\nEnter your achievements : ")
                df.loc[(row_pos - 1), 'achievements'] = u_achievements

            elif option == "19":
                docs = df.loc[(row_pos - 1), 'documents']
                rep = docs.replace("'", "")
                strip = rep.strip("{}")
                new_docs = dict(subString.split(':') for subString in strip.split(','))
                for document, status in new_docs.items():
                    if status == " Not submitted":
                        resp = input(f"Do you have your {document} card? Y/N\n")
                        if resp.upper() == "Y":
                            new_docs[document] = "Submitted"
                
                print("Document submission status updated")
                df.loc[(row_pos - 1), 'documents'] = str(new_docs)

            df.to_csv("applications.csv", index=False)

    counter = 0
    while counter == 0:
        clear()
        print(" Admissions Department ".center(146, '-')+"\n")
        print("Welcome to the Admissions Department.".center(150))
        print("Please select an option to proceed.\n\n1. Apply\n2. Update your application\n3. Go back")
        ans = input("\nEnter the option number : ")
        if ans.isalpha() or ans in "4567890`~!@#$%^&*()-_=+\{\}[]\|:;'\"<>,.?/\\":
            print("Invalid input")
            time.sleep(3)
        else:
            counter = 1

    if ans == "1":
        apply()
    elif ans == "2":
        update_app()
    elif ans == "3":
        main_menu()


def idcard():
    def register():
        print(" ID Card Registration ".center(146, '-'))
        appln_no = []
        csv_file_reader = csv.reader(
            open("C:\\Users\\2145644\\OOPS Project\\applications.csv", "r"))
        for row1 in csv_file_reader:
            if row1[0] == 'appno':
                continue
            appln_no.append(row1[0])

        status = 0
        while (status == 0):
            clear()
            print(" ID Card Registration ".center(146, '-'))
            appno = input("Enter 0 to back\nEnter your application number : ")
            if appno == "0":
                main_menu()
            elif appno in appln_no:
                status = 1
            else:
                print(
                    "\nApplication entered is incorrect. Please enter the right application number.")
                time.sleep(3)
            
        print("Please wait as we retrieve your details from our database...")
        time.sleep(5)
        csv_file_reader3 = csv.reader(
            open("C:\\Users\\2145644\\OOPS Project\\applications.csv", "r"))
        details = []
        details.append(appno)
        for row in csv_file_reader3:
            if row[0] == appno:
                for i in range(1, 8):
                    if i == 3 or i == 6:
                        continue
                    details.append(row[i])
                for i in range(16, 18):
                    details.append(row[i])

        applno, fname, lname, dob, phoneno, address, stream, course = details
        name = fname + " " + lname
        a = Student(applno, name, dob, phoneno, address, stream, course)
        student_info = a.__dict__
        new_info = {}
        for i, j in student_info.items():
            key = i.replace("_Student__", "")
            if key == 'csv':
                csvFile = j
                continue
            new_info[key] = j
            data = [new_info]

            # Writing the info dictionary to a csv file.
        fields = ["appno","reg_no", "name", "dob", "emailid",
              "phoneno", "address", "stream", "course"]
    
        csv_file_reader4 = csv.reader(open(csvFile, "r"))
        asd = []
        for row1 in csv_file_reader4:    
            asd.append(row1[0])
        if a.get_appno() in asd:
            print("\nAlready registered. Please go to View ID Card option to see the ID card details")
            time.sleep(5)
            main_menu()
        else:
            with open(csvFile, 'a', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=fields)
                writer.writerows(data)
                print(f'''\n\nID card generated
----------------------------------------
Name : {a.get_name()}                          

Register No. : {a.get_reg_no()}                    
                    
Class : {a.get_course()}

Phone : {a.get_phoneno()}

Email : {a.get_emailid()} 
----------------------------------------''')
                time.sleep(100)
                main_menu()

    def view_ID():
        print(" ID Card  ".center(146, '-'))
        inp1 = input("Enter your stream : ")
        inp2 = input("\nEnter the year : ")
        




    counter = 0
    while counter == 0:
        print(" ID Card Center ".center(146, '-'))
        inp = input("Enter the option number:\n1.Register for ID card\n2.View ID card")
        if inp.isalpha() or inp in "34567890`~!@#$%^&*()-_=+\{\}[]\|:;'\"<>,.?/\\":
            print("Invalid input")
            time.sleep(3)
        else:
            counter = 1
    if inp == "1":
        register()
    elif inp == "2":
        view_ID()


def exam():
    def check_time_table():
        clear()
        stats = 0
        while stats == 0:
            csv_file = None
            stream = input("Press 0 to go back \nEnter your stream name : ")
            if stream == "0":
                exam()
            elif stream == "BCA":
                csv_file = "C:\\Users\\2145644\\OOPS Project\\BCA_TT.csv"
            elif stream == "BBA":
                csv_file = "BBA_TT.csv"
            elif stream == "BA in Economics":
                csv_file = "BA_ECO_TT.csv"
            else:
                print("Enter right input")

            csv_file_reader4 = csv.reader(open(csv_file, "r"))
            exam_code = []
            exam_name = []
            exam_type = []
            exam_date = []
            exam_duration = []
            exam_marks = []

            for rows in csv_file_reader4:
                exam_code.append(rows[0])
                exam_name.append(rows[1])
                exam_type.append(rows[2])
                exam_date.append(rows[3])
                exam_duration.append(rows[4])
                exam_marks.append(rows[5])

            print('''\n   Date    | Exam Code |  Exam Type  |  Exam Duration |  Total Marks  | Exam Name            
--------------------------------------------------------------------------------------------''')
            for i in range(1, len(exam_code)):
                print(
                    f"{exam_date[i]} |  {exam_code[i]}   |     {exam_type[i]}       |   {exam_duration[i]}   |      {exam_marks[i]}      | {exam_name[i]}                  ")
            print("\nT - Theory\nP - Practical")
            counter = 0
            while counter == 0:
                ans = input("\nEnter 0 to go back : ")
                if ans.isalpha() or ans in "123456789`~!@#$%^&*()-_=+\{\}[]\|:;'\"<>,.?/\\":
                    print("Invalid input")
                    time.sleep(1)
                else:
                    counter = 1
            if ans == "0":
                exam()

    status = 0
    while status == 0:
        clear()
        print("Examination Section".center(133, '-'))
        print("Please select an option to proceed. \n\n1. Examination Time Table\n2. Check results\n3. Go back")
        ans = input("\nEnter the option number : ")
        if ans.isalpha() or ans in "4567890`~!@#$%^&*()-_=+\{\}[]\|:;'\"<>,.?/\\":
            print("Invalid input")
            time.sleep(3)
        else:
            status = 1
    if ans == "1":
        check_time_table()
    elif ans == "2":
        #check_results()
        pass
    elif ans == "3":
        main_menu()


main_menu()
