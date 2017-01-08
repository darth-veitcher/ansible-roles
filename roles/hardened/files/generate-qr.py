#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Builds a proper QR code from a ~/.google_authenticator file that can be
# scanned properly by a mobile phone.
#
# https://github.com/google/google-authenticator/wiki/Key-Uri-Format
#
'''
Files generated typically have the following structure:

G5QBC4WC42ID5TY6         # secret
"RATE_LIMIT 10 15        # n/a
" WINDOW_SIZE 5          # n/a
" TOTP_AUTH              # type
39081046                 # recovery codes ...
79232545
64524431
55543567
95315641
'''
from urllib import urlencode, quote
import os
import sys
import base64
import subprocess

URL = "otpauth://{type}/{issuer}:{label}?secret={secret}"
# URL = "otpauth://{type}/{label}?secret={secret}"
OPTIONALS = {
    'issuer': None,
    'algorithm': None,
    'digits': None,
    'period': None
}


def read_file(input):
    input_dict = {}
    with open(input, 'rb') as f:
        i = 0
        for line in f:
            line = line.strip('" \t\n')  # remove ",{space},{tab},{newline}
            if i == 0 and len(line) == 16:
                # base32 = base64.b32encode(line).strip('=')
                input_dict['secret'] = line  # ' '.join(base32[i:i+4] for i in xrange(0,len(base32),4))
            elif 'TOTP' in line:
                input_dict['type'] = 'totp'
            elif 'HOTP' in line:
                input_dict['type'] = 'hotp'
            i = i + 1

    return input_dict


def create_qr_string(args, **kwargs):
    input_dict = read_file(args.input_file)
    raw_url = URL.format(
        type=quote(input_dict['type']),
        issuer=quote(args.issuer),
        label=quote(args.user),
        secret=quote(input_dict['secret'])
    )
    usable_dict = {}
    for i in OPTIONALS:
        if args.__dict__.get(i, None):
            usable_dict[i] = args.__dict__[i]
        elif kwargs.get(i, None):
            usable_dict[i] = kwargs[i]
    if len(usable_dict) > 0:
        options = '&{0}'.format(urlencode(usable_dict))
    else:
        options = None
    return '{raw}{options}'.format(
        raw=raw_url,
        options=options if options else '').strip()


def create_qr_code(string, output):
    params = ['qrencode', '-s', '6', '-m', '5', '-t', 'PNG', '-o', output, string]
    subprocess.call(params, shell=False)


if __name__ == '__main__':
    import argparse
    response = None

    parser = argparse.ArgumentParser(description='Commandline settings')

    parser.add_argument('-i', '--input-file', required=True, help='~/.google_authenticator file to process')
    parser.add_argument('-u', '--user', required=True,
                        help='username to add as the label')
    parser.add_argument('--issuer', required=True,
                        help='issuer to add as the label')
    parser.add_argument('-o', '--output-file', required=True,
                        help='output file')
    args = parser.parse_args()

    if not os.path.isfile(args.input_file):
        sys.exit('Error. Unable to find input file.')
    else:
        response = create_qr_string(args)

    print(response.strip('" \t\n'))  # remove ",{space},{tab},{newline}
    create_qr_code(response.strip('" \t\n'), args.output_file)
