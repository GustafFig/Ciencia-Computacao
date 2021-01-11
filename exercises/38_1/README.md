# HashMap

## Trybe dia 38.1

### Exercises

#### 1) Facebook

Você receberá uma lista de palavras e uma string . Escreva uma função que decida quais palavras
podem ser formadas com os caracteres da string (cada caractere só pode ser utilizado uma vez).
Retorne a soma do comprimento das palavras escolhidas

#### 2) Google

Uma certa empresa tem uma estrutura hierarquizada onde cada pessoa reporta a uma única outra pessoa. Cada pessoa tem um score que é o total de pessoas que estão abaixo dela, incluindo subordinados de seus subordinados, além dela própria. Isso significa que uma pessoa que não tem nenhuma equipe tem score 1. Uma pessoa com apenas um subordinado e esse subordinado não tem equipe, tem score 2. Escreva um método que calcule o score de uma determinada pessoa
Dica: para saber o score de uma pessoa, você precisa saber o score das pessoas da equipe dela, correto? Qual estratégia utiliza a mesma função dentro dela própria

### Bônus

É muito comum em entrevistas que, quando a pessoa resolve o problema dentro do tempo, façam-se perguntas "follow-up" , que dificultam a questão. Os follow-ups abaixo são opcionais

1. Caso a empresa precise fazer essa consulta frequentemente, como você pode tornar essas consultas mais eficientes? Como você pode guardar o resultado de consultas anteriores?
2. Escreva um método para incluir uma nova pessoa na equipe de uma outra pessoa. Seu método deve considerar que cada pessoa pode ter no máximo k pessoas em seu time. Se o time estiver cheio, a nova contratada pode ser alocada na equipe de qualquer pessoa abaixo dela, não precisando ser na equipe imediatamente abaixo.
3. Se você adicionar uma nova contratação à lista de subordinadas, a estrutura que você fez no follow-up 1 está desatualizada. Modifique suas funções para que essa estrutura seja atualizada junto com a adição de uma nova contratação. Faça isso sem rodar de novo a função score() e lembre-se de atualizar todos os scores desde a pessoa da presidência até a equipe que a nova contratação entrou.