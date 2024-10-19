def total_salary(path):
    """Function to analyze salaries in given file"""
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            salaries = list()
            for line in lines:
                salaries.append(float(line.split(',')[1]))
            total = sum(salaries)
            average = float(total/len(salaries))
            return total, average

    except ValueError:
         print('Not enough data to proceed')

    except (FileNotFoundError, IOError) :
            print('File not found or broken!')
    

total, average = total_salary("task1\salary_file.txt") #test
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average} ") #test
#EOF