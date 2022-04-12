import psycopg2
import os

from sqlalchemy import true
class DataBase:

    #DB情報取得
    def connect():

        # 本番環境


        DBFLG = true

        if DBFLG:
            # 本番環境
            POSTGRES_URL ='postgres ：// ifnxktkdxwankq ：07c61dd3a3d8e7e6b73f58038695a8ebb9e994a92d93651abbfe14121e198674 @ ec2-34-207-12-160.compute-1.amazonaws.com：5432 / d360nfch4hl8mt'
        else:
            # LOCAL環境
            POSTGRES_URL = 'host=localhost port=5432 dbname=PGLOCAL user=postgres password=postgres'
        
        con = psycopg2.connect('POSTGRES_URL')

        print("DB接続を開始しました")
        return con

    #SELECTを実行
    def select_execute(con, sql):
        with con.cursor() as cur:
            cur.execute(sql)
            rows = cur.fetchall()
        return rows
    #UPDATEを実行
    def updatet_execute(con, sql):
        with con.cursor() as cur:
            cur.execute(sql)
        con.commit()
    #INSERTを実行
    def insert_execute(con, sql):
        with con.cursor() as cur:
            cur.execute(sql)
        con.commit()
    #DELETEを実行
    def delete_execute(con, sql):
        with con.cursor() as cur:
            cur.execute(sql)
        con.commit()