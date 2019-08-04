# -*- coding: utf8 -*-
print('Start Hello World function')
def main_handler(event, context):
    print(event)
    if 'key1' in event.keys():
        print("value1 = " + event['key1'])
    if 'key2' in event.keys():
        print("value2 = " + event['key2'])
    print("git file")
    return "hello from scf"  #return
