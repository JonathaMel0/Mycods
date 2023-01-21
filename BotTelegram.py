import requests
import psycopg2 as psql
from datetime import datetime
from time import sleep

con = psql.connect(host='######', database='postgres',  ####<-host BD
user='postgres', password='admin123')
cur = con.cursor()
#sql = 'create table cidade (id serial primary key, nome varchar(100), uf varchar(2))'
#cur.execute(sql)
#sql = "insert into cidade values (default,'São Paulo,'SP')"
#cur.execute(sql)
con.commit()
cur.execute("SELECT * from id_clientes")
recset = cur.fetchall()
dt = recset[0][0]
#dt = datetime #.strftime('%Y-%m-%d %H:%M:%S')
#print(dt)
con.close()

req = requests.get('https://economia.awesomeapi.com.br/json/last/USD-BRL')
reqjson = req.json()
cotacao = reqjson['USDBRL']['bid']




# enviar mensagens utilizando o bot para um chat específico
def send_message(token, chat_id, message, parse_mode):
    try:
        data = {"chat_id": chat_id, "text": msg, "parse_mode": parse_mode}
        url = "https://api.telegram.org/bot{}/sendMessage".format(token)
        requests.post(url, data, parse_mode)
    except Exception as e:
        print("Erro no sendMessage:", e)

#VARIÁVEIS
token = '######' #<-token telegram bot
parse_mode = 'HTML'
data = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

# id do chat
chat_id = '#######'<-chat id do telegram
#print("Id do chat:", chat_id)

# O QUE SERÁ ENVIADO
msg = f"""Cotação dólar atual: <b>{cotacao}</b>

<b>{data}</b>
"""
#msg = """<b>Bom dia!</b> 
#Última operação registrada do banco <b>BI</b> é <code>{}</code>. Esta data é para considerar se banco de dados foi atualizado normalmente.""".format(data) 
#msg = '<b>bold</b>, <strong>bold</strong>'
#msg = '<i>italic</i>, <em>italic</em>'
#msg = '<u>underline</u>, <ins>underline</ins>'
#msg = '<s>strikethrough</s>, <strike>strikethrough</strike>, <del>strikethrough</del>'
#msg = '<b>bold <i>italic bold <s>italic bold strikethrough</s> <u>underline italic bold</u></i> bold</b>'
#msg = '<a href="http://www.example.com/">inline URL</a>'
#msg = '<a href="tg://user?id=123456789">inline mention of a user</a>'
#msg = '<code>inline fixed-width code</code>'
#msg = '<pre>pre-formatted fixed-width code block</pre>'
#+ ' ' + data



## ENVIAR IMAGEM
def enviar_imagem(file_path):
    body = {
        'chat_id': chat_id,
    }
    files = {
        'photo': open(file_path, 'rb')
    }
    r = requests.post('https://api.telegram.org/bot{}/sendPhoto'.format(
    token), data=body, files=files)

    if r.status_code >= 400:
        print('Houve um erro ao enviar mensagem. Detalhe: {}'.format(r.text))
    else:
        print('Imagem enviada com sucesso.')


enviar_imagem('C:/Pasta dos Arquivos/enviar_foto_telegram/enviar.png')


 #ENVIO DA MENSAGEM
send_message(token, chat_id, msg, parse_mode)







