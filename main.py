import random

def guess_number():
    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 1 до 100. Попробуй угадать!")
    
    # Компьютер загадывает случайное число
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            # Пользователь вводит свою догадку
            guess = int(input("\nВведите ваше число: "))
            attempts += 1
            
            # Проверяем догадку
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

# Запускаем игру
if __name__ == "__main__":
    guess_number()