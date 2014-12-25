# misc stuff that trips me up

# lawls
@register_line_magic
def past(line):
     _ip.magics_manager.magics['line']['paste']()

@register_line_magic
def pase(line):
     _ip.magics_manager.magics['line']['paste']()

@register_line_magic
def pate(line):
     _ip.magics_manager.magics['line']['paste']()

@register_line_magic
def psat(lint):
     _ip.magics_manager.magics['line']['paste']()

@register_line_magic
def psate(line):
     _ip.magics_manager.magics['line']['paste']()

del past, pase, pate, psat, psate
