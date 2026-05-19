from math import floor, ceil

tennis_racket_price = float(input())
tennis_racket_qty = int(input())
trainers_qty = int(input())

trainers_price = tennis_racket_price / 6
total_racket = tennis_racket_qty * tennis_racket_price
total_trainers = trainers_price * trainers_qty
trainers_rackets = total_trainers + total_racket
other_equipment = trainers_rackets * 0.20
grand_total = trainers_rackets + other_equipment

paid_by_him = grand_total / 8
paid_by_trainers = grand_total - paid_by_him
print(f'Price to be paid by Djokovic {floor(paid_by_him)}')
print(f'Price to be paid by sponsors {ceil(paid_by_trainers)}')
