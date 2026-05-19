shirt_price = float(input())
target_sum = float(input())

pants_price = shirt_price * 0.75
socks_price = pants_price * 0.20
trainers = (shirt_price + pants_price) * 2
total_sum = (pants_price + shirt_price + socks_price + trainers) * 0.85
if target_sum < total_sum:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {total_sum:.2f} lv.")
else:
    print(f"No, he will not earn the world-cup replica ball.")
    print(f"He needs {abs(total_sum - target_sum):.2f} lv. more.")
