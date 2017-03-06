fw = open('example.txt', 'w')
fw.write('hello, world\n' 'hehehehehehe')
fw.close()

fr = open('example.txt', 'r')
example = fr.read()
print(example)
fr.close()