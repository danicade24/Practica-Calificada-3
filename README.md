# Practica Calificada 3
## Guía para Usar el Dev Container

### 1. **Subir el código al repositorio de GitHub**

Deben de estar todos los archivos necesarios, incluyendo los del Dev Container (`.devcontainer/Dockerfile` y `.devcontainer/devcontainer.json`), subidos al repositorio de GitHub. La estructura del proyecto es la siguiente

```
/PC3/
│
├── .devcontainer/
│   ├── Dockerfile
│   └── devcontainer.json
│
|-- src
|   |-- ejercicio1-parte1/
|   `-- ejercicio1-parte2/
`-- tests
    |-- ejercicio1-parte1/
    `-- ejercicio1-parte2/
├── requirements.txt    # Dependencias de Python o de otro entorno
|-- README.md
|-- requirements.txt
```

- **Dockerfile**: Define cómo se construye la imagen del contenedor.
- **devcontainer.json**: Configura el contenedor, incluyendo extensiones de VSCode, puertos, comandos a ejecutar, entre otros.

Esto permite que cualquier persona que clone el repositorio tenga acceso al mismo entorno de desarrollo, sin necesidad de configurar manualmente el entorno.

---

### 2. **Instrucciones para clonar y ejecutar el contenedor**

#### Paso 1: **Clonar el repositorio desde GitHub**
Se debe clonar el repositorio:

```bash
git clone https://github.com/danicade24/Practica-Calificada-3.git
```

#### Paso 2: **Asegurarse de tener Docker y VS Code instalados**
Es necesario tener instalados:

- **Docker**: [Descargar Docker](https://www.docker.com/get-started)
- **Visual Studio Code**: [Descargar VS Code](https://code.visualstudio.com/)
- **Extensión Remote - Containers** de VS Code: Se puede instalar desde la tienda de extensiones de VS Code.

#### Paso 3: **Abrir el proyecto en VS Code y ejecutar el contenedor**
Una vez clonado el repositorio y con las herramientas listas, se deben seguir estos pasos:

1. **Abrir VS Code** y navegar a la carpeta del proyecto clonado.
2. **Abrir el contenedor** en VS Code:
   - Abre la Paleta de Comandos (`Ctrl+Shift+P`).
   - Selecciona `Remote-Containers: Reopen in Container`. 
   - VS Code detectará automáticamente los archivos `.devcontainer` y configurará el entorno.

**Nota**: Si es que no quieres usar VS Code, también puedes ejecutar el contenedor desde tu terminal, pero VS Code simplifica mucho el proceso.

#### Paso 4: **Ejecutar la aplicación dentro del contenedor**
Dentro del contenedor, la otra persona puede ejecutar los comandos necesarios para ejecutar la aplicación. Ejemplo para una app en Python:

- Ejecutar la aplicación:

  ```bash
  python3 app.py
  ```


---

### 3. **Uso del contenedor sin VS Code (Solo Docker)**

Si alguien no quiere usar VS Code, también puede trabajar solo con Docker. Los pasos son los siguientes:

#### Paso 1: **Clonar el repositorio**

```bash
git clone https://github.com/danicade24/Practica-Calificada-3.git
```

#### Paso 2: **Construir la imagen Docker**

Construir la imagen del contenedor usando el Dockerfile:

```bash
docker build -t project .
```

#### Paso 3: **Ejecutar el contenedor**

Ejecutar el contenedor:

```bash
docker run -it --name pc3 -v $(pwd):/workspace project
```

Esto abre una terminal interactiva dentro del contenedor. Desde allí, puedes ejecutar la aplicación y cualquier comando necesario.

#### Paso 4: **Ejecutar la aplicación**

Dentro del contenedor, puedes instalar dependencias y ejecutar la aplicación, tal como lo harías en tu entorno local.

---
