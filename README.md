# 🗂️ Fase4 — Sistema de Gestión Software FJ

> Sistema Integral de Gestión de Clientes, Servicios y Reservas desarrollado en Python con arquitectura 100% orientada a objetos, manejo robusto de excepciones y registro de logs.

**Curso:** Programación 213023 — UNAD  
**Grupo:** 472  
**Tutor:** Wilson Hernán Pérez Correa

---

## 👥 Equipo de trabajo

| Nombre | GitHub | Ramas | Issues |
|---|---|---|---|
| Edisson Ferney Parrado Reyes | [@EdissonParrado](https://github.com/EdissonParrado) | `imports` `logs` `excepciones` `sistema` | #1 #2 #3 #9 |
| Alexandra Tautiva Betancur | [@ALXBETANCUR](https://github.com/ALXBETANCUR) | `entidadbase` `cliente` | #4 #5 |
| Daniel Eduardo Caro Rodriguez | [@carorodriguezdanieleduardo-dot](https://github.com/carorodriguezdanieleduardo-dot)| `servicio-sala` `equipo-asesoria` | #6 #7 |
| por definir | @usuario | `reserva` | #8 |

---

## 📁 Estructura del proyecto
Fase4-SoftwareFJ/
├── Sistema_Gestion.py   ← archivo principal del sistema
├── logs/                ← se crea automáticamente al ejecutar
└── README.md
---

## ⚙️ Cómo ejecutar el sistema

```bash
git clone https://github.com/Grupo472/Fase4-SoftwareFJ.git
cd Fase4-SoftwareFJ
python Sistema_Gestion.py
```

> Al ejecutarlo se crea automáticamente la carpeta `logs/` con el archivo `sistema.log`.

---

## 🔀 Flujo de trabajo

### 1. Clonar el repositorio (solo la primera vez)
```bash
git clone https://github.com/Grupo472/Fase4-SoftwareFJ.git
cd Fase4-SoftwareFJ
```

### 2. Crear tu rama y cambiarte a ella
```bash
git checkout -b nombre-de-tu-rama
```

### 3. Hacer commits mientras trabajas
```bash
git add Sistema_Gestion.py
git commit -m "feat(alcance): descripción de lo que hiciste"
git push origin nombre-de-tu-rama
```

### 4. Cuando termines tu Issue — abrir Pull Request
- Ve a **GitHub → Pull requests → New pull request**
- Selecciona: `base: main` ← `compare: tu-rama`
- Espera revisión y aprobación del líder antes de fusionar

---

## 📋 Convención de commits

Formato: `tipo(alcance): descripción en español`

| Tipo | Cuándo usarlo |
|---|---|
| `feat` | Agregas una clase, método o funcionalidad nueva |
| `fix` | Corriges un error en el código |
| `docs` | Cambias comentarios o documentación |
| `refactor` | Reorganizas código sin cambiar su funcionamiento |
| `test` | Agregas pruebas o la simulación final |
