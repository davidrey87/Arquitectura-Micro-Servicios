# Arquitectura-Micro-Servicios
Repositorio de la tarea 2

## Sistema de Procesamiento de Comentarios

Antes de ejecutar el código asegurate de instalar los prerrequisitos del sistema ejecutando:
> sudo pip install -r requirements.txt  

Los paquetes que se instalarán son los siguientes:

Paquete       | Versión | Descripción
--------------|---------|------------
Flask         | 0.10.1  | Micro framework de desarrollo
requests      | 2.12.4  | API interna utilizada en Flask para trabajar con las peticiones hacia el servidor
paralleldots  | 3.2.5   | Libreria de API para el analisis de sentimientos
python-twitte | 3.4.1   | Libreria de API para obtener mensajes de Twitter


*__Nota__: También puedes instalar éstos prerrequisitos manualmente ejecutando los siguientes comandos*   
> sudo pip install Flask==0.10.1  
> sudo pip install requests==2.12.4
> sudo pip install paralleldots==3.2.5  
> sudo pip install python-twitter==3.4.1

Una vez instalados los prerrequisitos es momento de ejcutar el sistema siguiendo los siguientes pasos:  
1. Ejecutar el servicio:  
   > python micro_servicios/sv_information.py  
1. Ejecutar el servicio:  
   > python micro_servicios/sv_sentiment.py  
1. Ejecutar el GUI:  
   > python gui.py  
1. Abrir el navegador
1. Acceder a la url del sistema:
   > http://localhost:8000/ - página de inicio!
