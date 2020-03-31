# Twitter Bot

*Bot do twitter para responder tweets que contem certas palavras previamente definidas*

Um bot criado para responder tweets e replys de tweets que contem uma palavra previamente definida pelo programador e responde com diferentes linhas existentes no arquivo `replies.txt`

## Como usar?
- Baixe a virtualenv `pip install virtualenv` ou `sudo pip install virtualenv`
- Crie uma virtualenv `virtualenv <nome_da_virtualenv>`
- Baixe o tweepy `pip install tweepy`
- Exporte suas keys e seus tokens `export CONSUMER_KEY="abcde..."` 
- Escreva as possiveis respostas no arquivo `replies.txt`
- Rode o codigo em python bots/reply_phrase_bot.py
