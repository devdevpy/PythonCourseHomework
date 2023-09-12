a_price_blank = float(input())
b_price_20_words = float(input())
words_count= float(input())
c_price_per_word = float(input())

total_price = a_price_blank + b_price_20_words + ((words_count - 20) * c_price_per_word)

print(f"{total_price:.2f}")