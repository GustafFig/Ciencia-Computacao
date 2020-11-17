# 1

## 1 - digite no terminal

> `curl -X GET http://httpbin.org`

## 2 - digite no terminal

> `curl -X POST -H "Content-type: application/json" -d '{"nome":"coloque seu nome"}' http://httpbin.org/post`
> Note que as opções devem vir antes da URL e que o temos que setar o header content-type para application/json para não enviarmos um form em urlencoded

## 3 - foi feito em dois com o -H

# 2

## 1 - digite no terminal

> `curl google.com`

## 2 - digite no terminal

> `curl -L google.com`

# 3

## digite no terminal

> `wget http://www.google.com`;

# 4 e 5

## rode na pasta raiz

> `node 4.js`
> e em outro terminal coloque
> `telnet 127.0.0.1 8085`

# 6

## ainda com o servidor rodando, digite no cliente

> `curl -I http://localhost:8085`

# 7 e 8

## rode com

> `node 7.js`
> entao use
> `echo "message" | nc -w1 -u 127.0.0.1:8086`

# 9

> `curl http://localhost:8086`

note que a conexão foi recusada
