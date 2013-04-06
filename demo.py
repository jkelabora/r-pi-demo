
import os
import boto
from boto import sqs
from boto.sqs.message import RawMessage

conn = boto.sqs.connect_to_region('ap-southeast-2')
sqs_q = conn.get_queue('r-pi')
m = RawMessage()

# =========================================================
raw_input("Start First Pipeline...")
m.set_body('Build SUCCESS: Prepare #')
sqs_q.write(m)

raw_input("unit tests pass...")
m.set_body('Build SUCCESS: Unit Tests #')
sqs_q.write(m)

raw_input("integration tests pass...")
m.set_body('Build SUCCESS: Integration Tests #')
sqs_q.write(m)

raw_input("deploy test pass...")
m.set_body('Build SUCCESS: Deploy Test #')
sqs_q.write(m)

raw_input("deploy to QA pass...")
m.set_body('Build SUCCESS: Deploy to QA #')
sqs_q.write(m)

raw_input("deploy to Production pass...")
m.set_body('Build SUCCESS: Deploy to Production #')
sqs_q.write(m)

# =========================================================
raw_input("Start Second Pipeline...")
m.set_body('Build SUCCESS: DT - Prepare #')
sqs_q.write(m)

raw_input("unit tests pass...")
m.set_body('Build SUCCESS: DT - Unit Test #')
sqs_q.write(m)

raw_input("oops! abort a hanging deploy test...")
m.set_body('Build ABORTED: DT - Deploy Test #')
sqs_q.write(m)

raw_input("nup... deploy test failed..")
m.set_body('Build FAILURE: DT - Deploy Test #')
sqs_q.write(m)

raw_input("fix the env... deploy test pass..")
m.set_body('Build SUCCESS: DT - Deploy Test #')
sqs_q.write(m)

raw_input("deploy to QA pass..")
m.set_body('Build SUCCESS: DT - Deploy QA #')
sqs_q.write(m)

# =========================================================




jenkins_regex = r"Build ([A-Z]+): (.*) #"

# the keys here are from the snsnotify-plugin, the values need to match the base_message_interface colours
jenkins_colours = {
    'FAILURE' : 'red',
    'SUCCESS' : 'green',
    'ABORTED' : 'white'
}

# the entries in STAGES need to be case-sensitive matches of the jenkins build names
first_pipeline = {
    'OFFSET' : 0,
    'STAGE_WIDTH' : 4,
    'STAGES' : [ 'Prepare', 'Unit Tests', 'Integration Tests', 'Deploy Test', 'Deploy to QA', 'Deploy to Production' ]
}

# the entries in STAGES need to be case-sensitive matches of the jenkins build names
second_pipeline = {
    'OFFSET' : 20,
    'STAGE_WIDTH' : 4,
    'STAGES' : [ 'DT - Prepare', 'DT - Unit Test', 'DT - Deploy Test', 'DT - Deploy QA' ]
}
