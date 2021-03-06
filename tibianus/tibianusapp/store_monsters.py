import requests
from typing import Union
import sys
import psycopg2
import os, sys
import db_settings



def make_request(url) -> requests.Response:
    response = requests.get(url)
    return response

def get_status_code(url) -> int:
    response = make_request(url)
    return response.status_code

def get_monsters_data(url) -> Union[requests.Response, int]: 

    if(get_status_code(url) == 200):
        response = make_request(url)
        return response.json()
    return get_status_code(url)


def get_monster_detail_data(url, monster) -> Union[requests.Response, int]: 
    
    monster_url = url + '/' + monster
    if get_status_code(monster_url) == 200:
        response = make_request(monster_url)
        return response.json()
    return get_status_code(monster_url)


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


def make_query(url):

    count_rows = 0
    omitted = 0
    try:
        connection = connector(db_settings)

        if type(connection) == psycopg2.OperationalError:
            print(connection)
            exit()
        else:
            cursor = connection.cursor()
            
            monsters = get_monsters_data(url)
            
            for monster in monsters:

                searched_monster = """SELECT monster_name FROM tibianusapp_monster WHERE monster_name = %s"""
                cursor.execute(searched_monster, (monster,))
                record = cursor.fetchone()

                if record == None:
                    current_monster = get_monster_detail_data(url, monster)
                    query = """INSERT INTO tibianusapp_monster (monster_name, monster_exp) VALUES (%s, %s)"""
                    
                    if('exp' in current_monster):                
                        if '?' in current_monster['exp'] or '--' in current_monster['exp']:
                            omitted += 1
                            continue
                        else:
                            if '~' in current_monster['exp']:
                                records = (current_monster['name'], current_monster['exp'].replace('~', ''))
                            else:
                                records = (current_monster['name'], current_monster['exp'].replace(',', ''))
                            cursor.execute(query, records)
                            connection.commit()
                            count += 1
                    else:
                        continue
                else:
                    continue 

            if connection:
                cursor.close()
                connection.close()
                print(f"Gotowe. Dodano {count_rows} rekord??w do bazy danych!\nPomini??tych zosta??o {omitted} rekord??w (wed??ug wytycznych dzia??ania algorytmu).")
                print('Po????czenie z PostgreSQL zosta??o zamkni??te')   

    except (Exception, psycopg2.Error) as error:
        print("B????d w przetwarzaniu ????dania: ", error)
    
    
    


make_query('https://tibiawiki.dev/api/creatures')

