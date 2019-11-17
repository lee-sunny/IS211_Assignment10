#!/usr/bin/python
# -*- coding: utf-8 -*-

"""PART II - Existing SQL Database
Second python script to query and display data
query_pets.py"""

import sqlite3 as lite

def main():
    conn = None
    try:
        
        #connect to the database in pets.db
        conn = lite.connect('pets.db')
        while True:
            c = conn.cursor()
            #Ask user for a person's ID number
            user_id = int(input("Enter a person's ID number to query data or -1 to exit: "))
            
            #repeat until user enters -1 to exit the program 
            if user_id == -1:
                break
            
            #if the user exists: print out data on the person and the pet
            cur_query = "SELECT person.first_name, person.last_name, person.age FROM person WHERE id = ?"

            with conn:
                c.execute(cur_query, (user_id,))
                cur_person_data = c.fetchone()
            
            if cur_person_data is not None:
                print("   %s %s is %s years old" % (cur_person_data[0], cur_person_data[1], cur_person_data[2]))

                c.execute("DROP TABLE IF EXISTS person_pet_ids;")

                c.execute(
                    "CREATE TABLE person_pet_ids as SELECT pet_id FROM person_pet WHERE person_id = ?", (user_id,))

                c.execute(
                    "SELECT pet.name, pet.breed, pet.age, pet.dead FROM pet JOIN person_pet_ids ON person_pet_ids.pet_id = pet.id;")

                data = c.fetchall()

                for cur_data in data:
                    print("   %s %s is the owner of %s, a %s that is %d years old" % (cur_person_data[0], cur_person_data[1], cur_data[0], cur_data[1], cur_data[2]))

            #if the user does not exist: print an error message
            else:
                print("***No person exists by that person ID number. Please try again.")
                
        conn.commit()
    except lite.Error as e:
        print("Error")
    finally:
        if conn:
            conn.close()

main()
