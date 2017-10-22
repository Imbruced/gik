class checking:
    def __init__(self):
        print('i am doing sth')


checking_instance = checking()
print(isinstance(checking_instance, checking))

# assert 3==33, 'no wez stary zrob cos'
a = 5
b = 10

a, b = b,a


d = [r for r in range(1, 100)]
p, d, *h = d
print(len(h))