# Learn Numbers in Georgian

This is a **Numbers Learning App** built using **PyQt5** to help users, especially children, practice converting numbers into their **Georgian** text representations. The app supports **integers**, **floats**, and **currency** types and dynamically generates quizzes based on the selected type.

The project utilizes the `num2geotext` Python package, which converts numbers into their equivalent Georgian text representations. The app features a graphical user interface (GUI) with radio buttons for selecting the number type, and a quiz system with real-time score updates and smiley feedback based on user performance.

## Features

- **Number Type Selection**: Choose between **Integer**, **Float**, or **Currency** types.
- **Real-Time Quiz**: A dynamic quiz with five questions where users are asked to convert numbers into their Georgian text representations.
- **Score Tracking**: The score is updated after each question and displayed in real-time.
- **Start and Reset**: You can start a new quiz or reset the quiz at any time.

## How to Run the App

### Prerequisites

- **Python 3.x** installed on your machine
- The following Python libraries:
  - `PyQt5`
  - `num2geotext`

You can install the required libraries using pip:

```bash
pip install PyQt5
pip install git+https://github.com/tskhirtladze/num2geotext.git
```

### Running the Application
1. Clone the repository or download the project files.
2. Navigate to the project directory.
3. Run the following command to start the application:

```bash
python app.py
```

## App Usage
1. Select a Number Type: Choose from Integer, Float, or Currency using the radio buttons.
2. Start the Quiz: Click the Start Quiz button to begin the quiz.
3. Answer Questions: Enter your answers in the text field and click Submit to check if your answer is correct.
4. Track Your Score: The score will be displayed after each question. At the end of the quiz, your final score will be shown along with a smiley based on your performance.
5. Reset Quiz: You can reset the quiz at any time using the Reset Quiz button.

