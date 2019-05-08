#! python
# quizgame.py - Adapted version of randomQuizGenerator.py from the book
# One quiz, random order, along with the answer key.

import random

# Quiz data (Hexadecimal to binary, 4 bits fixed)
hexa = {'0' : '0000',
        '1' : '00001',
        '2' : '0010',
        '3' : '0011',
        '4' : '0100',
        '5' : '0101',
        '6' : '0110',
        '7' : '0111',
        '8' : '1000',
        '9' : '1001',
        'A' : '1010',
        'B' : '1011',
        'C' : '1100',
        'D' : '1101',
        'E' : '1110',
        'F' : '1111'}

# Generate quiz file

with open('hexabitQuiz.txt', 'w') as quizFile:
    with open('hexabitAns.txt', 'w') as answerFile:

        # Write header for quiz
        quizFile.write('Name:\nDate:\n')
        quizFile.write((' ' * 20) + 'Hexadecimal to binary quiz\n\n')
        answerFile.write((' ' * 20) + 'Hexadecimal to binary answers\n\n')

        # Shuffle order of questions
        hexaDigits = list(hexa.keys())
        random.shuffle(hexaDigits)

        # Loop through all hexa digits, making a question for each
        for i in range(len(hexaDigits) - 1):

            # Get right and wrong answers
            correctAnswer = hexa[hexaDigits[i]]
            wrongAnswers = list(hexa.values())
            del wrongAnswers[wrongAnswers.index(correctAnswer)]
            wrongAnswers = random.sample(wrongAnswers, 3)
            answerOptions = wrongAnswers + [correctAnswer]
            random.shuffle(answerOptions)

            # Write question and answer options
            quizFile.write('{}. Binary representation of {}\n'.format(i + 1, hexaDigits[i]))
            for j in range(4):
                quizFile.write('   {}. {}\n'.format('ABCD'[j], answerOptions[j]))
            quizFile.write('\n')

            # Write answer key to a file
            answerFile.write('{}. {}\n'.format(i + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
