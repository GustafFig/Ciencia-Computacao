# Arquitetura de Redes

## Trybe dia 34.2

### Exercícios

Vamos juntar tudo o que aprendemos até aqui e exercitar mais ainda nosso aprendizado! Para isso iremos criar servers Node.js utilizando alguns dos protocolos vistos e, então, vamos explorá-los. Se tiver dúvidas ao utilizar alguma das ferramentas que mencionamos nos exercícios, exercite suas habilidades de busca no Google ou experimente o comando man

#### 1) O primeiro server que iremos utilizar é o nosso velho amigo HTTP, na camada de aplicação. Você pode tanto criar um quanto utilizar um dos projetos ou exercícios dos módulos anteriores. A ideia é utilizarmos os conhecimentos do conteúdo e a ferramenta cURL para realizarmos uma chamada HTTP para ele. A ideia aqui é que o projeto tenha rotas GET e POST, para que seja possível enviar requisições para os endpoints e receber respostas, assim como já nos acostumamos a receber via browser ou utilizando programas como o Postman. Caso tenha dificuldades maiores, você pode utilizar o Postman para converter uma requisição em cURL, é só fazer a requisição nele como você já sabe e depois clicar no botão code (que fica embaixo do save) e escolher cURL

- Faça uma chamada GET, utilizando o cURL
- Faça uma chamada POST, utilizando o cURL, passando um JSON no body da requisição
- Faça uma chamada qualquer, utilizando o cURL, passando um header na requisição

#### 2) Ainda utilizando o cURL, vamos explorar mais alguns conceitos do HTTP. Relembre que falamos que o HTTP organiza e dá significado aos dados encapsulados nessa camada. Por exemplo: ao vermos um 200 tanto nós quanto um client HTTP sabemos que aquela request foi realizada com sucesso. Vamos explorar isso com o cURL

- Faça uma chamada GET, utilizando o cURL, para "google.com"
- Perceba que foi retornado um 301. Isso quer dizer que existem diversos redirecionamentos que nos encaminham para o lugar certo. No caso, o caminho certo para a página do google é www.google.com. Ao acessarmos pelo navegador, não percebemos isso porquê ele faz o redirecionamento para a página certa para nós ao encontrar o 301, porém, se você inspecionar a network você irá identificar esse redirecionamento. Faça uma nova chamada a "google.com", porém agora utilizando o parâmetro -L ou --location, que serve para "seguir redirecionamentos"

#### 3) Agora utilizando o wget, pegue o conteúdo da página do site da Trybe, depois abra o arquivo HTML baixado em seu navegador. Faça o mesmo processo com outras páginas web

#### 4) Agora iremos para a camada de transporte. Vamos criar um server TCP, utilizando o módulo NET do Node.js. Como dissemos antes, o importante aqui é entender o conceito, aqui vão algumas ajudas

- A sintaxe do módulo NET é muito parecida com a do socket.io que conhecemos anteriormente
- Na documentação, temos um exemplo que se olhado com calma, podemos perceber que ele lembra bastante a sintaxe do socket.io, procure por createServer [https://nodejs.org/api/net.html](neste link) que contêm a documentação do NET
- Perceba que o servidor sozinho, não faz nada, ele precisa que alguém se conecte a ele, então para testá-lo, você pode utilizar o comando telnet localhost 8085, onde telnet é a aplicação que iremos utilizar, localhost é o local onde o servidor está (no caso, o seu próprio PC) e 8085 é a porta em que o servidor está escutando conexões
- Assim como no socket.io, onde cada evento recebe um nome, aqui também é assim, então pesquise por Event: 'data' para saber como tratar corretamente o evento de receber informações e deixá-las de forma legível para humanos

#### 5) Utilizando o comando telnet ou o Netcat

- Conecte no server do exercício anterior e envie informações. O server deverá imprimir as mensagens enviadas no console
- Pare o servidor e verifique o que aconteceu com a conexão que estava aberta com o comando telnet ou nc

#### 6) Reinicie o servidor TCP e agora faça uma requisição utilizando o cURL (HTTP). Perceba o que é exibido no console do server, já que não estamos utilizando o HTTP nele. Perceba também que o comando cURL não recebe uma resposta HTTP com sentido (um status code 200, por exemplo), de modo que ele não sabe que aquela requisição chegou ao fim

#### 7) Agora iremos explorar o outro protocolo de transporte que aprendemos, o UDP. Crie um servidor utilizando o módulo dgram do Node.js. Para isso, as dicas que vimos no exercício 4 se aplicam aqui, procure na [https://nodejs.org/api/dgram.html](documentação) o módulo que cria o servidor e como o evento deve ser nomeado. Uma coisa importante a se lembrar, é que enquanto o TCP faz controle de fluxo, o UDP não, então algumas diferenças serão percebidas no código também, nosso server deverá

- Imprimir no console toda mensagem recebida (não esqueça de converter também para string)
- Utilize a versão 4 do protocolo (udp4)
- Utilize a porta 8084

#### 8) Envie pacotes para o servidor UDP utilizando o Netcat (nc). Em seguida pare o servidor e perceba que como não há conexão nada é sentido pelo client

#### 9) Faça uma chamada ao server utilizando o cURL. Lembre que, além do HTTP, o comando utiliza o protocolo TCP e não o UDP. Repare o que acontece

### Bonus

#### 10) Identifique o IP interno e externo da sua máquina

#### 11) Identifique as interfaces de redes utilizadas por sua máquina e identifique qual está em uso agora
