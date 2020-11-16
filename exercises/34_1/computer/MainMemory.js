class MainMemory {
  constructor() {
    this.loadedMemory = []
  }

  load(value) {
    return this.loadedMemory.push(value);
  }

  get(index) {
    return parseInt(this.loadedMemory[index], 10);
  }

  clean() {
    this.loadedMemory = []
  }
}

module.exports = MainMemory;
