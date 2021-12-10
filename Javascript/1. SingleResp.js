const fs = require("fs");

class Journal {
  constructor() {
    this.entries = {};
    this.count = 0;
  }

  addEntry(text) {
    let c = ++this.count;
    let entry = `${c}: ${text}`;
    this.entries[c] = entry;
    return c;
  }

  removeEntry(index) {
    delete this.entries[index - 1];
  }

  toString() {
    return Object.values(this.entries).join("\n");
  }

  // the below functionality might be used by other objects as well.
  // As persistence is sth employed by various obhjects we cannot have them all in every class
  /*
  save(filename) {
    fs.writeFileSync(filename, this.toString());
  }

  load(filename) {}
  loadFromWeb(url) {}
  */
}

class PersistenceManager {
  saveToFile(journal, filename) {
    fs.writeFileSync(filename, journal.toString());
  }
}

let j = new Journal();
j.addEntry("I cried today");
j.addEntry("I ate a bug");
console.log(j.toString());

let p = new PersistenceManager();
let filename = "journal.txt";
p.saveToFile(j, filename);
