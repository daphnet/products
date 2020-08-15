# 61 建立記帳程式專案 (+二維清單)

# 比較適合用while loop，
# while loop適用於不確定會執行幾次的狀況
# products要怎麼同時裝入商品名稱跟價格
# solution 1 [name1, price1, name2, price2, name3, price3....]
# solution 2 [name1, name2, name3, name4] & [price1, price2, price3, price4]
# 以上兩法都不好，
# 法一，清單中同時兩種資料，要記住單數筆資料是商品名稱，雙數筆資料是價格
# 法二，拆成兩個清單，商品資訊分在兩個清單儲存，也不方便，要記得每筆的位置，才能互相配對
# 採用兩維清單(2 dimensional)（清單中還有清單）
# 大清單中有小清單，
# [[n1, p1], [n2, p2], [n3,p3], [n4, p4]]


# products = []
# while True:
#     name = input('Please enter product name: ')
#     if name == 'q':
#         break
#     price = input('Please enter price: ')
#     p = []
#     p.append(name)
#     p.append(price)
#     products.append(p)
# print(products)

# print(products[0][0]) # products[0] -> products裏的第0格，products[0][0] -> products第0格裏的第0格
# print(products[1][1]) # products[1] -> products裏的第1格，products[1][1] -> products第1格裏的第1格

# 上面程式可改寫為以下，
# products = []
# while True:
#     name = input('Please enter product name: ')
#     if name == 'q':
#         break
#     price = input('Please enter price: ')
#     # 上面程式可改寫為以下，小清單p可直接定義
#     p = [name, price]
#     products.append(p)
# print(products)

# 上面程式還可以更簡潔，
products = []
while True:
    name = input('Please enter product name: ')
    if name == 'q':
        break
    price = input('Please enter price: ')
    # 直接把小清單放在append裏
    products.append([name, price])
print(products)

# p是小清單
for p in products:
    print(p)

for p in products:
    print(p[0])

for p in products:
    print(p[0], 'price is', p[1])

