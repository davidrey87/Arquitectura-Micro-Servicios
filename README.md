# Arquitectura-Micro-Servicios
Repositorio de la tarea 2

## Sistema de Análisis de Sentimientos

Antes de ejecutar el código asegurate de instalar los prerrequisitos del sistema ejecutando:
> sudo pip install -r requirements.txt  

Los paquetes que se instalarán son los siguientes:

Paquete | Versión | Descripción
--------|---------|------------
Flask   | 0.10.1  | Micro framework de desarrollo
requests| 2.12.4  | API interna utilizada en Flask para trabajar con las peticiones hacia el servidor

*__Nota__: También puedes instalar éstos prerrequisitos manualmente ejecutando los siguientes comandos*   
> pip install 'Flask==0.10.1'  
> pip install 'requests==2.12.4'

Una vez instalados los prerrequisitos es momento de ejcutar el sistema siguiendo los siguientes pasos:  
1. Ejecutar el micro servicio:  
   > python micro_servicios/sv_information.py  
1. Ejecutar el gui:  
   > python gui.py  
1. Abrir el navegador
1. Acceder a la url del sistema:
   > http://localhost:8000/ - página de inicio!
