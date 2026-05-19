prime_sum = 0
non_prime_sum = 0

while True:

    entry = input()

    if entry == "stop":
        break

    num = int(entry)

    if num < 0:
        print("Number is negative.")

        continue

    if num < 2:

        non_prime_sum += num

    else:

        is_prime = True

        for i in range(2, int(num ** 0.5) + 1):

            if num % i == 0:
                is_prime = False

                break

        if is_prime:

            prime_sum += num

        else:

            non_prime_sum += num

print(f"Sum of all prime numbers is: {prime_sum}")

print(f"Sum of all non prime numbers is: {non_prime_sum}")