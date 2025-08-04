const express = require('express');
const db = require('./db');
const cors = require('cors');
const app = express();
const PORT = 5000;

app.use(cors());
app.use(express.json());

// Obtener todos los estudiantes
app.get('/api/estudiantes', (req, res) => {
  db.all("SELECT * FROM estudiantes", [], (err, rows) => {
    if (err) return res.status(500).json({ error: err.message });
    res.json(rows);
  });
});

// Agregar estudiante
app.post('/api/estudiantes', (req, res) => {
  const { nombre, nota1, nota2, nota3 } = req.body;
  db.run(
    "INSERT INTO estudiantes (nombre, nota1, nota2, nota3) VALUES (?, ?, ?, ?)",
    [nombre, nota1, nota2, nota3],
    function (err) {
      if (err) return res.status(500).json({ error: err.message });
      res.json({ id: this.lastID, nombre, nota1, nota2, nota3 });
    }
  );
});

// Eliminar estudiante
app.delete('/api/estudiantes/:id', (req, res) => {
  const { id } = req.params;
  db.run("DELETE FROM estudiantes WHERE id = ?", [id], function (err) {
    if (err) return res.status(500).json({ error: err.message });
    res.json({ eliminado: this.changes > 0 });
  });
});

app.listen(PORT, () => {
  console.log(`Servidor corriendo en http://localhost:${PORT}`);
});
