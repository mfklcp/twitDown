#MINERAÇÃO DE DADOS - UFMA
#JULIA E MARCIO
#ANALISE DE SENTIMENTO - TWITTER

#ESTE CODIGO FAZ DOWNLOAD DOS 100 PRIMEIROS TWITTERS ENCONTRADOS PELA API NOS ULTIMOS 10 DIAS

from datetime import date, datetime
import tweepy
from textblob import TextBlob

consumer_key = 'dytcgFdmvIV3Empc3Z8DpGuXK'
consumer_secret = 'srhFXgDS6XdpufxGaHE6DecF7IdXrTEao3US35qsit0PGSYODZ'

access_token = '2847346099-CTEhTJuOnYRmUDLMXMaqjJEAOVe4zrdPbdvS4Iy'
access_token_secret = 'kD43PTwv9jAUFaHvqRWA32Slld7pS0g2CaxIMnna8SEAz'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
hourCtrl = datetime.now().hour #HORA DE INICIO DO PROGRAMA, Usada para controlar a hora do download

intBetDow = 5 #Intervalo entre downloads (unidade hora)
file_path = 'tweeters.txt'
amount_tweets_down = 100 #maximo 100

def downTweet(public_tweets):
    for tweet in public_tweets:
         #print(tweet.created_at)
         #print(tweet.text, tweet.created_at)

         date = tweet.created_at.strftime('%d/%m/%Y')
         horary = tweet.created_at.strftime('%H:%M')
         place = tweet.user.location
         place = '''"''' + place + '''"'''
         content = (str(tweet.text).replace('''"''', "")).replace('\n', "") #TRATO AS ASPAS DUPLAS E O BARRA ENE PARA NAO DA PROBLEMA NO WEKA
         content = content.replace('\0', "")
         content = '''"'''+ content + '''"'''
         user_name = str(tweet.user.name).replace('''"''', "")
         user_name = '''"''' + user_name + '''"'''

         TweetTuple = str(tweet.id) + ","+date + "," + horary+","+user_name+","+content+","+str(tweet.retweet_count)+","+str(tweet.user.followers_count)+","+str(tweet.user.friends_count)+","+place+','+str(tweet.user.statuses_count)+','+str(tweet.user.favourites_count)
         print(TweetTuple )

         # analysis = TextBlob(tweet.text)
         # print(analysis.sentiment)

         if(prevTweDup(TweetTuple)<0):
              file = open(file_path, 'a', encoding='utf-8')
              file.write(TweetTuple)
              file.write("\n")
              file.close()
    #    analysis = TextBlob(tweet.text)
    #    print(analysis.sentiment)

def searchTweet(element, date):
    public_tweets = api.search(element, until=date, lang='pt', count=amount_tweets_down) #COUNT == Quantidade de tweeters requeridos
    downTweet(public_tweets)

def prevTweDup(TweetTuple):#FUNCAO, VERIFICA SE O TWEET JA ESTA SALVO NO ARQUIVO
    file = open(file_path, 'r', encoding='utf-8')
    nozzleString = file.read()
    TweetTuple = TweetTuple[0:17]#Fatio par otimizar a busca

    return nozzleString.find(TweetTuple)

data = date.fromordinal((date.today()).toordinal()+1) #DATA DE AMNHÃ
while(1):
     if(datetime.now().hour == hourCtrl):
          for i in range(0, 10):
               searchTweet('@Timbrasil', data) #TIM
               searchTweet('@ClaroBrasil', data) #Claro
               searchTweet('@digaoi', data) #OI
               searchTweet('@netOficial', data) #NET
               searchTweet('@Vivoemrede', data) #VIVO
               searchTweet('@skybrasil', data) #SKY
               searchTweet('@gvtoficial', data) #GVT
               searchTweet('@nextelbrasil', data) #GVT

               data = date.fromordinal(data.toordinal() -1)  # DECREMENTO

          hourCtrl += int(intBetDow%24)


