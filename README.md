# 🗂️ Fase4 — Sistema de Gestión Software FJ

> Sistema Integral de Gestión de Clientes, Servicios y Reservas desarrollado en Python con arquitectura 100% orientada a objetos, manejo robusto de excepciones y registro de logs.

**Curso:** Programación 213023 — UNAD  
**Grupo:** 472  
**Tutor:** Wilson Hernán Pérez Correa

---

## 👥 Equipo de trabajo

| Nombre | GitHub | Ramas | Issues |
|---|---|---|---|
| Edisson Ferney Parrado Reyes | [@EdissonParrado](https://github.com/EdissonParrado) | `imports` `logs` `excepciones`   | #1 #2 #3 |
| Alexandra Tautiva Betancur | [@ALXBETANCUR](https://github.com/ALXBETANCUR) | `clase-servicio` `servicio-sala` `entidadbase`| #4 #6 #7 #28 |
| Daniel Eduardo Caro Rodriguez | [@carorodriguezdanieleduardo-dot](https://github.com/carorodriguezdanieleduardo-dot)| `tu-rama` `----`  | #5 #9|
| Hugo Enrique Florez Granados | [@hugoflorez62](https://github.com/hugoflorez62) | `hugoflorez62-patch-1` `asesoria-especializada`| #8 #29 |
| Jhonnatan Steven Gonzales Ramirez | [@Jturing589](https://github.com/Jturing589) | `simulacion_main` | #30 |
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

| Tipo | Cuándo usarlo |
|---|---|
| `feat` | Agregas una clase, método o funcionalidad nueva |
| `fix` | Corriges un error en el código |
| `docs` | Cambias comentarios o documentación |
| `refactor` | Reorganizas código sin cambiar su funcionamiento |
| `test` | Agregas pruebas o la simulación final |


---

## 🔧 Ajustes y Correcciones por parte del colaborador (Edisson Parrado)

| Rama | Descripción | PR | Estado |
|------|-------------|----|---------|
| `feat/completar-reservasala-alquilerequipo` | Completar clases ReservaSala y AlquilerEquipo con uuid, logger y validaciones | [#40](https://github.com/Grupo472/Fase4-SoftwareFJ/pull/40) | ✅ Abierto |
| `feat/completar-clase-reserva` | Completar clase Reserva con inicialización, describir() y validar()| [#38](https://github.com/Grupo472/Fase4-SoftwareFJ/pull/38) | ✅ Fusionado |
| `fix/errores-criticos` | Corregir errores críticos en clases de servicios - excepciones y logger | [#37](https://github.com/Grupo472/Fase4-SoftwareFJ/pull/37) | ✅ Fusionado |
| `fix/EntidadSistema` | Corrección y mejora EntidadSistema (sección ALXBETANCUR)| [#35](https://github.com/Grupo472/Fase4-SoftwareFJ/pull/35) | ✅ Fusionado |


         
- ### ✨ Cambios Principales Realizados
  - - 1. **Corrección de Herencia** - EntidadSistema ahora funciona correctamente como clase base abstracta
      2. **Métodos Abstractos** - Implementación obligatoria de `describir()` y `validar()` en todas las entidades
      3. **Logging Robusto** - Integración consistente del logger en todas las excepciones y eventos críticos
      4. **Validaciones Mejoradas** - Regex para emails, validaciones de rango para precios y descuentos
      5. **UUID Automático** - Generación de identificadores únicos para ReservaSala y AlquilerEquipo
      6. **Manejo de Excepciones** - Excepciones personalizadas con encadenamiento (`from e`)
