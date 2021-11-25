import psycopg2
import datetime

# ユーザ情報取得処理

def login(id):
    conn = get_connection()
    cur = conn.cursor()

    sql ="select * from admin where admin_id = %s"

    try:
        cur.execute(sql,(id,))
        print("dbdbdb")
    except Exception as e:
        print("SQL実行に失敗：", e)

    result = cur.fetchone()

    cur.close()
    conn.commit()
    conn.close()
    
    return result

def shopRegistRequist():
    conn = get_connection()
    cur = conn.cursor()

    sql1 ="select req_shop,req_datetime from request where req_flag = 'f' order by req_datetime desc"

    try:
        cur.execute(sql1,())
        print("dbdbdb")
        
    except Exception as e:
        print("SQL実行に失敗：", e)
    result = cur.fetchall()

    cur.close()
    conn.commit()
    conn.close()
    
    return result

def embedRegist(id):
    conn = get_connection()
    cur = conn.cursor()

    sql1 ="select * from request where req_shop = %s"

    try:
        cur.execute(sql1,(id,))
        print("dbdbdb")
        
    except Exception as e:
        print("SQL実行に失敗：", e)
    result = cur.fetchone()

    cur.close()
    conn.commit()
    conn.close()
    
    return result




# DBとのコネクションを取得
def get_connection():
    return psycopg2.connect(dbname='d45d34bc7sh5ac', host='ec2-35-169-204-98.compute-1.amazonaws.com', user='igexshdkbbqyou', password='9b90fd5fa7c6bf65b3c9c57b043c10f4d4589a62b574f7f01b47a3c81a2ef5f5')
