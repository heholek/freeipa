#
# Copyright (C) 2015  FreeIPA Contributors see COPYING for license
#

from ipaclient.frontend import MethodOverride
from ipalib import util
from ipalib.plugable import Registry
from ipalib.text import _

register = Registry()


@register(override=True)
class certprofile_show(MethodOverride):
    def forward(self, *keys, **options):
        if 'out' in options:
            util.check_writable_file(options['out'])

        result = super(certprofile_show, self).forward(*keys, **options)
        if 'out' in options and 'config' in result['result']:
            with open(options['out'], 'wb') as f:
                f.write(result['result'].pop('config'))
            result['summary'] = (
                _("Profile configuration stored in file '%(file)s'")
                % dict(file=options['out'])
            )

        return result
