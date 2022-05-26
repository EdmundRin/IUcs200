import sqlite3
import os


# Basic starter code is given below

# Initialize a connection
connection = sqlite3.connect("mydatabase.db")

# Get the cursor to the connection
my_cursor = connection.cursor()

# TODO: Create Table and Insert Values (use the below data to populate the table)
connection.commit()

data = [
    ('Phoenix', 'Arizona', 105, 90),('Tucson', 'Arizona', 101, 92),
    ('Flag Staff', 'Arizona', 105, 90), ('San Diego', 'California', 77, 60),
    ('Albuquerque', 'New Mexico', 80, 72), ('Nome', 'Alaska', 64 ,-54)
]
table_name = "Weather"
columns = "City TEXT, State TEXT, High FLOAT, Low FLOAT"

query = "DROP TABLE IF EXISTS {}".format(table_name)
my_cursor.execute(query)
query = "CREATE TABLE {} ({})".format(table_name, columns)
my_cursor.execute(query)
connection.commit()

for info in data:
    City, State, High, Low = info
    query = "INSERT INTO {} VALUES ('{}', '{}', {}, {})".format(table_name, City, State, High, Low)
    my_cursor.execute(query)
connection.commit()




#-----------------------------------------------------------------------------------------------------------------------
if __name__=="__main__":

    # QUERY 1 Select all the tuples
    print("Query 1")
    for i in my_cursor.execute("SELECT * FROM Weather"):
        print(i)
    print("List Comprehension: ", data)


    # QUERY 2 
    # Select All the tuples where the high temperature is less than 80
    print("\nQuery 2")
    # TODO: Put query here
    for i in my_cursor.execute("SELECT * FROM Weather WHERE High < 80"):
        print(i)
    print("List Comprehension: ", [d for d in data if d[2] < 80 ])


    # QUERY 3 
    # Select All the cities where the low temperature is greater than the low of Albuquerque 
    print("\nQuery 3")
    # TODO: Put query here
    for i in my_cursor.execute("SELECT City FROM Weather WHERE Low > (SELECT Low FROM Weather WHERE City = 'Albuquerque')"):
        print(i)
    print("List Comprehension: ",[d[0] for d in data if d[3] > [d[3] for d in data if d[0] == 'Albuquerque'][0]])


    # QUERY 4 
    # Select the city and temperature with the smallest low temperature 
    print("\nQuery 4")
    # TODO: Put query here
    for i in my_cursor.execute("SELECT City, Low FROM Weather ORDER BY Low ASC LIMIT 1"):
        print(i)
    print("List Comprehension: ",[(d[0],d[3]) for d in data if d[3] in (sorted(data, key = lambda x:x[3])[0])])


    # QUERY 5 
    # Select the city temperature with the largest high temperature 
    print("\nQuery 5")
    # TODO: Put query here
    for i in my_cursor.execute("SELECT City, High FROM Weather ORDER BY High DESC LIMIT 2"):
        print(i)
    print("List Comprehension: ",[(d[0],d[2]) for d in data if d[2] in (sorted(data, key = lambda x:x[2],reverse=True)[0])])


    # QUERY 6 
    # Display the average High and Low temperatures
    # You are not allowed to use Avg()
    print("\nQuery 6")
    # TODO: Put query here
    for i in my_cursor.execute("SELECT avg(High), avg(High) FROM Weather"):
        print(i)
    print("List Comprehension: ", [(sum([d[2] for d in data])/len(data),sum([d[3] for d in data])/len(data))])


    # QUERY 7 
    # Give the counts of cities by their Low temperatures
    print("\nQuery 7")
    # TODO: Put query here
    for i in my_cursor.execute("SELECT Low, count(*) FROM Weather GROUP BY Low"):
        print(i)
    print("List Comprehension: ", [(i,list(map((lambda x: x[3]),data)).count(i)) for i in set(map((lambda x: x[3]),data))])

connection.close()
