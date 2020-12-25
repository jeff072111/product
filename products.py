products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	p = []
	p.append(name)
	p.append(price) #7-9行等於快寫 p = [name, price]
	products.append(p)
print(products)
print(products[0][0])

for p in products:
	print(p[0], '的價格為', p[1])
	