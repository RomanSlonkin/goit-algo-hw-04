def get_cats_info(path):
    '''Function to sort info from file to list'''
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            cats_info = list()
            for line in lines:
                cat = dict(id = line.split(',')[0], name = line.split(',')[1], age = int(line.split(',')[2]))
                cats_info.append(cat)
            return cats_info     

    except (FileNotFoundError, IOError) :
            print('File not found or broken!')

cats_info = get_cats_info("task2/cats_info.txt") #test
print(cats_info) #test
#EOF
