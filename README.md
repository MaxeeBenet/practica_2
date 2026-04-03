### 🚀 Practica 2 - Seminario de Lenguajes - Python

#### 🏆 Simulación de competencia de cocina y ranking

Simulación de una competencia de cocina donde 5 participantes son evaluados por 3 jueces en cada ronda.  
Cada juez otorga un puntaje del 1 al 10.  
El puntaje de la ronda es la suma de los tres jueces.  
La competencia se divide en 5 rondas, se actualiza la tabla de posiciones en cada ronda y luego se brinda la tabla final.

---

### 📁 Estructura

```
proyecto2026/
├── notebooks/        # Notebooks
├── src/              # Código fuente
├── requirements.txt
└── README.md
```

---

### ⚙️ Requisitos

- Python 3.13.x
- pip

---

### 📦 Instalación

1. Clonar el repositorio:

```
git clone https://github.com/MaxeeBenet/practica_2.git
```

2. Entrar en la carpeta:

```
cd proyecto2026
```

3. Crear entorno virtual:

```
Windows: python -m venv .venv
Linux/Mac: python3 -m venv .venv
```

4. Activar entorno virtual:

```
Windows (CMD): .venv\Scripts\activate
Git Bash: source .venv/Scripts/activate
Linux/Mac: source .venv/bin/activate
```

5. Instalar dependencias:

```
pip install -r requirements.txt
```

---

### ▶️ Ejecución

```
python src/concurso.py
```