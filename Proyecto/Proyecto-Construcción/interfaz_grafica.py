# Requiere: pip install customtkinter
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import os

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

USUARIOS_TXT = "registro.txt"
ESTUDIANTES_TXT = "estudiantes.txt"

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Centrado de ventana
        self.ancho = 600
        self.alto = 500
        self.geometry(f"{self.ancho}x{self.alto}+{self.winfo_screenwidth() // 2 - self.ancho // 2}+{self.winfo_screenheight() // 2 - self.alto // 2}")
        self.title("Sistema de Notas")
        self.usuario = None
        self.mostrar_login()

    def mostrar_login(self):
        self.clear()
        ctk.CTkLabel(self, text="Inicio de Sesión", font=("Arial", 20)).pack(pady=10)
        self.correo_entry = ctk.CTkEntry(self, placeholder_text="Correo")
        self.correo_entry.pack(pady=5)
        self.contrasena_entry = ctk.CTkEntry(self, placeholder_text="Contraseña", show="*")
        self.contrasena_entry.pack(pady=5)

        ctk.CTkButton(self, text="Iniciar Sesión", command=self.login).pack(pady=5)
        ctk.CTkButton(self, text="Registrarse", command=self.mostrar_registro).pack(pady=5)

    def mostrar_registro(self):
        self.clear()

        ctk.CTkLabel(self, text="Registro de Profesor", font=("Arial", 20)).pack(pady=10)
        self.nombre = ctk.CTkEntry(self, placeholder_text="Nombre")
        self.apellido = ctk.CTkEntry(self, placeholder_text="Apellido")
        self.cedula = ctk.CTkEntry(self, placeholder_text="Cédula")
        self.email = ctk.CTkEntry(self, placeholder_text="Correo")
        self.passw = ctk.CTkEntry(self, placeholder_text="Contraseña", show="*")

        for e in [self.nombre, self.apellido, self.cedula, self.email, self.passw]:
            e.pack(pady=5)

        ctk.CTkButton(self, text="Guardar", command=self.registrar_profesor).pack(pady=10)
        ctk.CTkButton(self, text="Volver", command=self.mostrar_login).pack()

    def registrar_profesor(self):
        datos = [e.get() for e in [self.nombre, self.apellido, self.cedula, self.email, self.passw]]
        if "" in datos:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return
        with open(USUARIOS_TXT, "a") as f:
            f.write("|".join(datos) + "\n")
        messagebox.showinfo("Éxito", "Profesor registrado")
        self.mostrar_login()

    def login(self):
        correo = self.correo_entry.get()
        clave = self.contrasena_entry.get()
        with open(USUARIOS_TXT, "r") as f:
            for linea in f:
                campos = linea.strip().split("|")
                if len(campos) >= 5:
                    nombre, apellido, cedula, mail, password = campos[:5]
                    if mail == correo and password == clave:
                        self.usuario = {
                            "nombre": nombre,
                            "apellido": apellido,
                            "correo": mail
                        }
                        self.mostrar_menu()
                        return
        messagebox.showerror("Error", "Correo o contraseña incorrectos")

    def mostrar_menu(self):
        self.clear()
        ctk.CTkLabel(self, text=f"Bienvenido, {self.usuario['nombre']} {self.usuario['apellido']}", font=("Arial", 16)).pack(pady=10)
        ctk.CTkButton(self, text="1. Registro de Notas", command=self.pantalla_registro_notas).pack(pady=5)
        ctk.CTkButton(self, text="2. Consultar por Curso", command=self.pantalla_consultar_curso).pack(pady=5)
        ctk.CTkButton(self, text="Cerrar Sesión", command=self.mostrar_login).pack(pady=10)

    def pantalla_registro_notas(self):
        self.clear()
        self.lista_frame = ctk.CTkScrollableFrame(self)
        self.lista_frame.pack(fill="both", expand=True, pady=10)

        ctk.CTkLabel(self, text="Registro de Notas", font=("Arial", 18)).pack(pady=5)
        self.nombre_e = ctk.CTkEntry(self, placeholder_text="Nombre del Estudiante")
        self.apellido_e = ctk.CTkEntry(self, placeholder_text="Apellido")
        self.materia = ctk.CTkEntry(self, placeholder_text="Materia")
        self.curso = ctk.CTkEntry(self, placeholder_text="Curso (ej: gr1)")
        self.n1 = ctk.CTkEntry(self, placeholder_text="Nota 1")
        self.n2 = ctk.CTkEntry(self, placeholder_text="Nota 2")

        for e in [self.nombre_e, self.apellido_e, self.materia, self.curso, self.n1, self.n2]:
            e.pack(pady=2)

        ctk.CTkButton(self, text="Guardar", command=self.guardar_nota).pack(pady=5)
        ctk.CTkButton(self, text="Volver", command=self.mostrar_menu).pack(pady=5)

    def guardar_nota(self):
        datos = [e.get() for e in [self.nombre_e, self.apellido_e, self.materia, self.curso, self.n1, self.n2]]
        if "" in datos:
            messagebox.showerror("Error", "Completa todos los campos")
            return
        try:
            n1 = float(datos[4])
            n2 = float(datos[5])
        except:
            messagebox.showerror("Error", "Notas deben ser numéricas")
            return

        promedio = round((n1 + n2) / 2, 2)
        if promedio >= 14:
            estado = "APROBADO"
            color = "green"
        elif promedio >= 9:
            estado = "SUPLETORIO"
            color = "orange"
        else:
            estado = "REPROBADO"
            color = "red"

        registro = "|".join(datos + [str(promedio), estado])
        with open(ESTUDIANTES_TXT, "a") as f:
            f.write(registro + "\n")

        label = ctk.CTkLabel(self.lista_frame, text=f"{' '.join(datos[:2])} - {datos[2]} ({datos[3]}): {promedio} - {estado}", text_color=color)
        label.pack(anchor="w")

    def pantalla_consultar_curso(self):
        self.clear()
        ctk.CTkLabel(self, text="Consulta por Curso", font=("Arial", 18)).pack(pady=5)
        self.busqueda_curso = ctk.CTkEntry(self, placeholder_text="Curso")
        self.busqueda_curso.pack(pady=5)
        ctk.CTkButton(self, text="Buscar", command=self.buscar_por_curso).pack(pady=5)
        self.resultado_frame = ctk.CTkScrollableFrame(self)
        self.resultado_frame.pack(fill="both", expand=True)
        ctk.CTkButton(self, text="Volver", command=self.mostrar_menu).pack(pady=5)

    def buscar_por_curso(self):
        curso = self.busqueda_curso.get()
        for widget in self.resultado_frame.winfo_children():
            widget.destroy()
        if not os.path.exists(ESTUDIANTES_TXT): return
        with open(ESTUDIANTES_TXT, "r") as f:
            for linea in f:
                if curso in linea:
                    ctk.CTkLabel(self.resultado_frame, text=linea.strip()).pack(anchor="w")

    def clear(self):
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()
