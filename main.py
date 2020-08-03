from helpers.args import Args
from models.core import Core

args = Args()
core = Core()

params = args.getParams()
entry = params.entry
output = params.output
session = params.session
message = params.message
command = params.command

status = core.start(entry, output, command, session)
callback = core.ask(message)

print('input >> ' + message)
print('output >> ' + callback)
print('status >> ' + status)
print('session >> ' + session)
