#PhoneBook
import csv

# csv.writer
# writerow

"""with open('num.csv', mode='w') as test1:
    test_writer = csv.writer(test1, delimiter=',')
    test_writer.writerow(['Piaz', '7894564'])
    test_writer.writerow(['Apple', '564654465'])
    test_writer.writerow(['Pineapple', '24654875'])
    test_writer.writerow(['Parrot', '84054054'])"""

with open('num.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row[0], row[1])