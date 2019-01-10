from lib.tree import Tree

tree = Tree(k=int(input('k: ')), k_leaf=int(input('k*: ')))

while True:
    command = input('>> ')
    if command == 'insert':
        tree.insert(int(input('Key: ')), input('Data: '))
    elif command == 'rangeinsert':
        for i in range(int(input('Start: ')), int(input('End: ')) + 1):
            tree.insert(i, str(i))
            print(str(i) + ': ' + str(tree))
    elif command == 'lookup':
        result = tree.lookup(int(input('Key: ')))
        if result is None:
            print(None)
        else:
            print(result.data)
    elif command == 'rangelookup':
        print(tree.rangelookup(int(input('Start: ')), int(input('End: '))))
    elif command == 'print':
        print(tree)
    elif command == 'exit':
        break
