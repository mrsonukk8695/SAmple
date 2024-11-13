questions = [
    {
        "prompt" : "What is the capital of France?",
        "options": ["A. Paris","B. London", "C. Berlin", "D. Madrid" ],
        "answer" : "A"
    },

    {
        "prompt" : "Who is the author of the novel 'Pride and Prejudice'?",
        "options": ["A. Jane Austen","B. Charles Dickens", "C. Mark Twain", "D. Ernest Hemingway" ],
        "answer" : "A"
    },
    
    {
        "prompt" : "What is the largest ocean in the world?",
        "options": ["A. Pacific Ocean","B. Atlantic Ocean", "C. Indian Ocean", "D. Arctic Ocean" ],
        "answer" : "D"
    },

    {
        "prompt" : "What is the primary currency of South Africa?",
        "options": ["A. Rand","B. Zimbabwe Dollar", "C. Euro", "D. South African Rand" ],
        "answer" : "D"
    },
    
    {
        "prompt" : "Who wrote the novel 'To Kill a Mockingbird'?",
        "options": ["A. Harper Lee","B. Mark Twain", "C. J.K. Rowling", "D. Ernest Hemingway" ],
        "answer" : "A"
    },

    {
        "prompt" : "Which famous American author wrote the novel '1984'?",
        "options": ["A. George Orwell","B. Charles Dickens", "C. Mark Twain", "D. Harper Lee" ],
        "answer" : "A"
    }
]

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        user_answer = input("Enter your answer(A, B, C or D): ")
        if user_answer.upper() == question["answer"]:
            score += 1
            print("Correct, hooray!! \n")
        else:
            print(f"Sorry, the correct answer is {question['answer']}. \n")
    print(f"Your final score is {score}/{len(questions)}")

run_quiz(questions)