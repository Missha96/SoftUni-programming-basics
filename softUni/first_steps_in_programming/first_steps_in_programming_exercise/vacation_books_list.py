pages_for_book = int(input())
pages_for_one_hour = int(input())
days_for_reading_one_book = int(input())

total_time_for_reading_a_book = pages_for_book // pages_for_one_hour
total_hours_per_day = total_time_for_reading_a_book // days_for_reading_one_book

print(total_hours_per_day)