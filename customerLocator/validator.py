with open('gistfile1.txt', 'r') as f:
    customers = f.readlines()

customers = [s.replace('\n', ',') for s in customers]
o=open('customers.json','w')
o.write('{"customers": [')
for ele in customers:
    o.write(ele)
o.write(']}')
o.close()
