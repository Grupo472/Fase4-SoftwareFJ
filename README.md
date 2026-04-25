# Fase4-SoftwareFJ
Sistema Integral de Gestión de Clientes, Servicios y Reservas para Software FJ. Desarrollado en Python con POO, clases abstractas, manejo de excepciones y registro de logs. Curso Programación 213023 - UNAD - Grupo 472.

## Integrantes del equipo

| Nombre | Usuario GitHub | Rama | Issues |
|---|---|---|---|
| Edisson Ferney Parrado Reyes | EdissonParrado | `base` / `sistema` | #1 #2 #3 #9 |
| Alexandra Tautiva Betancur | (usuario GitHub) | `entidades` | #4 #5 |
| Daniel Eduardo Caro Rodriguez | (usuario GitHub) | `servicios` | #6 #7 |
| Hugo Enrique Florez Granados | (usuario GitHub) | `reserva` | #8 |

## Estructura del proyecto
Fase4-SoftwareFJ/
├── Sistema_Gestion.py   ← archivo principal del sistema
├── logs/                ← se crea automáticamente al ejecutar
└── README.md

## Cómo trabajar en el proyecto

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
git commit -m "Descripción clara de lo que hiciste"
git push origin nombre-de-tu-rama
```

### 4. Cuando termines tu Issue — abrir Pull Request
- Ve a GitHub → Pull requests → New pull request
- Base: `main` ← Compare: `tu-rama`
- Espera revisión del líder antes de fusionar

## Reglas del equipo
- ❌ Nunca hacer commits directamente al `main`
- ✅ Un commit por cada parte lógica completada
- ✅ Mensajes de commit descriptivos en español
- ✅ Esperar aprobación del líder para fusionar al main
- ✅ Los Issues se cierran cuando el PR es aprobado