import random
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QRadioButton, QButtonGroup, QPushButton, \
    QLineEdit, QMessageBox, QFrame
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt
from num2geotext import int_num_to_geo_text, float_num_to_geo_text, float_num_to_geo_currency


class LearnNumbersInGeorgian(QWidget):
    def __init__(self):
        super().__init__()

        # Window setup
        self.setWindowTitle("Learn Numbers in Georgian")
        self.setGeometry(100, 100, 400, 500)
        self.setStyleSheet("background-color: #f0f0f0;")

        # Score and settings
        self.score = 0
        self.num_questions = 10
        self.current_question = 0
        self.number = None
        self.correct_answer = None
        self.number_type = "Integer"
        self.quiz_active = False  # To track if the quiz is active or not

        # Create main layout
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Header
        self.header = QLabel("Learn Numbers in Georgian", self)
        self.header.setFont(QFont("Arial", 22, QFont.Bold))
        self.header.setStyleSheet("color: #333;")
        self.header.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.header)

        # Number type label (to display selected type)
        self.number_type_label = QLabel(f"Selected Type: {self.number_type}")
        self.number_type_label.setFont(QFont("Arial", 16))
        self.number_type_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.number_type_label)

        # Number type selection
        self.type_label = QLabel("Select Number Type:")
        self.layout.addWidget(self.type_label)

        # Radio buttons for number type selection (Integer, Float, Currency)
        self.integer_button = QRadioButton("Integer")
        self.float_button = QRadioButton("Float")
        self.currency_button = QRadioButton("Currency")
        self.integer_button.setChecked(True)

        # Button group to manage number type radio buttons
        self.type_group = QButtonGroup()
        self.type_group.addButton(self.integer_button)
        self.type_group.addButton(self.float_button)
        self.type_group.addButton(self.currency_button)

        # Add number type radio buttons to layout
        self.layout.addWidget(self.integer_button)
        self.layout.addWidget(self.float_button)
        self.layout.addWidget(self.currency_button)

        # Start button
        self.start_button = QPushButton("Start Quiz")
        self.start_button.setStyleSheet("background-color: #5cb85c; color: white; font-size: 16px;")
        self.start_button.clicked.connect(self.start_quiz)
        self.layout.addWidget(self.start_button)

        # Question display frame
        self.question_frame = QFrame(self)
        self.question_frame.setStyleSheet("background-color: #fff; border-radius: 10px; padding: 20px;")
        self.question_layout = QVBoxLayout()
        self.question_frame.setLayout(self.question_layout)
        self.layout.addWidget(self.question_frame)

        # Question label
        self.question_label = QLabel("")
        self.question_label.setFont(QFont("Arial", 16))
        self.question_layout.addWidget(self.question_label)

        # Answer input field
        self.answer_entry = QLineEdit()
        self.answer_entry.setPlaceholderText("Type your answer in Georgian")
        self.answer_entry.setStyleSheet("padding: 10px; border: 1px solid #ccc; border-radius: 5px;")
        self.question_layout.addWidget(self.answer_entry)

        # Submit button
        self.submit_button = QPushButton("Submit Answer")
        self.submit_button.setStyleSheet("background-color: #007bff; color: white; font-size: 16px;")
        self.submit_button.clicked.connect(self.check_answer)
        self.question_layout.addWidget(self.submit_button)

        # Score display
        self.score_label = QLabel("Score: 0/0")
        self.score_label.setFont(QFont("Arial", 16))
        self.score_label.setStyleSheet("color: #333;")
        self.score_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.score_label)

        # Final message box
        self.final_message = QLabel("")
        self.final_message.setFont(QFont("Arial", 16))
        self.final_message.setStyleSheet("color: #333;")
        self.final_message.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.final_message)

        # Smiley display label
        self.smiley_label = QLabel("")
        self.smiley_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.smiley_label)

        # Reset button
        self.reset_button = QPushButton("Reset Quiz")
        self.reset_button.setStyleSheet("background-color: #d9534f; color: white; font-size: 16px;")
        self.reset_button.clicked.connect(self.reset_quiz)
        self.layout.addWidget(self.reset_button)

        # Disable answer input and submit button initially
        self.answer_entry.setEnabled(False)
        self.submit_button.setEnabled(False)

    def set_number_type(self):
        """Sets the number type based on the selected radio button and updates the label."""
        if self.integer_button.isChecked():
            self.number_type = "Integer"
        elif self.float_button.isChecked():
            self.number_type = "Float"
        elif self.currency_button.isChecked():
            self.number_type = "Currency"

        # Update the number type display label
        self.number_type_label.setText(f"Selected Type: {self.number_type}")

    def generate_question(self):
        # Set number type
        self.set_number_type()

        # Generate random number and get the correct Georgian text based on the number type
        if self.number_type == "Integer":
            self.number = random.randint(1, 100)
            self.correct_answer = int_num_to_geo_text(self.number)
        elif self.number_type == "Float":
            self.number = round(random.uniform(1, 100), 2)
            self.correct_answer = float_num_to_geo_text(self.number)
        elif self.number_type == "Currency":
            self.number = round(random.uniform(1, 1000), 2)
            self.correct_answer = float_num_to_geo_currency(self.number)

        # Display the question
        self.question_label.setText(f"What is {self.number} in Georgian?")
        self.answer_entry.clear()

        # Enable input field and submit button when quiz is active
        self.answer_entry.setEnabled(True)
        self.submit_button.setEnabled(True)

        # Update score label
        self.score_label.setText(f"Score: {self.score}/{self.current_question}")

    def start_quiz(self):
        self.score = 0
        self.current_question = 0
        self.quiz_active = True
        self.smiley_label.clear()  # Clear smiley on new quiz start
        self.generate_question()

    def check_answer(self):
        if not self.quiz_active:
            return  # Do nothing if the quiz is not active

        user_answer = self.answer_entry.text().strip()

        # Check if the user's answer matches the correct answer
        if user_answer == self.correct_answer:
            QMessageBox.information(self, "Correct!", "Good job!")
            self.score += 1
        else:
            QMessageBox.warning(self, "Wrong!", f"Correct answer: {self.correct_answer}")

        # Move to the next question or finish the quiz
        self.current_question += 1
        self.score_label.setText(f"Score: {self.score}/{self.current_question}")  # Update score during answering

        if self.current_question < self.num_questions:
            self.generate_question()
        else:
            self.show_score()
            self.quiz_active = False  # End the quiz
            self.submit_button.setEnabled(False)  # Disable submit button after finishing the quiz
            self.answer_entry.setEnabled(False)  # Disable the answer entry after finishing the quiz

    def show_score(self):
        self.final_message.setText(f"Your final score: {self.score}/{self.num_questions}")

        # Show smiley based on score
        if self.score == 5:
            smiley_path = "smileys/happy.png"
        elif self.score <= 2:
            smiley_path = "smileys/sad.png"
        else:
            smiley_path = "smileys/excited.png"

        pixmap = QPixmap(smiley_path)
        self.smiley_label.setPixmap(pixmap)

    def reset_quiz(self):
        self.score = 0
        self.current_question = 0
        self.quiz_active = False  # Mark quiz as inactive during reset
        self.final_message.setText("")
        self.question_label.setText("")
        self.answer_entry.clear()
        self.submit_button.setEnabled(False)  # Disable submit button when resetting the quiz
        self.answer_entry.setEnabled(False)  # Disable answer entry when resetting the quiz
        self.score_label.setText("Score: 0/0")  # Reset the score label
        self.smiley_label.clear()  # Clear smiley image on reset
        self.start_quiz()  # Start the quiz again with new questions


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LearnNumbersInGeorgian()
    window.show()
    sys.exit(app.exec_())
