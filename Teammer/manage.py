    # This file is part of Teammer.

    # Teammer is free software: you can redistribute it and/or modify
    # it under the terms of the GNU General Public License as published by
    # the Free Software Foundation, version 3.

    # Teammer is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    # GNU General Public License for more details.

    # You should have received a copy of the GNU General Public License
    # along with Teammer.  If not, see <http://www.gnu.org/licenses/>.


#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Teammer.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
