def get_score(answer):
    if answer == 1:
        return 0
    elif answer == 2:
        return 1
    elif answer == 3:
        return 2
    elif answer == 4:
        return 3
    else:
        return None

def main():
    questions = [
        "Over the last 2 weeks, how often have you been bothered by little interest or pleasure in doing things?",
        "Over the last 2 weeks, how often have you been bothered by feeling down, depressed, or hopeless?",
        "Over the last 2 weeks, how often have you been bothered by trouble falling or staying asleep, or sleeping too much?",
        "Over the last 2 weeks, how often have you been bothered by feeling tired or having little energy?",
        "Over the last 2 weeks, how often have you been bothered by poor appetite or overeating?",
        "Over the last 2 weeks, how often have you been bothered by feeling bad about yourself or that you are a failure or have let yourself or your family down?",
        "Over the last 2 weeks, how often have you been bothered by trouble concentrating on things, such as reading the newspaper or watching television?",
        "Over the last 2 weeks, how often have you been bothered by moving or speaking so slowly that other people could have noticed, or the opposite, being so fidgety or restless that you have been moving around a lot more than usual?",
        "Over the last 2 weeks, how often have you been bothered by thoughts that you would be better off dead or of hurting yourself?"
    ]

    scores = []

    for question in questions:
        print(question)
        answer = int(input("Select your answer (1. Not at all / 2. Several days / 3. More than half the days / 4. Nearly every day): "))
        score = get_score(answer)
        if score is not None:
            scores.append(score)
        else:
            print("Invalid answer. Please select a valid option (1, 2, 3, or 4).")

    total_score = sum(scores)

    if 1 <= total_score <= 4:
        category = "Minimal depression"
    elif 5 <= total_score <= 9:
        category = "Mild depression"
    elif 10 <= total_score <= 14:
        category = "Moderate depression"
    elif 15 <= total_score <= 19:
        category = "Moderately severe depression"
    elif 20 <= total_score <= 27:
        category = "Severe depression"
    else:
        category = "Invalid score"

    print("\nYour total score is:", total_score)
    print("Based on your score, you have:", category)

if __name__ == "__main__":
    main()
