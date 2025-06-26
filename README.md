oyecto Poker Analyst
Análisis inteligente de manos de póker Texas Hold’em para decisiones pre-flop y post-flop, basado en simulaciones y lógica experta. Implementado en Python y con interfaz en Streamlit.

Descripción
Este proyecto permite analizar manos de póker en distintas etapas:

Pre-flop: Evalúa la fuerza de las cartas iniciales y la posición en la mesa para recomendar acciones como fold, call o raise.

Post-flop: Calcula probabilidades y evalúa la mano después de que se han revelado cartas comunitarias (flop), con simulaciones para recomendaciones estratégicas.

El backend está implementado en Python con funciones especializadas y el frontend usa Streamlit para interfaz gráfica.

Características
Análisis pre-flop con lógica basada en posición, número de jugadores y acciones previas.

Análisis post-flop con simulaciones Monte Carlo para estimar probabilidades de ganar.

Recomendaciones estratégicas claras para cada etapa.

Integración con Streamlit para interfaz web interactiva.

Testing automatizado con pytest.

Dockerización para despliegue sencillo y portable.

Instalación
Clonar repositorio:

git clone https://github.com/tu-usuario/proyecto-poker-analyst.git
cd proyecto-poker-analyst

Crear entorno virtual (opcional pero recomendado):
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

Instalar dependencias:
pip install -r requirements.txt


Uso
Para iniciar la aplicación web con Streamlit:

streamlit run app.py
Ingresa tus cartas, posición, flop y demás parámetros para obtener análisis y recomendaciones.

Testing
Para correr los tests automatizados con pytest:
pytest
Los tests verifican que las funciones de análisis pre-flop y post-flop se comporten correctamente ante distintos escenarios.

Docker
Para construir la imagen Docker:
docker build -t poker-analyst .
Para correr los tests dentro del contenedor:
docker run --rm poker-analyst python -m pytest
Para iniciar la aplicación en Docker (si configuraste el ENTRYPOINT o CMD):
docker run -p 8501:8501 poker-analyst
Luego abrir en el navegador:
http://localhost:8501
