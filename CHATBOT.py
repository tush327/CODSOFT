import random
from datetime import datetime

class CollegeAdmissionBot:
    """A rule-based chatbot that assists students in the college admission process."""

    negative_responses = ("no", "nope", "nah", "naw", "not interested", "sorry")
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")
    random_greetings = (
        "Welcome to the College Admission Portal! How can I assist you today?",
        "Hello! Ready to start your college application? I'm here to help!",
        "Hi there! Want to know more about the admission process? I can help with that!"
    )

    # Predefined available courses and their fees
    available_courses = {
        "Computer Science": 50000,  # INR
        "Mechanical Engineering": 60000,  # INR
        "Civil Engineering": 55000,  # INR
        "Electrical Engineering": 65000,  # INR
        "Business Administration": 40000  # INR
    }

    def __init__(self):
        self.admission_details = {}

    def greet(self):
        print(random.choice(self.random_greetings))
        self.name = input("Can I have your name, please?\n")
        willing_to_apply = input(f"Hi {self.name}, would you like to proceed with your college admission application?\n")

        if self.make_exit(willing_to_apply):
            return

        if willing_to_apply.lower() in self.negative_responses:
            print("No problem! Good luck with everything!")
            return

        self.ask_course_selection()

    def make_exit(self, reply):
        if reply.lower() in self.exit_commands:
            print("Goodbye! Have a great day ahead!")
            return True
        return False

    def ask_course_selection(self):
        """Ask the user to select a course for admission."""
        while True:
            print("Here are the available courses:")
            for course in self.available_courses.keys():
                print(f"- {course}")
            course = input("Which course would you like to apply for?\n")

            if course.capitalize() in self.available_courses:
                self.admission_details['course'] = course.capitalize()
                self.ask_dob()
                break
            else:
                print("Sorry, that course is not available. Please select from the listed options.")

    def ask_dob(self):
        """Ask for the student's date of birth."""
        while True:
            dob = input("Please enter your Date of Birth (YYYY-MM-DD):\n")
            if not self.is_valid_date(dob):
                print("Invalid date format. Please use YYYY-MM-DD.")
                continue
            self.admission_details['dob'] = dob
            self.ask_12th_percentage()
            break

    def ask_12th_percentage(self):
        """Ask for the student's 12th-grade percentage."""
        while True:
            try:
                percentage = float(input("What is your 12th-grade percentage?\n"))
                if percentage < 0 or percentage > 100:
                    print("Please enter a valid percentage between 0 and 100.")
                    continue
                self.admission_details['percentage'] = percentage
                self.ask_entrance_exam_score()
                break
            except ValueError:
                print("Please enter a valid percentage.")

    def ask_entrance_exam_score(self):
        """Ask for the student's entrance exam score."""
        while True:
            try:
                score = float(input("What is your entrance exam score (out of 100)?\n"))
                if score < 0 or score > 100:
                    print("Please enter a valid score between 0 and 100.")
                    continue
                self.admission_details['exam_score'] = score
                self.show_course_fee()
                break
            except ValueError:
                print("Please enter a valid score.")

    def show_course_fee(self):
        """Calculate and show the fee for the selected course."""
        course = self.admission_details['course']
        fee = self.available_courses[course]
        print(f"\nThe fee for the {course} course is ₹{fee} per year.")

        # Check if the student is eligible for a scholarship
        if self.admission_details['percentage'] > 85 and self.admission_details['exam_score'] > 75:
            scholarship = 0.2 * fee  # 20% scholarship
            print(f"🎉 Congratulations! You are eligible for a 20% scholarship, reducing your fee to ₹{fee - scholarship} per year.")
        else:
            print(f"Your total fee remains ₹{fee} per year.")

        self.confirm_application()

    def confirm_application(self):
        """Ask the student to confirm their application."""
        confirm = input(f"Do you want to submit your application for the {self.admission_details['course']} course? (yes/no)\n")
        if confirm.lower() == "yes":
            print("Your application has been submitted! Best of luck with the admission process!")
        else:
            print("Application canceled. Let me know if you need any further assistance.")

    def is_valid_date(self, date_string):
        try:
            datetime.strptime(date_string, "%Y-%m-%d")
            return True
        except ValueError:
            return False

# Entry point
if __name__ == "__main__":
    bot = CollegeAdmissionBot()
    bot.greet()
