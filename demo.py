
import os
import boto
from boto import sqs
from boto.sqs.message import RawMessage

conn = boto.sqs.connect_to_region('ap-southeast-2')
sqs_q = conn.get_queue('r-pi')

raw_input("Press Enter to continue...")

m = RawMessage()
m.set_body('This is awesome...')
sqs_q.write(m)
















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
