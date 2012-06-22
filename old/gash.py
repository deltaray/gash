#!/usr/bin/python3

# Even though a python implementation may be easier and cleaner, it takes too long to run
# even without adding my own code. Just importing modules and processing a config
# file takes more than .1 seconds, which is already above my goal. So unfortunately
# a python implementation won't be very practical.  python2.7 was faster, but
# eventually it would have to be python3 anyways so what's the point?


# GASH by Mark Krenz (deltaray@slugbug.org)
# Additional help and input by the folks on the freenode#climagic channel.

# GAmified SHell, putting your interactive shell into a pseudo-fantasy setting.
# Written for most popular Unix shells including bash, zsh and tcsh.

# The idea behind this is to encourage more people to try advanced ideas in their
# shell, which gives them more experience points for doing so and eventually 
# raises your level. As you progress the levels, easier commands won't give you
# any experience points, so you'll have to learn to do more.

# Released under GPL 3.0 License.


########### PLEASE READ! #### PLEASE READ! #### PLEASE READ! ##################
#
# The source code is here so that you can check to make sure the program
# doesn't pull any shenanigans and so that you can customize it expand
# it if you want.
#
# Just because you can access the "game data" and see what lies ahead
# doesn't mean you should, nor should you share such game data with others
# and spoil the fun for everyone. Please respect that.
# Try to have fun and respect other's wish to do the same.
#
# This doesn't make the program any less open source, but how do you make an
# open source adventure game anyways without revealing everything?
#
########### PLEASE READ! #### PLEASE READ! #### PLEASE READ! ##################

VERSION = "0.3"

# Design considerations
# 1. Ideally, never take more than .25 seconds to run. <0.05 would be ideal, 0.1 acceptable.
# 2. Be stateless.
# 3. Be minimal.
# 4. Multiple shells on same user@host should be treated as one.
# 5. Be as simple as possible.
# 6. Try not to pry into user data. Respect privacy.




import argparse
import os
import configparser
import pickle

Config = configparser.ConfigParser()
Config.read("old/gashrc-sample.ini")

# Old syntax for calling in history mode.
#gashlastreturnvalue=\$? ; history | gash -i -C \$COLUMNS -l \$gashlastreturnvalue


# gash commands
#
#   Global options
#    -C <arg> - Specify width in columns
#    -V - Print version
#    -v[v[v]]] - Increase verbosity
#
#    histinput (Only intended for use on gash setup)
#         -l <arg> - Specify last command's return value
#
#  Commands below this are intended to be used more often by user. 
#
#    character
#    inventory
#    look "[item]" (By default, looks for what is in the room.)
#    take "<item>"
#    drop "<item>"
#    buy  "<item>"
#    sell "<item>"
#


# Parse commands and options

parser = argparse.ArgumentParser()
parser.add_argument('-C', action='store', type=int, default='80', help="Specify terminal's column width")
parser.add_argument('--version', '-V', action='version', version='%(prog)s '+VERSION)
parser.add_argument('--verbose' '-v', action='count', help='Increase output verbosity')

subparsers = parser.add_subparsers(help='sub commands')
histinput_parser = subparsers.add_parser('historyinput', help='Input history line for parsing.')
histinput_parser.add_argument('-l', action='store', type=int, help='Specify last command return code')


character_parser = subparsers.add_parser('character', aliases=['char', 'c'],  help='Show character info')

inventory_parser = subparsers.add_parser('inventory', aliases=['inv', 'i'], help='Show inventory')

look_parser = subparsers.add_parser('look', aliases=['l'], help='Look in the room')

examine_parser = subparsers.add_parser('examine', aliases=['ex', 'e'], help='Examine an object')
examine_parser.add_argument('item', help='Item you want to examine, this may need to be quoted.')

take_parser = subparsers.add_parser('take',aliases=['t'], help='Take an item')
take_parser.add_argument('item', help='Item you want to take, this may need to be quoted')

drop_parser = subparsers.add_parser('drop', aliases=['d'], help='Drop an item')
drop_parser.add_argument('item', help='Item you want to drop, this may need to be quoted')

buy_parser = subparsers.add_parser('buy', aliases=['b'], help='Buy an item')
buy_parser.add_argument('item', help='Item you want to buy, this may need to be quoted')

sell_parser = subparsers.add_parser('sell', aliases=['s'], help='Sell an item')
sell_parser.add_argument('item', help='Item you want to sell, this may need to be quoted')

args = parser.parse_args()

print(args)

user_homedir = os.environ['HOME']

# Gash setup
gash_configfile = user_homedir + "/.gashrc"
gash_savefile = user_homedir + "/.gashsave"


# ANSI/ASCII setup
ansi_reset = "\e[0m"

print (user_homedir)

utf8_box_chars = { 
    'upper_left_corner'  : '╭', 
    'upper_right_corner' : '╮', 
    'lower_left_corner'  : '╰', 
    'lower_right_corner' : '╯', 
    'vertical'           : '│', 
    'horizontal'         : '─', 
    'title_right'        : '╾', 
    'title_left'         : '╼', 
}

ascii_box_chars = {
    'upper_left_corner'  : '+',
    'upper_right_corner' : '+',
    'lower_left_corner'  : '\\',
    'lower_right_corner' : '/',
    'vertical'           : '|',
    'horizontal'         : '-',
    'title_right'        : '>',
    'title_left'         : '<',
}

box_chars = ascii_box_chars


print(box_chars['upper_left_corner'] + box_chars['horizontal'] + box_chars['upper_right_corner'] + '\n' + 
box_chars['vertical'] + ' ' + box_chars['vertical'] + '\n' +
box_chars['lower_left_corner'] + box_chars['horizontal'] + box_chars['lower_right_corner'] + '\n')


