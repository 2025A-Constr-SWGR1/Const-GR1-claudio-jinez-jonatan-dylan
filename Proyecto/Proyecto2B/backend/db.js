const sqlite3 = require('sqlite3').verbose();
const db = new sqlite3.Database('./notas.db');

db.serialize(() => {
  db.run(`CREATE TABLE IF NOT EXISTS estudiantes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    nota1 REAL,
    nota2 REAL,
    nota3 REAL
  )`);
});

module.exports = db;
