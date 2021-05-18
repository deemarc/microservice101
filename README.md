# microservice101
my playground on testing out mircroservice stuff

# table of content
0. [How to use code in this github](#how-to-use-code-in-this-github)
1. [Connect it all together](#connect-it-all-together)
2. [rabbitmq_pubsub](#rabbitmq-pub-sub)
3. [celery](celery)

# how to use code in this github
This github repository contains many mini project that I have implemented to test out some of the common tools and architectur use in python microservice. (currently there will only for python microserive. let's see how thing goes)

the root directory will contain folders. 1 folder contain one project which is isolated and can run by it self. each will have their own readme for setup and run the project.

hope this will be benefits to others :)

# Connect it all together

Microservices, is as concept in which we break our one big giant serive (aka; monoligh) in to multiple mini services thus the name microservices. This seperation have lots of benefits for example; seperation of concern, scaling up (only the part that needs to be), and so on.

# rabbitmq pub sub
however, these mircroservice needs to work together thus there need to be a way to communicate each other. 
the popular way to do so is we provide a message bus (or message broker) that will delivering message between each microservices. here is where Rabbitmq will come in haddy

# celery
now let's see some common usecase of message broker. when a user user our flask api service. how ever their is a task that have some time comsuming task to be done. we would want our user to wait right? and also our service will be occupied and other customer won't be able to use our service. 

so, we will send this task to be run on background task.
these background task will be run using celery and it will get the message from our flask api telling what it need to be execute through message broker, rabbitmq