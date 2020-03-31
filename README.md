# Twitter Bot

**Bot do twitter para responder tweets que contem certas palavras previamente definidas**

Bots criados para interagir no twitter, sendo eles:

- Bot de replies: bot feito para responder tweets e replys de tweets que contem uma palavra previamente definida pelo programador e responde com diferentes linhas existentes no arquivo `replies.txt`
- Bot de fav e rt: bot feito para favoritar e retweetar quando certas palavras aparecerem no tweeter

## Como usar?
- Baixe a virtualenv `pip install virtualenv` ou `sudo pip install virtualenv`
- Crie uma virtualenv `virtualenv <nome_da_virtualenv>`
- Baixe o tweepy `pip install tweepy`
- Exporte suas keys e seus tokens `export CONSUMER_KEY="abcde..."` 

**BOT REPLIES**
- Escreva as possiveis respostas no arquivo `replies.txt`
- Rode o codigo em python bots/reply_phrase_bot.py

**BOT FAV E RT**
- Rode o codigo em python bots/fav_and_rt_bot.py
