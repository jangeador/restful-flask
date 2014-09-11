# restful-flask

This is a small project that I created in order to learn more about creating restful services using Flask and then consuming said services using angularjs.

## Installation

1. Fork / Clone this project
2. Install the requirements in requirements.txt
3. modify the gunicorn_start file to match your environment
4. run the gunicorn_start script
5. open the client/index.html file to see in action


### Instructions to deploy the server on webfaction

#### Installing Supervisor

1. Install supervisor 
  ```pip3.4 install supervisor```

2. Create the file ```~/etc/supervisord.conf``` with the contents similar to below but modified for your environment
  ```sh
  [unix_http_server]
  file=/home/[your_username]/tmp/supervisor.sock
  
  [supervisord]
  logfile=/home/[your_username]/supervisor/logs/supervisord.log
  logfile_maxbytes=50MB
  logfile_backups=10
  loglevel=info
  pidfile=/home/[your_username]/etc/supervisord.pid
  
  [rpcinterface:supervisor]
  supervisor.rpcinterface_factory = supervisor.rpcinterface:make_main_rpcinterface
  
  [supervisorctl]
  serverurl=unix:///home/[your_username]/tmp/supervisor.sock
    
  [program:restful-flask]
  # change the next line to the location of the gunicorn_start script
  command=/home/[your_username]/projects/restful-flask/server/gunicorn_start
  user=[your_username]
  autostart=true
  autorestart=true
  redirect_stderr=true
  ```
3. Ensure that the log directory exists 
  ```mkdir -p ~/supervisor/logs```

#### Create the app in webfaction

4. Create the app in webfaction control panel

5. Select "Custom" as the App Category and "Custom app (listening on port) as the App Type"

#### Modify the gunicorn to use the parameters of the custom app
6. Modify the variables in ```gunicorn_start```

  ```sh
  NAME="Flask_Server"
  FLASKDIR=/home/[your_username]/projects/restful-flask/server
  VENVDIR=/home/[your_username]/.virtualenvs/restful-flask
  SOCKFILE=/home/[your_username]/projects/restful-flask/server/sock
  USER=[your_username]
  GROUP=[your_username]
  NUM_WORKERS=4
  # File name without the .py
  MODULE_NAME=server
  PORT=[port of the custom_app]
  ...
  ...
  ```

#### Restart Supervisor
7. Restart supervisord
  ```supervisorctl reload```
