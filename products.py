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
# products = []
# while True:
#     name = input('Please enter product name: ')
#     if name == 'q':
#         break
#     price = input('Please enter price: ')
#     price = int(price)
#     # 直接把小清單放在append裏
#     products.append([name, price])
# print(products)

# # p是小清單
# for p in products:
#     print(p)

# for p in products:
#     print(p[0])

# for p in products:
#     print(p[0], 'price is', p[1])


# 62 寫入檔案
# 63 型別轉換提點
# 64 寫入欄位名稱 + 編碼問題

# 字串可以做 加 跟 乘 合併
# 'abc' + '123' = 'abc123' # 加法常用
# 'abc' * 3 = 'abcabcabc' # 乘法少用
# 同類型資料才能做串接合併，
# 所以如果前面有把price = input()轉換成整數資料型態，
# 底下資料串接時寫入檔案時，就要再用str()轉回字串

# # with open('products.csv', 'w') as f:
# with open('products.csv', 'w', encoding='utf-8') as f:
#     # f.write('name,price\n')
#     f.write('商品,價格\n') # 欄位名稱變亂碼
#     for p in products:
#         f.write(p[0] + ',' + str(p[1]) + '\n')


# 65/66 讀取檔案 + split()

# # 讀取檔案
# products = []
# with open('products.csv', 'r', encoding='utf-8') as f:
#     for line in f:
#         if '商品,價格' in line:
#             continue # 繼續，跳過此次不做，繼續做下一迴
#         # line.strip()，把換行符號及前後空格去除
#         # line.split(',')，遇到逗點就切割
#         name, price = line.strip().split(',')
#         products.append([name, price])
# print(products)

# # 讓使用者輸入
# while True:
#     name = input('Please enter product name: ')
#     if name == 'q':
#         break
#     price = input('Please enter price: ')
#     price = int(price)
#     # 直接把小清單放在append裏
#     products.append([name, price])
# print(products)

# # 印出所有購買紀錄
# for p in products:
#     print(p[0], 'price is', p[1])

# # 寫入檔案
# with open('products.csv', 'w', encoding='utf-8') as f:
#     # f.write('name,price\n')
#     f.write('商品,價格\n') # 欄位名稱變亂碼
#     for p in products:
#         f.write(p[0] + ',' + str(p[1]) + '\n')


# 67. 檢查檔案在不在
# os.path.isfile('file_name')
# 只給檔名->相對路徑，檢查目前目錄裏有沒有這個檔案
# 給完整位址->絕對路徑

import os # import opreating system

# 讀取檔案
products = []

if os.path.isfile('products.csv'): # 檢查檔案是否存在
    print('yes, found the file.')
    with open('products.csv', 'r', encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue # 繼續，跳過此次不做，繼續做下一迴
            # line.strip()，把換行符號及前後空格去除
            # line.split(',')，遇到逗點就切割
            name, price = line.strip().split(',')
            products.append([name, price])
    print(products)

else:
    print('file cannot be found.')

# 讓使用者輸入
while True:
    name = input('Please enter product name: ')
    if name == 'q':
        break
    price = input('Please enter price: ')
    price = int(price)
    # 直接把小清單放在append裏
    products.append([name, price])
print(products)

# 印出所有購買紀錄
for p in products:
    print(p[0], 'price is', p[1])

# 寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f:
    # f.write('name,price\n')
    f.write('商品,價格\n') # 欄位名稱變亂碼
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n')

