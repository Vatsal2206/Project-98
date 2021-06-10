def swapping():
    with open('file1.txt', 'r') as a:
        file1_data = a.read()
    with open('file2.txt', 'r') as b:
        file2_data = b.read()

    with open('file1.txt', 'w') as a:
        a.write(file2_data)
    
    with open('file2.txt', 'w') as b:
        b.write(file1_data)

    print('File1:'+file1_data)
    print('File2:'+file2_data)

swapping()
