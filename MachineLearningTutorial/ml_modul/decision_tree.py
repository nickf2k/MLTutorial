from sklearn import tree


# bước 1: thu thập data
# bước 2: xử lí dữ liệu
# bước 3: training model
# bước 4: dự đoán kết quả
# bước 5: đánh giá model
dtree = tree.DecisionTreeClassifier()
dac_trung = [[1, 3, 3, 7],
             [5, 2, 4, 6],
             [1, 2, 4, 6],
             [5, 4, 4, 3],
             [1, 4, 4, 7],
             [3, 2, 3, 7],
             [3, 3, 3, 6],
             [5, 2, 2, 7]]
label = [0, 1, 1, 0, 0, 0, 0, 1]
res = dtree.fit(dac_trung,label)
kq = dtree.predict([[1,4,3,6], [3,2,1,1]]) # mang 2 chieu de nhan biet nhieu kq hon
print(kq)