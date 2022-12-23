# Python program that provides various functionalities which a college requires using OOPS concepts.

# Admission class
from tkinter import Y

from numpy import i0


class Admission:
    '''Admission class is the class which handles the process of admission of a student based on the eligibity criteria'''
    with open('count.txt','r') as f:
        counter = int(f.read())
   
    # Courses available in college.
    courses = {"Science": [["BCA", 100, 100000], ["BCA in Analytics", 70, 120000], ["BSc(PMCS)", 60, 80000], ["BSc(PME)", 60, 80000]], "Commerce": [["BBA", 100, 100000], ["BBA in Aviation", 70, 120000], [
        "BCom", 100, 80000], ["BCom in Finance", 70, 100000], ["BCom in Tourism", 70, 100000]], "Arts": [["BA in English", 70, 80000], ["BA in Sociology", 70, 80000], ["BA in Economics", 70, 80000]]}

    def __init__(self, first_name, last_name, gender, dob, phone_no, email_id, address, father_name, father_occupation, mother_name, mother_occupation, category, tenth_score, twelveth_score, previous_stream, stream_opting_for, course_opting_for, achievements):
        # Personal details
        self.__appno = "APPLN" + str(Admission.counter)
        with open('count.txt','w') as f:
            Admission.counter += 1
            f.write(str(Admission.counter))

        self.__first_name = first_name
        self.__last_name = last_name
        self.__gender = gender
        self.__dob = dob
        self.__phone_no = phone_no
        self.__email_id = email_id
        self.__address = address
        self.__father_name = father_name
        self.__father_occupation = father_occupation
        self.__mother_name = mother_name
        self.__mother_occupation = mother_occupation
        self.__category = category

        # Education details
        self.__tenth_score = tenth_score
        self.__twelveth_score = twelveth_score
        self.__previous_stream = previous_stream
        self.__stream_opting_for = stream_opting_for
        self.__course_opting_for = course_opting_for
        self.__achievements = achievements
        self.__status = None

        # Documents details
        self.__documents = {"10th_marks_card": None, "12th_marks_card": None,
                            "Aadhar_Card": None, "Code_of_conduct": None, "Transfer_certificate": None}
    
    #GET methods
    def get_app_no(self):
        return self.__appno

    def get_name(self):
        return self.__first_name + " " + self.__last_name

    def get_gender(self):
        return self.__gender

    def get_dob(self):
        return self.__dob

    def get_phone_no(self):
        return self.__phone_no

    def get_email_id(self):
        return self.__email_id

    def get_address(self):
        return self.__address

    def get_father_name(self):
        return self.__father_name

    def get_father_occupation(self):
        return self.__father_occupation

    def get_mother_name(self):
        return self.__mother_name

    def get_mother_occupation(self):
        return self.__mother_occupation

    def get_category(self):
        return self.__category

    def get_tenth_score(self):
        return self.__tenth_score

    def get_twelveth_score(self):
        return self.__twelveth_score

    def get_previous_stream_compelted(self):
        return self.__previous_stream

    def get_stream_opting_for(self):
        return self.__stream_opting_for

    def get_course_opting_for(self):
        return self.__course_opting_for

    def get_achievements(self):
        return self.__achievements

    def get_status(self):
        return self.__status

    def get_documents(self):
        return self.__documents

    #SET methods

    def set_fname(self,fname):
        self.__first_name = fname
    
    def set_lname(self,lname):
        self.__last_name = lname
    
    def set_gender(self,gender):
        self.__gender= gender
    
    def set_dob(self,dob):
        self.__dob = dob 
    
    def set_phone_no(self,phoneno):
        self.__phone_no = phoneno 
    
    def set_email_id(self,emailid):
        self.__email_id = emailid 
    
    def set_address(self,address):
        self.__address = address 
    
    def set_father_name(self,fathername):
        self.__father_name = fathername 
    
    def set_father_occupation(self,fatheroccupation):
        self.__father_occupation = fatheroccupation
    
    def set_mother_name(self,mothername):
        self.__mother_name = mothername 
    
    def set_mother_occupation(self,motheroccupation):
        self.__mother_occupation = motheroccupation 
    
    def set_category(self,category):
        self.__category = category 
    
    def set_tenth_score(self,tenthscore):
        self.__tenth_score = tenthscore 
    
    def set_twelve_score(self,twelvescore):
        self.__twelveth_score = twelvescore 
    
    def set_previous_stream(self,previousstream):
        self.__previous_stream = previousstream 
    
    def set_opting_stream(self,optingstream):
        self.__stream_opting_for = optingstream 
    
    def set_opting_course(self,optingcourse):
        self.__course_opting_for = optingcourse 
    
    def set_achievements(self,achievements):
        self.__achievements = achievements

    def set_status(self,status):
        self.__status = status

    def check_course_availability(self):
        status = 0
        stream_opted = self.__stream_opting_for
        course_opted = self.__course_opting_for
        for stream, courses in Admission.courses.items():
            if stream != stream_opted:
                continue
            for course_name, seats, fee in courses:
                if course_name == course_opted:
                    status = 1
                    if seats != 0:
                        return True
                    else:
                        return "Unfortunately, seats are not available."
                else:
                    continue
        if status == 0:
            return "Unfortunately, course you're looking for is not available."
                    
    

    def check_eligibility(self):
        '''This function checks the eligibility of a student based on the course he/she has completed and the marks he has scored in his previous grade and the category he belongs to.'''
        marks_scored = self.get_twelveth_score()
        previous_stream = self.get_previous_stream_compelted()
        opting_stream = self.get_stream_opting_for()
        category = self.get_category()

        if previous_stream == "Science" and opting_stream == "Science" or opting_stream == "Commerce" or opting_stream == "Arts":
            if category == "General" and marks_scored > 75:
                return True
            elif category == "SC|ST" or category == "2A" or category == "2B" or category == "3B" and marks_scored > 70:
                return True
            else:
                return "Unfortunately, you are not eligible for this course based on the marks you have scored in your previous grade."

        elif previous_stream == "Commerce" and opting_stream == "Commerce" or opting_stream == "Arts":
            if category == "General" and marks_scored > 80:
                return True
            elif category == "SC|ST" and marks_scored > 60 or category == "2A" and marks_scored > 60  or category == "2B" and marks_scored > 60 or category == "3B" and marks_scored > 60:
                return True
            else:
                return "Unfortunately, you are not eligible for this course based on the marks you have scored in your previous grade."

        elif previous_stream == "Arts" and opting_stream == "Arts":
            if category == "General" and marks_scored > 80:
                return True
            elif category == "SC|ST" or category == "2A" or category == "2B" or category == "3B" and marks_scored > 50:
                return True
            else:
                return "Unfortunately, you are not eligible for this course based on the marks you have scored in your previous grade."
        else:
            return "You cannot opt for this course as you do not have the required educational background."

    def admission_process(self):
        documents = self.get_documents()
        tenth_marks_card = input("Do you have your 10th marks card? Y/N\n")
        twelveth_marks_card = input("Do you have your 12th marks card? Y/N\n")
        aadhar_card = input("Do you have your Aadhar card? Y/N\n")
        code_of_conduct = input("Do you have your code_of_conduct? Y/N\n")
        transfer_cert = input("Do you have your transfer certificate? Y/N\n")

        if tenth_marks_card.upper() == "Y":
            documents["10th_marks_card"] = "Submitted"
        if twelveth_marks_card.upper() == "Y":
            documents["12th_marks_card"] = "Submitted"
        if aadhar_card.upper() == "Y":
            documents["Aadhar_Card"] = "Submitted"
        if code_of_conduct.upper() == "Y":
            documents["Code_of_conduct"] = "Submitted"
        if transfer_cert.upper() == "Y":
            documents["Transfer_certificate"] = "Submitted"

        return True

    def document_submission_check(self):
        documents = self.get_documents()
        if None in documents.values():
            print("Submit the following documents for completing the admission process.")
            for document, status in documents.items():
                if status == "None":
                    print(document)
            return False
        else:
            return True

    def fee_payment(self):
        fee_to_be_paid = 0
        if self.document_submission_check() == True:
            course_info = Admission.courses
            course_opted = self.get_course_opting_for()
            for stream, courses in course_info.items():
                for course_name, seats, fee in courses:
                    if course_name == course_opted:
                        fee_to_be_paid = fee
            answer = input(
                f"Please pay the {fee_to_be_paid} amount to get your admission done. Y/N \n")
            if answer.upper() == "Y":
                return True

