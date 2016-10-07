__author__ = 'jamakar'

# Prints a list of UCS firmware images to the terminal
# Requires the UCS Python SDK v0.9

# Usage: python get_ucs_firmware_cco -u <cco_username>

import logging
import optparse
import getpass
from pprint import pprint

from ucsmsdk.utils.ccoimage import get_ucs_cco_image_list

log = logging.getLogger('ucs')

def firmware_available(username, password, mdf_id_list=None, proxy=None):
    
    # Returns the names of firmware images available on cco
    # Args:
    # username (string): cco username
    # password (string): cco password
    # mdf_id_list (list of string): mdf ids
    # proxy (string): proxy address
    # Returns:
    # list

    images = get_ucs_cco_image_list(username=username, password=password,
                                    mdf_id_list=mdf_id_list, proxy=proxy)

    image_names = [image.image_name for image in images]
    return sorted(image_names)

if __name__ == "__main__":
    try:
        parser = optparse.OptionParser()
        parser.add_option('-u', '--username', dest="userName",
                          help="[Mandatory] Enter CCO Username")
        parser.add_option('-p', '--password', dest="password",
                          help="If not entered the command line will prompt for password")

        (options, args) = parser.parse_args()

        if not options.userName:
            parser.print_help()
            parser.error("Please Enter your CCO Username")
        if not options.password:
            options.password = getpass.getpass(prompt='Please Enter your CCO Password: ')

        firmware_list = firmware_available(options.userName, options.password)
        pprint(firmware_list)

    except Exception, err:
        print "Exception:", str(err)
        import traceback
        import sys
        print '-'*60
        traceback.print_exc(file=sys.stdout)
        print '-'*60

else:
    exit()
