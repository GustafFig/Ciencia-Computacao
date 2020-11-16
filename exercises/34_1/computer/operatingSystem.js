const SecondaryMemory = require('./SecondaryMemory')
const MainMemory = require('./MainMemory')

const secondaryMemory = new SecondaryMemory();
const mainMemory = new MainMemory();

// Conjunto de números aleatórios a serem somados

const createRandomList = (length) => {
  let nummbers = [];
  for (let i = 1; i <= length; i += 1) {
    const number = Math.floor(Math.random() * 100000)
    nummbers.push(number.toString());
  }
  return nummbers;
};

const randomNumbers = createRandomList(200);
console.log(randomNumbers);

// Carregando todos os números em memória (principal e secundária)
randomNumbers.forEach((number) => {
  secondaryMemory.load(number);
  mainMemory.load(number);
});

// Interando sobre os números carregados na MEMORIA PRINCIPAL e realizando a soma
let initialMainMemoryTime = Date.now();
let mainMemorySum = 0;
for (let i = 0; i < randomNumbers.length; i++) {
  mainMemorySum += mainMemory.get(i);
}
console.log(`Memória Principal\nSoma: ${mainMemorySum} Tempo gasto: ${Date.now() - initialMainMemoryTime}ms\n`);

// Interando sobre os números carregados na MEMORIA SECUNDARIA e realizando a soma
let initialSecondaryMemoryTime = Date.now()
let secondaryMemorySum = 0
for (let i = 0; i < randomNumbers.length; i++) {
  secondaryMemorySum += secondaryMemory.get(i)
}

console.log(`Memória Secundária\nSoma: ${secondaryMemorySum} Tempo gasto: ${Date.now() - initialSecondaryMemoryTime}ms`)

/*
  Ao rodar uma segunda vez sem limpar o diretórios files nossos resultados variam por serem usados os mesmos valores em
  secondaryMemory, mas os valores novos em main memory
*/
