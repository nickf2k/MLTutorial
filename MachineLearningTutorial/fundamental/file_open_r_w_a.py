new_file = open("./file.txt", "r+")
fruits=["Orange\n", "Banana\n", "Apple\n"]
new_file.writelines(fruits)
new_file.seek(0) #dua con tro vao vi tri index 0
read = new_file.readlines()
for line in read:
    print(line)
new_file.close()
