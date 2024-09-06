'''
    Script for turn on bomb in software Ignition
'''

if system.gui.confirm(u'Turn on bomb?', 'Confirm', True):
	def command_on(position):
		system.tag.write(event.source.parent.PATH + '/CMD_ON', position)
		
	if event.source.parent.RETENTIVO == True:
	
		command_on(True)
		
	else:
	
		command_on(True)
		system.util.invokeLater(lambda: command_on(False),2000)
		
'''
    Script for turn off bomb in software Ignition
'''

if system.gui.confirm(u'Turn off bomb?', 'Confirm', True):
	def command_off(position):
		system.tag.write(event.source.parent.parent.parent.PATH + '/CMD_OFF', position)

	if event.source.parent.parent.parent.RETENTIVO == True:
	
		command_off(True)
		
	else:
		command_off(True)
		system.util.invokeLater(command_off(False),2000)