import random

# Number of colors in the code
# R = Red
# G = Green
# B = Blue
# Y = Yellow
# W = White
# O = Orange
COLORS = ['R', 'G', 'B', 'Y', 'W', 'O']
TRIES = 15
CODE_LENGTH = 4

def generate_code():
    code = []
    
    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color) 
        
        return code
    
def guess_code():
    
    while True:
        guess = input('Enter your guess: ').upper().split(" ")
        
        if len(guess) != CODE_LENGTH:
            print('You must enter exactly 4 colors')
            continue
        
        for color in guess:
            if color not in COLORS:
                print(f'Invalid color: {color}')
                break
        else:
            break
        
    return guess

def check_code(guess, real_code):
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0
    
    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1
        
    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_pos += 1
            color_counts[guess_color] -= 1
            
    for guess_color, real_color in zip(guess, real_code):
        if guess_color in color_counts and color_counts[guess_color] > 0 and guess_color != real_color:
            incorrect_pos += 1
            color_counts[guess_color] -= 1 
            
    return correct_pos, incorrect_pos

def main():
    print('Welcome to Mastermind!')
    print('The available colors are: R, G, B, Y, W, O')
    print('You have to guess the 4 colors in the correct order')
    print(f'You have {TRIES} tries to guess the code')
    
    code = generate_code()
    for attempts in range(1, TRIES + 1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)
        
        if correct_pos == CODE_LENGTH:
            print(f'Congratulations! You have guessed the code in {attempts} attempts')
            break
        
        print(f"Correct position: {correct_pos} | Incorrect position: {incorrect_pos}")
        
    else:
        print('You lose! The code was', *code)
        
if __name__ == '__main__':
    main()
    