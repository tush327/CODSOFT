import random
from datetime import datetime

class JECRCAdmissionBot:
    """An interactive chatbot to guide students through JECRC University's admission process."""

    negative_responses = ("no", "nope", "nah", "not interested", "sorry")
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")

    random_greetings = (
        "🎓 Welcome to JECRC University Admission Portal! How can I assist you today?",
        "✨ Hello and welcome to JECRC University – where your future begins!",
        "Hi there! Dreaming big? Let's get you admitted to JECRC University!"
    )

    fun_facts = [
        "🏫 JECRC University is ranked among the top private universities in Rajasthan!",
        "🌐 100+ companies visit JECRC for campus placements every year!",
        "📚 We offer state-of-the-art labs, research opportunities, and global collaborations.",
        "🎉 Life at JECRC is not just about academics – enjoy fests, clubs, and vibrant campus culture!"
    ]

    motivational_quotes = [
        "🌟 Remember: Marks don't define you. Passion does.",
        "💪 You're already ahead of those who didn't even try!",
        "🔥 Great things never come from comfort zones – keep going!",
        "🎯 Keep pushing forward. Your journey has just begun.",
        "🚀 Your attitude determines your direction, not just your score."
    ]

    available_courses = {
        "Computer Science": 50000,
        "Mechanical Engineering": 60000,
        "Civil Engineering": 55000,
        "Electrical Engineering": 65000,
        "Business Administration": 40000
    }

    def __init__(self):
        self.admission_details = {}

    def greet(self):
        print(random.choice(self.random_greetings))
        print(random.choice(self.fun_facts))
        self.name = input("\n👋 Can I have your name, please?\n")
        willing_to_apply = input(f"Hi {self.name}, would you like to proceed with your admission at JECRC University? (yes/no)\n")

        if self.make_exit(willing_to_apply):
            return

        if willing_to_apply.lower() in self.negative_responses:
            print("No problem! Wishing you the best for your future!")
            return

        self.ask_course_selection()

    def make_exit(self, reply):
        if reply.lower() in self.exit_commands:
            print("👋 Goodbye! Wishing you a bright future ahead!")
            return True
        return False

    def ask_course_selection(self):
        while True:
            print("\n🎓 Available Courses at JECRC University:")
            for course in self.available_courses:
                print(f"- {course}")
            course = input("\nWhich course would you like to apply for?\n")

            if course.strip().title() in self.available_courses:
                self.admission_details['course'] = course.strip().title()
                self.ask_dob()
                break
            else:
                print("❌ Sorry, that course is not available. Please choose from the listed options.")

    def ask_dob(self):
        while True:
            dob = input("📅 Please enter your Date of Birth (YYYY-MM-DD):\n")
            if self.is_valid_date(dob):
                self.admission_details['dob'] = dob
                self.ask_contact_details()
                break
            else:
                print("❌ Invalid format. Please use YYYY-MM-DD.")

    def ask_contact_details(self):
        while True:
            contact = input("📧 Please enter your contact email or phone number:\n")
            if contact:
                self.admission_details['contact'] = contact
                self.ask_12th_percentage()
                break
            else:
                print("❌ Please enter a valid contact detail.")

    def ask_12th_percentage(self):
        while True:
            try:
                percentage = float(input("📄 What was your 12th-grade percentage?\n"))
                if 0 <= percentage <= 100:
                    self.admission_details['percentage'] = percentage
                    self.ask_entrance_exam_score()
                    break
                else:
                    print("❌ Enter a percentage between 0 and 100.")
            except ValueError:
                print("❌ Please enter a valid number.")

    def ask_entrance_exam_score(self):
        while True:
            try:
                score = float(input("📝 What was your entrance exam score (out of 100)?\n"))
                if 0 <= score <= 100:
                    self.admission_details['exam_score'] = score
                    self.show_course_fee()
                    break
                else:
                    print("❌ Score should be between 0 and 100.")
            except ValueError:
                print("❌ Enter a valid numeric score.")

    def show_course_fee(self):
        course = self.admission_details['course']
        base_fee = self.available_courses[course]
        percentage = self.admission_details['percentage']
        scholarship = 0

        # Scholarship calculation
        if 95 < percentage <= 100:
            scholarship = 0.25
        elif 91 <= percentage <= 95:
            scholarship = 0.20
        elif 86 <= percentage <= 90:
            scholarship = 0.15
        elif 80 <= percentage <= 85:
            scholarship = 0.10

        final_fee = base_fee * (1 - scholarship)

        print(f"\n💰 The standard annual fee for {course} is ₹{base_fee}.")
        if scholarship > 0:
            print(f"🎉 Based on your academic performance, you qualify for a {int(scholarship * 100)}% scholarship!")
            print(f"✅ Your fee after scholarship: ₹{int(final_fee)} per year.")
        else:
            print(f"🧠 Although there's no scholarship this time, JECRC University believes in your potential!")
            print(random.choice(self.motivational_quotes))
            print(f"👉 Your annual fee is ₹{base_fee}. Let's chase success together!")

        self.confirm_application()

    def confirm_application(self):
        confirm = input(f"\n✅ Do you want to submit your application for {self.admission_details['course']}? (yes/no)\n")
        if confirm.lower() == "yes":
            print("\n🎉 Congratulations! Your application to JECRC University has been submitted.")
            print(f"📌 Name: {self.name}")
            print(f"📞 Contact: {self.admission_details['contact']}")
            print(f"🎓 Course: {self.admission_details['course']}")
            print(f"📅 DOB: {self.admission_details['dob']}")
            print("🎊 We will get in touch with you soon. Best of luck!")
        else:
            print("❌ Application canceled. Reach out anytime if you change your mind.")

    def is_valid_date(self, date_string):
        try:
            datetime.strptime(date_string, "%Y-%m-%d")
            return True
        except ValueError:
            return False

# Entry Point
if __name__ == "__main__":
    bot = JECRCAdmissionBot()
    bot.greet()
