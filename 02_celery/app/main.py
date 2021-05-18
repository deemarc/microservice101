import json
from flask import Flask, request
import celery_task
import os

from datetime import datetime

app = Flask(__name__)


@app.route('/',methods = 'GET')
def index(): 
    return json.dumps({
        'message':"hello world"
    })


@app.route('/progress')
def progress():
    '''
    Get the progress of our task and return it using a JSON object
    '''
    jobid = request.values.get('jobid')
    if jobid:
        job = celery_task.get_job(jobid)
        if job.state == 'PROGRESS':
            return json.dumps(dict(
                state=job.state,
                progress=job.result['current'],
            ))
        elif job.state == 'SUCCESS':
            return json.dumps(dict(
                state=job.state,
                progress=1.0,
            ))

    return json.dumps({
        'job_id':jobid,
        'message':'end with error',
        'job_state':job.state

    })

@app.route('/result')
def result():
    '''
    Pull our generated .png binary from redis and return it
    '''
    jobid = request.values.get('jobid')
    if jobid:
        job = celery_task.get_job(jobid)
        return json.dumps({
            'result':job.get()
        })
    else:
        return 404




if __name__ == '__main__':
    app.run(host='0.0.0.0')