# Requisitos de Instalación Generales

* __Instalación de Python 2.7__

    * Esta instalación Python requerie el compilador __GCC__ en su sistema,
      use el siguiente comando para instalar los requisitos previos de __Python 2.7__ antes de instalarlo.

      ```sh
         $ yum install gcc openssl-devel bzip2-devel
         o
         $ sudo apt install gcc openssl-devel bzip2-devel
      ```

    * Descarga __Python 2.7__

      ```sh
         $ cd /usr/src
         $ wget https://www.python.org/ftp/python/2.7/Python-2.7.tgz
      ```

    * Ahora extrae el paquete descargado.

      ```sh
         $ tar xzf Python-2.7.tgz
         $ cd Python-2.7
         $ ./configure --enable-optimizations
         $ make altinstall
      ```

        > __NOTA:__ \
        \
        __make altinstall__ se usa para evitar reemplazar el archivo binario predeterminado de python __/usr/bin/python__

    * Verifique la versión de Python

      ```sh
         $ python2.7 -V
      ```

    * Luego de realizar la verificación de la version de __python2.7__ \
     procederemos a realizar la instalación de __pip__ ejecutando los siguientes comandos:


      ```sh
         $ yum install epel-release -y
         $ yum update -y
         $ yum install python-pip -y
          
         o 

         $ sudo apt install epel-release -y
         $ sudo apt update -y
         $ sudo apt install python-pip -y

      ```

* __Instalación de virtualenv y virtualenvwrapper (Python)__

    * __virtualenvwrapper__ debe instalarse en el mismo área global de paquetes de sitio donde virtualenv está instalado.
      Es posible que necesite privilegios administrativos para hacer eso. La forma más fácil de instalarlo es usar __pip__

      ```sh
         $ pip install virtualenv
         $ pip install virtualenvwrapper
      ```

       o:

      ```sh
         $ sudo pip install virtualenv
         $ sudo pip install virtualenvwrapper
      ```

      > __NOTA:__ \
      \
      __virtualenv__ te permite crear muchos entornos virtuales diferentes de Python.
      Solo debe instalar virtualenv y virtualenvwrapper en su instalación base de Python (es decir, NO mientras un virtualenv está activo)
      para que el mismo release sea compartido por todos los entornos de Python que dependan de él.


        * Agregar variables de entorno en bash profile
    
          ```sh
              export WORKON_HOME=~/virtualenvs
              source /usr/bin/virtualenvwrapper.sh
          ```
    
          > __NOTA:__ \
          \
           Verificar si el bash existe en la siguente ruta: \
           \
           `/usr/bin/virtualenvwrapper.sh`



      ```
* __Clonar repositorio__

    * Utilice el siguiente comando para clonar repositorio.

      ```sh
         $ git clone https://github.com/stevedch/medical_backend.git

      ```

* __Crear entorno virtual y activar entorno virtual__

    * Utilice el siguiente comando para crear un entorno virtual.

      ```sh
         $ virtualenv --python=/usr/bin/python2.7 ~/.virtualenvs/medical_backend
      ```

    * Después de haber creado el entorno virual deberá activar el entorno creado con el 
      siguiente comando.

      ```sh
         $ source /home/[user]/.virtualenvs/medical_backend/bin/activate
      ```

`

* __Instalar proyecto__

    * Después de haber instalado el proyecto deberá dirigirse al proyecto.

      ```sh
         $ cd /home/steve/Escritorio/medical_backend
      ```

    * Deberá instalar las librerías ejecutando el siguiente comando.

      ```sh
         $ pip install -r requirements.txt
      ``` 

    * Deberá crear las migraciones del modelos ejecutando el siguiente comando.

      ```sh
         $ python manage.py makemigrations
      ```

    * Deberá persistir la migraciones de los modelos ejecutando el siguiente comando.

      ```sh
         $ python manage.py migrate
      ```

      > __NOTA:__ \
      \
         En el proyecto medical_backend se encuentra un archivo llamado dump.sql, este
         archivo contiene las inserciones de los modelos rol, user y ticket.  \
         Los usuarios para autenticar en la aplicación son: \
         -- USUARIO ADMINISTRADOR \
                user: root \
                password: admin.2018 \
         -- USUARIO ESTÁNDAR \
            user: root.2 \
            password: admin.2019

    * Deberá ejecutar el siguiente comando para levantar el servidor.

      ```sh
         $ python manage.py runserver 127.0.0.1:8000
      ```

    * Acceda a la siguiente url.

      ```sh
         $ http://127.0.0.1:8000/
      ```


Dependencias
============

| Name | URL |
| ------ | ------ |
| Python 2.7.5 | [https://www.python.org/ftp/python/2.7/Python-2.7.tgz] |
| virtualenv | [https://virtualenv.pypa.io/en/stable/installation/] |
| virtualenvwrapper | [https://virtualenvwrapper.readthedocs.io/en/latest/install.html] |