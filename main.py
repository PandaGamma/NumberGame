import random

def guess_number():
    print("Угадай число")
    print("Я загадал число от 1 до 5.")
    
    secret_number = random.randint(1, 5)
    attempts = 0
    
    while True:
        try:
            guess = int(input("\nВведите ваше число: "))
            attempts += 1
            
            if guess < secret_number:
                print("Слишком маленькое число! Попробуйте еще раз.")
            elif guess > secret_number:
                print("Слишком большое число! Попробуйте еще раз.")
            else:
                print(f"Поздравляю! Вы угадали число {secret_number}!")
                print(f"Количество попыток: {attempts}")
                break
                
        except ValueError:
            print("Пожалуйста, введите целое число!")

if __name__ == "__main__":
    guess_number()