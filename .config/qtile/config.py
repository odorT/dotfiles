# -*- coding: utf-8 -*-

import os
import socket
import subprocess
from libqtile import backend, bar, layout, widget, qtile, hook
from libqtile.config import Click, Drag, Group, KeyChord, Key, Match, Screen
from libqtile.command import lazy
from libqtile.lazy import lazy
from typing import List  # noqa: F401

mod = "mod4"
terminal = "alacritty"

keys = [
    # My keybinds
    Key([mod], "Return", lazy.spawn(terminal)),
    Key([mod], "f", lazy.spawn("firefox")),
    Key([mod, "shift"], "Return",
        lazy.spawn("rofi -combi-modi window,drun,ssh  -show combi -icon-theme 'Papirus' -show-icons")),
    Key([mod, "shift"], "n", lazy.spawn("nemo")),
    Key([mod, "shift"], "g", lazy.spawn("gpaste-client ui")),
    Key([mod, "shift"], "c", lazy.spawn("code")),
    Key([mod], "i", lazy.spawn("betterlockscreen -l")),

    Key([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -1000")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +1000")),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),
    

    # The Essentials
    Key([mod], "Tab",
        lazy.next_layout(),
        desc="Toggle between layouts"
        ),
    Key([mod], "w",
        lazy.window.kill(),
        desc="Kill focused window"
        ),
    Key([mod, "control"], "r",
        lazy.restart(),
        desc="Restart Qtile"
        ),
    Key([mod, "control"], "q",
        lazy.shutdown(),
        desc="Shutdown Qtile"
        ),

    # Switch between windows
    Key([mod], "h",
        lazy.layout.left(),
        desc="Move focus to left"
        ),
    Key([mod], "l",
        lazy.layout.right(),
        desc="Move focus to right"
        ),
    Key([mod], "j",
        lazy.layout.down(),
        desc="Move focus down"
        ),
    Key([mod], "k",
        lazy.layout.up(),
        desc="Move focus up"
        ),
    Key([mod], "space",
        lazy.layout.next(),
        desc="Move window focus to other window"
        ),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h",
        lazy.layout.shuffle_left(),
        desc="Move window to the left"
        ),
    Key([mod, "shift"], "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right"
        ),
    Key([mod, "shift"], "j",
        lazy.layout.shuffle_down(),
        desc="Move window down"
        ),
    Key([mod, "shift"], "k",
        lazy.layout.shuffle_up(),
        desc="Move window up"
        ),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h",
        lazy.layout.grow_left(),
        desc="Grow window to the left"
        ),
    Key([mod, "control"], "l",
        lazy.layout.grow_right(),
        desc="Grow window to the right"
        ),
    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        desc="Grow window down"
        ),
    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        desc="Grow window up"
        ),
    Key([mod], "n",
        lazy.layout.normalize(),
        desc="Reset all window sizes"
        ),
]

# TODO fix MUS layout && add music station there
group_names = [
    ("WWW", {'layout': 'columns'}),
    ("DEV", {'layout': 'columns'}),
    ("SYS", {'layout': 'columns'}),
    ("CHAT", {'layout': 'columns'}),
    ("VBOX", {'layout': 'columns'}),
    ("MUS", {'layout': 'floating'}),
    ("VID", {'layout': 'columns'}),
    ("GAME", {'layout': 'max'}),
]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    # Switch to another group
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))
    # Send current window to another
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name)))


### DEFAULT COLOR SCHEME ###
# colors = [
#     ["#ffffff", "#ffffff"],  # 0
#     ["#A8E0FF", "#A8E0FF"],  # 1
#     ["#e1acff", "#e1acff"],  # 2
#     ["#e1acff", "#e1acff"],  # 3
#     ["#81F499", "#81F499"],  # 4
#     ["#e9c46a", "#e9c46a"],  # 5
#     ["#FF0000", "#FF0000"],  # 6
#     ["#264653", "#264653"],  # 7

#     ["#f4a261", "#f4a261"],  # 8
#     ["#e76f51", "#e76f51"],  # 9
#     ["#74438f", "#74438f"],  # 10
#     ["#2a9d8f", "#2a9d8f"],  # 11
#     ["#339ACC", "#339ACC"],  # 12
#     ["#4f76c7", "#4f76c7"],  # 13
#     ["#1D2330", "#1D2330"],  # 14
#     ["#1D1A31", "#1D1A31"],  # 15
# ]

colors = [
    ["#293136", "#293136"],  # color 0
    ["#3b4252", "#3b4252"],  # color 1
    ["#8c8c8c", "#8c8c8c"],  # color 2
    ["#565b78", "#565b78"],  # color 3
    ["#a1acff", "#a1acff"],  # color 4
    ["#ffffff", "#ffffff"],  # color 5
    ["#9293d2", "#9293d2"],  # color 6
    ["#89b8fd", "#89b8fd"],  # color 7
    ["#e2c5dc", "#e2c5dc"],  # color 8
    ["#0ee9af", "#0ee9af"],  # color 9
    ["#e9c46a", "#e9c46a"],  # color 10
    ["#4f76c7", "#4f76c7"],  # color 11
]

### DEFAULT WIDGET SETTINGS ###
extension_widget_defaults = dict(
    font='Dejavu Serif',
    fontsize=12,
    padding=2,
    rounded=True,
    margin_y=4,
    margin_x=3,
    background=colors[0]
)

layouts = [
    layout.Columns(
        border_focus = "#0ee9af",
        border_normal = "#808080",
        border_width=3,
        margin=5,
        border_on_single=True,
        margin_on_single=10,
    ),
    layout.Floating(),
    layout.MonadTall(
        # border_focus = colors[6],
        # border_normal = colors[4],
        border_width=3,
        margin=5,
        border_on_single=True,
        margin_on_single=10,
    ),
    layout.Max(),
]

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

screens = [
    Screen(
        top=bar.Bar(
            background=colors[1],
            margin=[5, 5, 1, 5],
            size=22,
            opacity=0.9,
            widgets=[
                widget.Sep(
                    background=colors[7],
                    linewidth=0,
                    padding=10
                ),
                widget.CurrentLayoutIcon(
                    custom_icon_paths=[os.path.expanduser(
                        "~/.config/qtile/icons")
                    ],
                    foreground=colors[1],
                    background="#565b78",
                    padding=5,
                    scale=0.7
                ),
                widget.Sep(
                    linewidth=4,
                    padding=10,
                    foreground=colors[5],
                    background=colors[0]),
                widget.GroupBox(
                    # font="trebuchet ms",
                    font="iosevka bold",
                    # font = "comic sans ms",
                    # font = "hack",
                    fontsize=10,
                    margin_y=3,
                    margin_x=2,
                    padding_y=5,
                    padding_x=5,
                    borderwidth=4,
                    active=colors[5],
                    inactive="#7e7e7e",
                    rounded=True,
                    highlight_color=colors[1],
                    highlight_method="block",
                    this_current_screen_border=colors[7],
                    this_screen_border=colors[6],
                    other_current_screen_border=colors[1],
                    other_screen_border=colors[1],
                    foreground=colors[8],
                    background=colors[0],
                ),
                widget.Sep(
                    linewidth=4,
                    padding=10,
                    foreground=colors[5],
                    background=colors[0]),
                widget.Prompt(
                    background=colors[8],
                    foreground=colors[0],
                    font="Novamono For Powerline",
                    fontsize=14,
                ),
                # widget.OpenWeather(
                #     font="Novamono For Powerline",
                #     fontsize=14,
                #     app_key = "cdbbb85813f4f2c81a1283fd5d720991",
                #     background = colors[8],
                #     foreground = colors[0],
                #     coordinates = [40.3777, 49.892],
                #     language = 'en',
                #     # fmt = ''
                # ),


                widget.Spacer(
                    background=colors[7],
                ),


                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper()),

                widget.TextBox(
                    text='',
                    background=colors[7],
                    foreground=colors[3],
                    padding=0,
                    fontsize=45
                ),
                widget.TextBox(
                    text='',
                    background=colors[3],
                    foreground=colors[8],
                    padding=0,
                    fontsize=45
                ),
                widget.Net(
                    font="Novamono for Powerline",
                    fontsize=14,
                    interface="enp37s0",
                    format='{down} ↓↑ {up}',
                    foreground=colors[1],
                    background=colors[8],
                    padding=5
                ),
                widget.TextBox(
                    text='',
                    background=colors[8],
                    foreground=colors[3],
                    padding=0,
                    fontsize=45
                ),
                widget.TextBox(
                    text='',
                    background=colors[3],
                    foreground=colors[6],
                    padding=0,
                    fontsize=45
                ),
                widget.TextBox(
                    text="CPU",
                    font="Novamono for Powerline",
                    fontsize=14,
                    foreground=colors[1],
                    background=colors[6],
                    padding=5,
                ),
                widget.GenPollText(
                    func = lambda: subprocess.check_output("/home/kamran/.local/bin/cpuload").decode("utf-8"),
                    font="Novamono for Powerline",
                    fontsize=14,
                    foreground=colors[1],
                    background=colors[6],
                    padding=2,
                    mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(terminal + ' -e htop')},
                ),
                widget.GenPollText(
                    update_interval = 1,
                    func = lambda: subprocess.check_output("/home/kamran/.local/bin/cputemp").decode("utf-8"),
                    font = "Novamono for Powerline",
                    fontsize = 14,
                    foreground = colors[1],
                    background = colors[6],
                    padding= 5,
                    mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(terminal + ' -e watch sensors')},
                ),
                widget.TextBox(
                    text='',
                    background=colors[6],
                    foreground=colors[3],
                    padding=0,
                    fontsize=45
                ),
                widget.TextBox(
                    text='',
                    background=colors[3],
                    foreground=colors[8],
                    padding=0,
                    fontsize=45
                ),
                widget.Memory(
                    background=colors[8],
                    foreground=colors[1],
                    font="Novamono for Powerline",
                    mouse_callbacks={
                        'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')
                    },
                    fontsize=14,
                    format='RAM {MemUsed: .0f} MB',
                ),
                widget.TextBox(
                    text='',
                    foreground=colors[3],
                    background=colors[8],
                    padding=0,
                    fontsize=45
                ),
                widget.TextBox(
                    text='',
                    background=colors[3],
                    foreground=colors[6],
                    padding=0,
                    fontsize=45
                ),
                widget.Systray(
                    background=colors[6],
                    icons_size=20,
                    padding=4
                ),
                widget.Sep(
                    linewidth=0,
                    padding=6,
                    foreground=colors[5],
                    background=colors[6],
                ),
                widget.Volume(
                    background=colors[6],
                    foreground=colors[1],
                    font="Novamono for Powerline",
                    fontsize=14,
                    mouse_callbacks={
                        'Button3': lambda: qtile.cmd_spawn("pavucontrol")
                    },
                ),
                widget.Sep(
                    linewidth=0,
                    padding=6,
                    background=colors[6],
                ),
                widget.TextBox(
                    text='',
                    background=colors[6],
                    foreground=colors[3],
                    padding=0,
                    fontsize=45
                ),
                widget.TextBox(
                    text='',
                    background=colors[3],
                    foreground=colors[8],
                    padding=0,
                    fontsize=45
                ),
                widget.Clock(
                    font="Novamono for Powerline",
                    foreground=colors[1],
                    background=colors[8],
                    fontsize=14,
                    format='%a  %d/%m | %I:%M %p',
                ),
                widget.Sep(
                    padding=10,
                    linewidth=0,
                    background=colors[7],
                    foreground=colors[7],
                ),

            ],
        ),
    ),
]

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

# @hook.subscribe.startup_once
# def startup():
#     Group("CHAT", spawn="slack")
#     Group("MUS", spawn="vlc")

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
