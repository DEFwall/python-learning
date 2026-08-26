num = int(input())
ch1 = num // 100
ch2 = (num // 10) % 10
ch3 = num % 10
print(num)
print(ch1 * 100 + ch3 * 10 + ch2)
print(ch2 * 100 + ch1 * 10 + ch3)
print(ch2 * 100 + ch3 * 10 + ch1)
print(ch3 * 100 + ch1 * 10 + ch2)
print(ch3 * 100 + ch2 * 10 + ch1)
