import tkinter as tk
from tkinter import messagebox
from tkinter.simpledialog import askstring

# Define the risk factors and corresponding questions
risk_factors = {
    "smoking": "Do you smoke?",
    "alcohol": "Do you drink alcohol?",
    "exercise": "Do you exercise regularly?",
    "diet": "Do you eat a healthy diet?",
    "stress": "Do you experience a lot of stress?",
    "sleep": "Do you get enough sleep?",
    "sugar_intake": "Do you consume a lot of sugary foods and drinks?"
}

class RiskAssessmentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Risk Assessment Pybot: Envisioning Companion")

        self.assessment_frame = None
        self.result_label = None
        self.responses = {}
        self.greeting_label = None
        self.start_button = None

        for factor in risk_factors:
            self.responses[factor] = tk.StringVar()

        self.create_widgets()
        self.create_assessment_frame()

    def create_widgets(self):
        greeting_text = "Hello, I'm Pybot. I can help you assess your risk for certain health factors.\nClick 'Start Assessment' to begin."
        self.greeting_label = tk.Label(self.root, text=greeting_text, font=("Helvetica", 12))
        self.greeting_label.pack()

        self.start_button = tk.Button(self.root, text="Start Assessment", command=self.start_assessment)
        self.start_button.pack()

        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 12))
        self.result_label.pack()

    def create_assessment_frame(self):
        self.assessment_frame = tk.Frame(self.root)

        for factor, question in risk_factors.items():
            label = tk.Label(self.assessment_frame, text=question)
            yes_button = tk.Button(self.assessment_frame, text="Yes", command=lambda factor=factor: self.set_response(factor, "Yes"))
            no_button = tk.Button(self.assessment_frame, text="No", command=lambda factor=factor: self.set_response(factor, "No"))
            label.pack()
            yes_button.pack()
            no_button.pack()

        assess_button = tk.Button(self.assessment_frame, text="Assess Risk", command=self.risk_assessment)
        assess_button.pack()

    def start_assessment(self):
        self.assessment_frame.pack()
        self.start_button.pack_forget()
        self.greeting_label.pack_forget()

    def set_response(self, factor, response):
        self.responses[factor].set(response)

    def risk_assessment(self):
        risk_score = 0
        risk_factor_responses = []

        for factor in risk_factors:
            response = self.responses[factor].get()
            if response == "Yes":
                risk_score += 1
            risk_factor_responses.append(f"{risk_factors[factor]}: {response}")

        if risk_score == 0:
            result_text = "Congratulations, your risk score is low!"
        elif risk_score <= 2:
            result_text = "Your risk score is moderate. Please consider making some lifestyle changes."
        else:
            result_text = "Your risk score is high. Please consult with a healthcare professional."

        # Accumulate risk factor responses into a single message
        response_message = "\n".join(risk_factor_responses)

        # Create a dialog box to gather additional information
        user_info = askstring("Additional Information", "Would you like to provide your name, age, and contact information? (Yes/No)")

        if user_info and user_info.lower() == "yes":
            info_input = askstring("Additional Information", "Please enter your name, age, and 10-digit contact number, separated by spaces:")
            if info_input:
                info_list = info_input.split()
                if len(info_list) == 3 and info_list[2].isdigit() and len(info_list[2]) == 10:
                    name, age, contact = info_list
                    result_text += f"\nName: {name}\nAge: {age}\nContact: {contact}"
                else:
                    messagebox.showerror("Error", "Invalid input. Please enter name, age, and a 10-digit contact number separated by spaces.")

        # Display the risk factor responses and additional information in a single prompt
        full_message = result_text + "\n\nRisk Factor Responses:\n" + response_message
        messagebox.showinfo("Risk Assessment Result", full_message)

if __name__ == '__main__':
    root = tk.Tk()
    app = RiskAssessmentApp(root)
    root.mainloop()
