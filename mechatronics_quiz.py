# Mechatronics Quiz App
# Author: Solomon
# ND2 Mechatronics Engineering, YabaTech

def ask_question(question, options, correct_answer):
    """Ask one question and return True if the answer is correct."""
    print("\n" + question)
    for option in options:
        print(option)
    
    while True:
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer in ["A", "B", "C", "D"]:
            break
        print("Invalid input. Please enter A, B, C or D only.")
    
    if answer == correct_answer:
        print("Correct!")
        return True
    else:
        print(f"Wrong. The correct answer is {correct_answer}.")
        return False


def calculate_percentage(score, total):
    """Calculate and return the percentage score."""
    return (score / total) * 100


def main():
    # List of questions: [question, options list, correct answer]
    questions = [
        [
            "1. What does a sensor do in a mechatronic system?",
            ["A. Provides power", "B. Detects physical quantities", "C. Stores data permanently", "D. Amplifies signals only"],
            "B"
        ],
        [
            "2. Which of these is an actuator?",
            ["A. Temperature sensor", "B. DC motor", "C. LCD display", "D. Arduino board"],
            "B"
        ],
        [
            "3. PLC stands for:",
            ["A. Programmable Logic Controller", "B. Power Line Control", "C. Personal Laptop Computer", "D. Pulse Level Converter"],
            "A"
        ],
        [
            "4. Ohm's Law is:",
            ["A. V = I × R", "B. P = I × R", "C. V = I / R", "D. I = V × R"],
            "A"
        ],
        [
            "5. Which microcontroller is popular for beginners?",
            ["A. Raspberry Pi only", "B. Arduino", "C. Desktop CPU", "D. Graphics card"],
            "B"
        ]
    ]

    print("=== Mechatronics Quiz App ===")
    print("Answer each question with A, B, C or D.\n")

    score = 0
    total = len(questions)

    for q in questions:
        if ask_question(q[0], q[1], q[2]):
            score += 1

    percentage = calculate_percentage(score, total)

    print("\n========== RESULT ==========")
    print(f"You scored {score} out of {total}")
    print(f"Percentage: {percentage:.1f}%")

    if percentage >= 80:
        print("Grade: A  Excellent work!")
    elif percentage >= 60:
        print("Grade: B  Good job!")
    elif percentage >= 40:
        print("Grade: C  Keep practising.")
    else:
        print("Grade: D  Review the topics and try again.")

    print("============================")


if __name__ == "__main__":
    main()
