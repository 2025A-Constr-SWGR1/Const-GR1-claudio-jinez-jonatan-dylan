const API_URL = 'http://localhost:5000/api/estudiantes';

function calcularEstado(promedio) {
  if (promedio >= 7) return "Aprobado";
  else if (promedio >= 5) return "Supletorio";
  else return "Reprobado";
}

async function cargarEstudiantes() {
  const res = await fetch(API_URL);
  const estudiantes = await res.json();
  const tabla = document.getElementById('tabla-estudiantes');
  tabla.innerHTML = '';
  estudiantes.forEach(est => {
    const promedio = ((est.nota1 + est.nota2 + est.nota3) / 3).toFixed(2);
    const estado = calcularEstado(promedio);
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td>${est.nombre}</td>
      <td>${est.nota1}</td>
      <td>${est.nota2}</td>
      <td>${est.nota3}</td>
      <td>${promedio}</td>
      <td>${estado}</td>
      <td><button onclick="eliminarEstudiante(${est.id})">Eliminar</button></td>
    `;
    tabla.appendChild(tr);
  });
}

document.getElementById('formulario').addEventListener('submit', async e => {
  e.preventDefault();
  const nombre = document.getElementById('nombre').value;
  const nota1 = parseFloat(document.getElementById('nota1').value);
  const nota2 = parseFloat(document.getElementById('nota2').value);
  const nota3 = parseFloat(document.getElementById('nota3').value);

  await fetch(API_URL, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ nombre, nota1, nota2, nota3 })
  });

  e.target.reset();
  cargarEstudiantes();
});

async function eliminarEstudiante(id) {
  await fetch(`${API_URL}/${id}`, { method: 'DELETE' });
  cargarEstudiantes();
}

cargarEstudiantes();
