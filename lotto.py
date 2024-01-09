import random

def generate_lotto_numbers():
    lotto_numbers = random.sample(range(1, 46), 6)
    return sorted(lotto_numbers)

if __name__ == "__main__":
    lotto_result = generate_lotto_numbers()
    print("생성된 로또 번호: {}".format(lotto_result))