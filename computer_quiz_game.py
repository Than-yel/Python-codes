print('WELCOME TO MY COMPUTER QUIZ')

# Initialize score counter
score = 0

# create a variable to ask user if they want to play
playing = input('Do you want to play the game? ')
if playing.lower() != 'yes':
    quit()

print("Alright! Let's play!")

# Ask user the questions
# Question 1
answer = input("1. What does MCP stand for? ")
if answer.lower() == 'model context protocol':
    print('Correct!')
    score += 1
else:
    print('Incorrect! The answer is "Model Context Protocol"')

# Question 2
answer = input("2. Who is the CEO of OpenAI? ")
if answer.lower() == 'sam altman':
    print('Correct!')
    score += 1
else:
    print('Incorrect! The answer is "Sam Altman"')

# Question 3
try:
    answer = float(input("3. What is 28% of 70? "))
    if abs(answer - 19.6) < 0.001:  # This is because computers may accept even an input of 19.5999. So abs means the absolute value
        print('Correct!')
        score += 1
    else:
        print('Incorrect! The answer is 19.6')
except ValueError:
    print('Invalid input! Please enter a number')

# Question 4
try:
    answer = int(input("4. There are 5 observations (1, 2, 3, 4, 5). What is the mean? "))
    if answer == 3:
        print('Correct!')
        score += 1
    else:
        print('Incorrect! The answer is 3')
except ValueError:
    print('Invalid input! Please enter an integer')

# Question 5
answer = input("5. In Linear regression, what is the most common technique? [Full name]: ")
if answer.lower() == 'ordinary least squares':
    print('Correct!')
    score += 1
else:
    print('Incorrect! The answer is "Ordinary Least Squares"')

# Show final score
print(f"\nGAME OVER! Your final score: {score}/5")
print(f"Percentage: {(score/5)*100:.1f}%")