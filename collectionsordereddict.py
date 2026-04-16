from collections import OrderedDict
n = int(input())
item_dict = OrderedDict()
for _ in range(n):
    item_name, _, price = input().rpartition(' ')
    price = int(price)
    if item_name in item_dict:
        item_dict[item_name] += price
    else:
        item_dict[item_name] = price
for name, net_price in item_dict.items():
    print(name, net_price)
