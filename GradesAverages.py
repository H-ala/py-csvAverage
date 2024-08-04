import csv
# For the average
from statistics import mean 

# shows names and their average
def calculate_averages(input_file_name, output_file_name):
    with open(input_file_name) as fin:
        reader = csv.reader(fin)   
        for row in reader:
            name = row[0]
            these_grades = list()
            for grade in row[1:]:
                these_grades.append(float(grade))

            with open(output_file_name, 'a', newline = '') as fout:
                writer = csv.writer(fout)
                writer.writerow([name, mean(these_grades)])
    

# sorted by grades average with their names
def calculate_sorted_averages(input_file_name, output_file_name):
    moratab = dict()
    with open(input_file_name) as fin:
        reader = csv.reader(fin)
        for row in reader:
            name = row[0]
            these_grades = list()
            for grade in row[1:]:
                these_grades.append(float(grade))
                moratab[name] = mean(these_grades)

    result = sorted(list(moratab.items()), key = lambda x: (x[1], x[0]))

    with open(output_file_name, 'a', newline = '') as fout:
        writer = csv.writer(fout)
        writer.writerows(result)


# three best avarages with their student's name
def calculate_three_best(input_file_name, output_file_name):
    moratab = dict()
    with open(input_file_name) as fin:
        reader = csv.reader(fin)
        for row in reader:
            name = row[0]
            these_grades = list()
            for grade in row[1:]:
                these_grades.append(float(grade))
                moratab[name] = mean(these_grades)

    result = sorted(list(moratab.items()), key = lambda x: (-x[1], x[0]))
    i = len(result) - 1

    for this_one in range(3,len(result)):
        del result[i]
        i -= 1
    
    with open(output_file_name, 'a', newline = '') as fout:
        writer = csv.writer(fout)
        writer.writerows(result)


    

# three worst averages without the student's name
def calculate_three_worst(input_file_name, output_file_name):
    moratab = dict()
    with open(input_file_name) as fin:
        reader = csv.reader(fin)
        for row in reader:
            name = row[0]
            these_grades = list()
            for grade in row[1:]:
                these_grades.append(float(grade))
                moratab[name] = mean(these_grades)

    result = sorted(list(moratab.values()))
    i = len(result) - 1

    for this_one in range(3,len(result)):
        del result[i]
        i -= 1


    with open(output_file_name, 'a', newline = '') as fout:
        for nomre in result:
            fout.write('%s\n'% nomre)

    

# show average of averages
def calculate_average_of_averages(input_file_name, output_file_name):
    averages = list()
    with open(input_file_name) as fin:
        reader = csv.reader(fin)
        for row in reader:
            name = row[0]
            these_grades = list()
            for grade in row[1:]:
                these_grades.append(float(grade))
            averages.append(mean(these_grades))
        
    with open(output_file_name, 'a') as fout:
        writer = csv.writer(fout)
        writer.writerow([mean(averages)])

            

calculate_averages('In.csv', 'Out.csv')
# calculate_sorted_averages('In.csv', 'Out.csv')
# calculate_three_best('In.csv', 'Out.csv')
# calculate_three_worst('In.csv', 'Out.csv')
# calculate_average_of_averages('In.csv', 'Out.csv')