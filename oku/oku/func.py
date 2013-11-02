from django.db import connection
from django.db import connection


cursor = connection.cursor()
cursor.execute("""
    SELECT CityName
    FROM destinations
    WHERE CityName = %s""", ['Ankara'])
row = cursor.fetchone()
print row
