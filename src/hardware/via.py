#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  via.py
#
#  Copyright 2013 Antergos
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

""" VIA (openchrome) driver installation """

from hardware.hardware import Hardware
import os
import logging

CLASS_NAME = "Via"

DEVICES = [
('0x1106', '0x1122', "VX800/VX820 Chrome 9 HC3 Integrated Graphics"),
('0x1106', '0x3122', "VT8623 [Apollo CLE266] integrated CastleRock graphics"),
('0x1106', '0x3230', "K8M890CE/K8N890CE [Chrome 9]"),
('0x1106', '0x3260', "VIA Chrome9 HC IGP"),
#('0x1106', '0x3343', "P4M890 [S3 UniChrome Pro]"),
#('0x1106', '0x3344', "CN700/P4M800 Pro/P4M800 CE/VN800 Graphics [S3 UniChrome Pro]"),
('0x1106', '0x3371', "CN896/VN896/P4M900 [Chrome 9 HC]"),
('0x1106', '0x7122', "VX900 Graphics [Chrome9 HD]"),
#('0x1106', '0x7205', "KM400/KN400/P4M800 [S3 UniChrome]"),
('0x1106', '0x8e48', "")]

class Via(Hardware):
    def __init__(self):
        pass

    def get_packages(self):
        return ["xf86-video-openchrome"]

    def post_install(self, dest_dir):
        path = "%s/etc/X11/xorg.conf.d/10-via.conf" % dest_dir
        with open(path, 'w') as video:
            video.write('Section "Device"\n')
            video.write('\tIdentifier     "Device0"\n')
            video.write('\tDriver         "openchrome"\n')
            #video.write('\tOption         "EnableAGPDMA" "false"\n')
            #video.write('\tOption         "XaaNoImageWriteRect"\n')
            video.write('\tVendorName     "VIA"\n')
            video.write('EndSection\n')

    def check_device(self, device):
        """ Device is (VendorID, ProductID)
            DEVICES is (VendorID, ProductID, Description) """
        for (vendor, product, description) in DEVICES:
            if device == (vendor, product):
                logging.debug(_("Found device: %s") % description)
                return True
        return False
