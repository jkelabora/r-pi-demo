
import os
import boto
from boto import sqs
from boto.sqs.message import RawMessage

conn = boto.sqs.connect_to_region('ap-southeast-2')
sqs_q = conn.get_queue('raspberry-pipeline')
m = RawMessage()

# =========================================================
raw_input("Start First Pipeline...")
m.set_body('Build SUCCESS: WF - Prepare #')
sqs_q.write(m)

raw_input("unit tests pass...")
m.set_body('Build SUCCESS: WF - Unit Tests #')
sqs_q.write(m)

raw_input("integration tests pass...")
m.set_body('Build SUCCESS: WF - Integration Tests #')
sqs_q.write(m)

raw_input("deploy test pass...")
m.set_body('Build SUCCESS: WF - Deploy Test #')
sqs_q.write(m)

raw_input("deploy to QA pass...")
m.set_body('Build SUCCESS: WF - Deploy to QA #')
sqs_q.write(m)

raw_input("deploy to Production pass...")
m.set_body('Build SUCCESS: WF - Deploy to Production #')
sqs_q.write(m)

# =========================================================
raw_input("Start Second Pipeline...")
m.set_body('Build SUCCESS: RM - Prepare #')
sqs_q.write(m)

raw_input("unit tests pass...")
m.set_body('Build SUCCESS: RM - Unit Tests #')
sqs_q.write(m)

raw_input("integration test pass..")
m.set_body('Build SUCCESS: RM - Integration Tests #')
sqs_q.write(m)

raw_input("deploy test pass..")
m.set_body('Build SUCCESS: RM - Deploy Test #')
sqs_q.write(m)

raw_input("deploy to QA pass..")
m.set_body('Build SUCCESS: RM - Deploy to QA #')
sqs_q.write(m)

raw_input("deploy to Production pass..")
m.set_body('Build SUCCESS: RM - Deploy to Production #')
sqs_q.write(m)

# =========================================================
raw_input("Start Third Pipeline...")
m.set_body('Build SUCCESS: DT - Prepare #')
sqs_q.write(m)

raw_input("unit tests pass...")
m.set_body('Build SUCCESS: DT - Unit Tests #')
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
m.set_body('Build SUCCESS: DT - Deploy to QA #')
sqs_q.write(m)

raw_input("deploy to Production pass..")
m.set_body('Build SUCCESS: DT - Deploy to Produciton #')
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
    'OFFSET' : 4,
    'STAGE_WIDTH' : 2,
    'STAGES' : [ 'WF - Prepare', 'WF - Unit Tests', 'WF - Integration Tests', 'WF - Deploy Test', 'WF - Deploy to QA', 'WF - Deploy to Production' ]
}

# the entries in STAGES need to be case-sensitive matches of the jenkins build names
second_pipeline = {
    'OFFSET' : 14,
    'STAGE_WIDTH' : 2,
    'STAGES' : [ 'RM - Prepare', 'RM - Unit Tests', 'RM - Integration Tests', 'RM - Deploy Test', 'RM - Deploy to QA' 'RM - Deploy to Production' ]
}

third_pipeline = {
    'OFFSET' : 24,
    'STAGE_WIDTH' : 2,
    'STAGES' : [ 'DT - Prepare', 'DT - Unit Tests', 'DT - Deploy Test', 'DT - Deploy to QA', 'DT - Deploy to Production' ]
}
