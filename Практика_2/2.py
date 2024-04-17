a = {'title': 'Hello', 'description': 'world', 'price': '3'}
b = {'python': 'lang', 'key:': '#789', 'title': 'Hello', 'description': 'world', 'price': '3'}
a_b = a.keys()-b.keys()
b_a = b.keys()-a.keys()

if a_b:
    print(a_b)
if b_a:
    print(b_a)