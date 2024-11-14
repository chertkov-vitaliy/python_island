#!/usr/bin/env python
#
# Small script to show PostgreSQL and Pyscopg together
#

import psycopg2

try:
    conn = psycopg2.connect("dbname='test_' user='postgres' host='localhost' password='123'")
    # we use a context manager to scope the cursor session
    with conn.cursor() as curs:

        # simple single row system query
        curs.execute("SELECT version()")

        # returns a single row as a tuple
        single_row = curs.fetchone()

        # use an f-string to print the single tuple returned
        print(f"{single_row}")
except:
    print("I am unable to connect to the database")