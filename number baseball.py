import random

def generate_random_number():
    return random.sample(range(0, 10), 4)

def evaluate_guess(secret_number, user_guess):
    strikes = sum([1 for i in range(4) if secret_number[i] == user_guess[i]])
    balls = sum([1 for i in range(4) if user_guess[i] in secret_number and user_guess[i] != secret_number[i]])

    return strikes, balls

def baseball_game():
    print("4자리 숫자 야구 게임을 시작합니다. 0부터 9까지의 서로 다른 네 자리 숫자를 맞춰보세요.")

    secret_number = generate_random_number()
    attempts = 0

    while True:
        user_input = input("네 자리 숫자를 입력하세요: ")

        if len(user_input) != 4 or not user_input.isdigit():
            print("올바른 형식의 숫자를 입력하세요.")
            continue

        user_guess = [int(digit) for digit in user_input]

        if len(set(user_guess)) != 4:
            print("서로 다른 숫자를 입력하세요.")
            continue

        attempts += 1

        strikes, balls = evaluate_guess(secret_number, user_guess)

        print("결과: { } 스트라이크, { } 볼".format(strikes, balls))

        if strikes == 4:
            print("축하합니다! { }번 만에 숫자를 맞추셨습니다.".format(attempts))
            break

if __name__ == "__main__":
    baseball_game()