
NOTICE
======
This program isn't fully ready for public decimation at this time. I've put
it on github, but that's mostly just to keep track of the code during development
and let a few people watch the progress. Please don't announce this anywhere
yet without getting my permission (deltaray@slugbug.org). Thanks.


Welcome
=======

Welcome to GASH. A filesystem filled with adventure.  GASH is a program that
allows you to [GA]mify your [SH]ell. You start out with a basic level 1 chracter
and progress according to your command line skills much like you would
in a fantasy role playing game.

For the most part, you can ignore gash and do your daily business. GASH will
just give you some feedback, rewards and encouragement along the way. You will
also be penalized if you make mistakes, which could lead to your eventual
demise.  Good luck.

Setup
=====

Put the gash program someplace.  I'd recommend putting it in your path
somewhere so its easier to run the GASH commands if you want to. If you don't
put it in your path somewhere, then in the setup below you'll need to specify
the full path to the gash program as well as use the full path to the program
when you run any of the gash commands.


BASH users:
-----------

  Set your PROMPT_COMMAND to the following.

  `PROMPT_COMMAND="lastreturn=\$? ; history | gash -i -C \$COLUMNS -l \$lastreturn"`

  You could also append this to something you already have, you'd just have to
  make sure that `lastreturn=\$?` happens before anything else so that you don't
  get the return value of something you run in the PROMPT_COMMAND value.

  You should setup this variable in your .bashrc file so that it is set when
  you start bash interactively each time.

ZSH users:
----------

  zsh has a similar function called precmd() for running programs before
  printing the normal PS1 prompt. Put this function in your .zshrc file:

  `function precmd() { lastreturn=$? ; history | gash -i -C $COLUMNS -l $lastreturn }`

  Note that you don't need to backslash the variable names like you do in the
  BASH example.
   

GASH commands
=============

Use your shell as you normally would. GASH just checks the return code
of each command you run and where you are in the filesystem for information
on what to do for scoring.

You can also get more involved with it by running some of the following commands
using the gash program. The commands take the following syntax.

  `gash <command> [object]`

  Where object could be an object you want to work with and command is one of
the following commands:

* __look__
* __inventory__
* __character__
* __take__
* __drop__
* __buy__
* __sell__

 Somewhere on the filesystem there is an in game store where you can buy
items that will help you during your journey. If you go into the store
you will be able to buy and sell items. Use `gash look` to see what
is available at the store.

Config file options
===================

### Settings can be one of the following types:
 * An alphanumeric string [a-zA-Z0-9]
 * A boolean value which can be one of yes, no, 1 or 0.
 * An alphanumeric list (string values as above, seperated by commas)

### Available settings

* __utf8_mode__ (default: yes) - Uses utf-8 characters available now on most popular terminals.

* __display_256colors__ (default: yes) - Use 256 color xterm output available now on most terminals.

* __hud_display__ (default: yes) - Turn on or off the character stats display (HUD = Heads Up Display)

* __hud_every_n_times__ (default: 1) - Another way you can control the display
           of the HUD is to only display it every so many commands. By
           default this is set to 1 (every time), but you can change this
           to something like 10 and it will only display the HUD every
           10th command. It determines this based on the command history
           number so it might not display right away after changing it.

* __hud_type__ (default: beforeprompt) - Change how the HUD is displayed.

    * _beforeprompt_ - A single line before each prompt.

    * _box_ - Draw a nice box in the upper right corner of your terminal.
          The setback of using this option is that it overwrites whatever
          was output from the previous command you ran in that corner
          of the terminal and it clutters up your scrollback history with
          every write.

    * _topline_ - A single line at the top of the terminal. This also
              has the drawback of overwriting the top line of your last 
              program's output.

    * _titlebar_ - Draws the HUD inside your terminal emulator's window titlebar.
               This can be a nice solution for getting it out of the way, however

* __hud_color_fg__ (default: white)- The foreground color of your HUD. See ANSI colors and attributes section.
* __hud_color_bg__ (default: normal) - The background color of your HUD. See ANSI colors and attributes section.
* __hud_color_attr__  A comma seperated list of ANSI attributes used on the HUD text. See ANSI colors and attributes section.

* __messages_display__ (default: yes) - The messages display comes up when you level up, encounter things, take damage, game messages, etc.
* __messages_color_fg__ (default: yellow) - The foreground color of the Messages area. See ANSI colors and attributes section.
* __messages_color_bg__ (default: normal) - The background color of the Messages area. See ANSI colors and attributes section.
* __messages_color_attr__  A comma seperated list of ANSI attributes used on the messages area. See ANSI colors and attributes section.

* __character_color_fg__ (default: blue) - The foreground color of the Character display. See ANSI colors and attributes section.
* __character_color_bg__ (default: normal) - The background color of the Character display. See ANSI colors and attributes section.
* __character_color_attr__  A comma seperated list of ANSI attributes used on the Character display. See ANSI colors and attributes section.

* __silence__ (default: no) - Controls all output of all messages and displays in GASH. Set to yes to turn all displays off.

* __leaderboard__ (default: no) - Connect with the GASH worldwide leaderboard at gash.climagic.org. (Doesn't work yet)
* __leaderboard_authcode__ (default: NULL) - Authentication code for connecting to leaderboard.


ANSI colors and attributes
==========================

The color settings can currently handle the following colors
for both fg and bg colors:

* black
* white
* red
* blue
* green
* yellow
* magenta
* cyan
* normal (for background, this is equivilent to transparent)

Also the following attributes are supported by gash, however your
terminal may not display some of them.

* normal
* __bold__  (bright and light are aliases for this)
* _italic_
* underline
* blink
* reverse (reverses the foreground and background colors)
* invisible 


Environment variables
=====================

The following environment variables can be set so you can quickly control some
aspects of gash that you may wish to override for a little bit:

* __GASH_HUD__ - Set to 0 to turn off the HUD. 
* __GASH_MESSAGES__ - Set to 0 to turn off the message display
* __GASH_SILENCE__ - Set to 1 to turn off all gash messages.
* __GASH_VERBOSE__, __GASH_DEBUG__ - This is for developers to quickly check things.

  Example of usage:

    `$ export GASH_HUD=0`

  To turn the HUD back on:

    `$ export -n GASH_HUD`  (This unexports the variable.)

    or 

    `$ unset GASH_HUD`


