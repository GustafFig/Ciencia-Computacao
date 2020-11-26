# Raspagem de Dados

## Trybe dia 35.3

Estou usando as seguintes bibliotecas:
    - requests: Para fazer requisições
    - parsel: Para fazer a raspagem através das tags com seletores
    - pymongo: Connecta ao mongoDB

### Exercícios

#### 1) Faça uma requisição ao site [https://httpbin.org/encoding/utf8](https://httpbin.org/encoding/utf8) e exiba seu conteúdo de forma legível

#### 2) Faça uma requisição ao recurso usuários da API do Github (https://api.github.com/users)[https://api.github.com/users], exibindo o username e url de todos os usuários retornados

#### 3) Às vezes, você precisa fazer com que o seu raspador da Web pareça estar fazendo solicitações HTTP como o navegador, para que o servidor retorne os mesmos dados que você vê no seu navegador. Faça uma requisição a [https://scrapethissite.com/pages/advanced/?gotcha=headers](https://scrapethissite.com/pages/advanced/?gotcha=headers) e verifique se foi bem sucedido.

#### 4) Baseados em uma página contendo detalhes sobre um livro [http://books.toscrape.com/catalogue/the-grand-design_405/index.html](http://books.toscrape.com/catalogue/the-grand-design_405/index.html), faça a extração dos campos título, preço, descrição e url contendo a imagem de capa do livro

> O preço deve vir somente valores numéricos e ponto. Ex: Â£13.76 -> 13.76.
> A descrição de ter o sufixo "more..." removido quando existir.
> Os campos extraídos devem ser apresentados separados por vírgula

#### 5) Modifique o exercício anterior para retornar também quantos livros estão disponíveis apresentando como último campo no retorno

#### 6) Escreva um programa que se conecte ao banco de dados library e liste os livros da coleção books para uma determinada categoria recebida por uma pessoa usuária. Somente o título dos livros deve ser exibido

#### 7) Faça o calculo de quantos livros publicados (STATUS = PUBLISH) temos em nosso banco de dados por categoria. Ordenando-os de forma decrescente de acordo com a quantidade

### Bônus

#### 8) Agora um desafio, vá ao site https://en.wikipedia.org/wiki/Gallery_of_sovereign_state_flags e recupere as imagens de todas as bandeiras

Faça requisições para as URLs das imagens e escreva seus conteúdos em arquivos binários. São 206 ao total

> Ps: note que fiz um index.js rode-o com `npm install && node index.js` e abra o navegador com http://localhost:3000/0.png, tente trocar 0 por outros numeros

#### 9) Alguns sites possuem paginação feita através de rolagem infinita. Descubra como funciona a rolagem infinita e extraia todas as citações do seguinte site: http://quotes.toscrape.com/scroll
