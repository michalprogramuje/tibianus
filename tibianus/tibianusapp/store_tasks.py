import requests
from typing import Union
import sys
import psycopg2
import os, sys
import db_settings


def connector(db_settings) -> Union[int, psycopg2.connect]:
    
    try:
        connection = psycopg2.connect(
            user=db_settings.USER,
            password=db_settings.PASSWORD,
            host=db_settings.HOST,
            port = db_settings.PORT,
            database = db_settings.NAME
        )
    except (Exception, psycopg2.Error) as error:
        return error
    else:
        return connection


def make_query():
    try:
        connection = connector(db_settings)

        if type(connection) == psycopg2.OperationalError:
            print(connection)
            exit()
        else:
            cursor = connection.cursor()

            all_ranks = """SELECT * FROM tibianusapp_rank"""


            cursor.execute(all_ranks)
            record = cursor.fetchall()
            print(record)

            # if record == None:
                # current_monster = get_monster_detail_data(url, monster)
                # query = """INSERT INTO tibianusapp_monster (monster_name, monster_exp) VALUES (%s, %s)"""
                    
                #     if('exp' in current_monster):                
                #         if '?' in current_monster['exp'] or '--' in current_monster['exp']:
                #             omitted += 1
                #             continue
                #         else:
                #             if '~' in current_monster['exp']:
                #                 records = (current_monster['name'], current_monster['exp'].replace('~', ''))
                #             else:
                #                 records = (current_monster['name'], current_monster['exp'].replace(',', ''))
                #             cursor.execute(query, records)
                #             connection.commit()
                #             count_rows += 1
                #     else:
                #         continue
                # else:
                #     continue 

            if connection:
                cursor.close()
                connection.close()
                print(f"Gotowe. Dodano {count_rows} rekordów do bazy danych!\nPominiętych zostało {omitted} rekordów (według wytycznych działania algorytmu).")
                print('Połączenie z PostgreSQL zostało zamknięte')   

    except (Exception, psycopg2.Error) as error:
        print("Błąd w przetwarzaniu żądania: ", error)
    
    
    


make_query()

