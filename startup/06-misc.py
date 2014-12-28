# misc stuff that trips me up

from datetime import datetime, timedelta
from numpy import arange

# lawls
@register_line_magic('past')
@register_line_magic('pase')
@register_line_magic('pate')
@register_line_magic('psat')
@register_line_magic('psate')
@register_line_magic('pasta')
def paste_copies(line):
    _ip.magics_manager.magics['line']['paste']()

del paste_copies


