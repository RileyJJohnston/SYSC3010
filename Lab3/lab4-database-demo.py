#!/usr/bin/env python3
import sqlite3
#connect to database file
dbconnect = sqlite3.connect("my.db");
#If we want to access columns by name we need to set
#row_factory to sqlite3.Row class
dbconnect.row_factory = sqlite3.Row;
#now we create a cursor to work with db
cursor = dbconnect.cursor();
#execute insetr statement
cursor.execute('''insert into temperature values (4, 2.1, '2013-10-09')''');
dbconnect.commit();

print("\nDisplaying all sensors in kitchen:")
cursor.execute('SELECT * FROM sensors where zone = "kitchen"');
#print data
for row in cursor:
    print(row['sensorID'],row['type'],row['zone'] );
#close the connection

print("\nDisplaying all door sensors:")
cursor.execute('SELECT * FROM sensors where type = "door"');
#print data
for row in cursor:
    print(row['sensorID'],row['type'],row['zone'] );
#close the connection

dbconnect.close();
