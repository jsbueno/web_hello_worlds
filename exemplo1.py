import random

def main():
    while True:
        target = random.randint(0, 1000)
        guess = -1
        count = 0
        while guess != target:
            count += 1
            str_guess = input(
                "\nTentativa {} - Adivinhe o número entre 0 e 1000: ".format(count))
            try:
                guess = int(str_guess)
            except ValueError:
                print("\nNúmero inválido\n")
                continue
            if guess < target:
                print ("\nO número é maior que {}".format(guess))
            elif guess > target:
                print ("\nO número é menor que {}".format(guess))
        print("\nParabéns! Você acertou o número {} em {} tentativas!".format(target, count))
        opt = input("Deseja continuar (S/N)? ")
        if len(opt) and opt[0].lower() == "n":
            break

main()