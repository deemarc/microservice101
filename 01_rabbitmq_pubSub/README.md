# Rabbitmq publish and subscribe
this is simple project that try out rabbitmq example using publish and subscribe python.

the message producer (publisher) will send the message into connected exchage, the exchane need to be set as a 'fanout' type so that the message will be send to all the queue that has been bind with it.

## setup
make sure that you current directory is in this folder before try to follow the steps

0. if you still did't get source code
    ```
    git clone [this_repository_url] 
    cd [project_folder]/01_rabbitmq_pubSub
    ```

1. <b>run up rabbitmq </b>

    In here I use docker compose (cause I plan to also populate it with other services in other project) but you can run it using docker command line or just run outside

    ```
    docker-compose up -d
    ```
2. Run subscriber
    
    in this project I didn't dockerise the service (to lazy haha) so, I recommended you to run It in virtual enviroment. you can run multiper instance of subsriber to see the publisher is actually send the message to all of them.
     
    ```
    virtualenv ./venv
    source ./venv/bin/activate
    python subscriber.py
    ```

3. Run publisher
    it will send message to all the subsriber
    ```
    source ./venv/bin/activate
    python publisher.py
    ```