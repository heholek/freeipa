# Authors:
#   Pavel Zuna <pzuna@redhat.com>
#   Adam Young <ayoung@redhat.com>
#   Endi S. Dewata <edewata@redhat.com>
#
# Copyright (c) 2010  Red Hat
# See file 'copying' for use and warranty information
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import print_function

import json

from ipaclient.frontend import CommandOverride
from ipalib.util import json_serialize
from ipalib.plugable import Registry

register = Registry()


@register(override=True)
class json_metadata(CommandOverride):
    def output_for_cli(self, textui, result, *args, **options):
        print(json.dumps(result, default=json_serialize))


@register(override=True)
class i18n_messages(CommandOverride):
    def output_for_cli(self, textui, result, *args, **options):
        print(json.dumps(result, default=json_serialize))
