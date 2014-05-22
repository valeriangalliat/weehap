import weechat

hap = '''
        $$$$$$$$$$
    $$$$$$$$$$$$$$$$$$
  $$$$    $$$$$$    $$$$
  $$  $$$$$$$$$$$$$$  $$
$$  $$    $$$$$$    $$  $$
$$  $$    $$$$$$    $$  $$
$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$  $$$$$$  $$$$$$$$
  $$$$$$$$      $$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$
    $$$$$$$$$$$$$$$$$$
        $$$$$$$$$$

'''

desc = 'Display colored hap smiley in current buffer.'


def hap_command(data, buffer, args):
    for line in hap.splitlines():
        weechat.command(buffer, '\x0307' + line)

    return weechat.WEECHAT_RC_OK


weechat.register('hap', 'Val', '1.0', 'Unlicense', desc, '', '')

# Display welcome message
weechat.prnt('', hap)

weechat.hook_command('hap', desc, '', '', '', 'hap_command', '')
