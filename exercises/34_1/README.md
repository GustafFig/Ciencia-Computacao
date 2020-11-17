# Arquitetura de Computador

## Trybe 34 - 1

### Exercíios

#### 1) Crie um projeto que irá simular a arquitetura que vimos em aula de uma maneira bem simples, ela terá um arquivo principal para a execução do programa que representará nosso Sistema Operacional e duas classes que representarão a Memória Principal e a Secundária

Cada tipo de memória irá armazenar os dados de fato na memória que ela representa, sendo a Principal armazenando tudo em memória RAM e a secundária no disco através do fs (File System) e através do NodeJS estaremos fazendo chamadas ao Sistema Operacional para realizar essas tarefas para gente, pois ele melhor do que ninguém saberá utilizar as memórias. O objetivo do nosso script será realizar a soma de um array de números aleatórios utilizando as duas implementações de memória. Os dados serão sempre armazenados como strings!

1. Crie um novo diretório na sua máquina para os exercícios (pode chamar ele de computador ou pc 😎), os próximos arquivos deverão ser criados dentro dela
2. Vamos começar a nossa memória principal, ou memória RAM, para isso crie um arquivo MainMemory.js **(confira em templates)** e adicione o conteúdo abaixo nela. Implemente os métodos get e load

* No get você irá retornar a posição dada (index) do array de loadedMemory. Não esqueça de converter o valor para numérico (float ou int)
* No load você irá adicionar (push) o elemento passado (value) ao array loadedMemory
  
3. Agora, crie um arquivo SecondaryMemory.js para ser a nossa memória secundária e adicione o conteúdo abaixo **(confira em templates)**. Mais uma vez você será responsável pela implementação dos métodos get e load porém, agora, utilizaremos o fs, para persistir esses dados em disco

   * No load, utilizando o método writeFileSync do fs, escreva o código que crie um novo arquivo utilizando nextFileName como path e salve o value no conteúdo deste novo arquivo
   * No get, retorne o conteúdo do arquivo fileName, utilize o método readFileSync do fs. Não esqueça de converter o valor para numérico (float ou int)
   * Crie, no diretório de onde estiver executando os programas, um diretório disk para guardar os dados que você salvará em disco.
  
4. Vamos criar nosso arquivo principal para gerenciar as "memórias" que criamos, crie um novo arquivo operatingSystem.js e coloque o seguinte conteúdo
5. Vamos testar nosso script, execute o arquivo operatingSystem.js e veja a saída no console. Deu certo?! Como foram os tempos de saída?!
6. Para deixar nosso script ainda mais legal, vamos aumentar a quantidade de números para serem somados, adicione uma grande quantidade de números no array de números aleatórios (bastante mesmo, tipo uns 200). E rode o script novamente. Como foi o tempo de resposta agora? deu diferença? qual foi mais rápido?!
7. Agora, vamos reforçar mais um conteúdo apreendido, comente o trecho do código que carrega os números da memória e execute novamente. Compare os resultados das somas. O que aconteceu

#### 2) Agora vamos explorar o papel do sistema operacional e o gerenciamento de recursos, para isso utilizaremos os módulos nativos do NodeJS, para solicitar chamadas do SO que nos mostre informações dos recursos de nossa máquina. Crie um script chamado resources.js e utilize-o para exibir no console as seguintes informações

1. A plataforma que estamos utilizando, por exemplo: linux, win32, darwin, etc., a arquitetura, por exemplo, x32 ou x64, e a versão (release). Para isso utilize o módulo
2. Adicione o código para exibir a quantidade de cores da sua CPU e o modelo e a velocidade em gigahertz - GHz de cada um (utilize o valor vindo em speed e faça a conversão 😎)
3. Exiba também a quantidade total de memória RAM disponível em sua máquina em gigabytes - GB (faça a conversão também 😉)

#### 3) Faça um script que, a cada intervalo de segundo, mostre no console a memória utilizada do sistema operacional vs a memória total (ambos em megabytes)

#### 4) Faça um script que exibe o seu respectivo process id utilizando o módulo process do NodeJS e então fique em execução por um determinado tempo. Agora utilizando os comandos de monitoramento visto no conteúdo, exiba os processos em execução e então identifique o seu processo
