print("***QUIZ WORLD***")
print("Wellcome to Python quiz game !!")
playing = input('Do you want to play ? ').lower()
if playing == 'yes':
    print(" ***ALL THE BEST**")
    questions = (" Who developed Python Programming Language?: ",
                       "Which type of Programming does Python support?: ",
                       " Is Python case sensitive when dealing with identifiers?: ",
                       " Which of the following is the correct extension of the Python file?: ",
                       " All keywords in Python are in ?: ")

    options = (("A. Wick van Rossum", "B. Rasmus Lerdorf", "C. Guido van Rossum", "D. Niene Stom"),
                   ("A. object-oriented programming", "B. structured programming", "C.  functional programming", "D.all of the mentioned"),
                   ("A. no", "B.  yes", "C. machine dependent", "D.  none of the mentioned"),
                   ("A.  .python", "B. .pl", "C. .py", "D. .p"),
                   ("A.Capitalized ", "B.lower case ", "C. UPPER CASE", "D.none of the mentioned"))
                   

    answers = ("C", "D", "B", "C", "D")
    guesses = []
    score = 0
    question_num = 0

    for question in questions:
        print("----------------------")
        print(question)
        for option in options[question_num]:
            print(option)

        guess = input("Enter (A, B, C, D): ").upper()
        guesses.append(guess)
        if guess == answers[question_num]:
            score += 1
            print("CORRECT!")
        else:
            print("INCORRECT!")
            print(f"{answers[question_num]} is the correct answer")
        question_num += 1

    print("----------------------")
    print("       RESULTS        ")
    print("----------------------")

    print("answers: ", end="")
    for answer in answers:
        print(answer, end=" ")
    print()

    print("guesses: ", end="")
    for guess in guesses:
        print(guess, end=" ")
    print()

    score = int(score / len(questions) * 100)
    print(f"Your score is: {score}%")
else:
    print('thankyou you are out of a game.')
    quit()