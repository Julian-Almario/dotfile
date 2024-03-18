from libqtile import bar, layout, widget, extension
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.dgroups import simple_key_binder
import os
import json

mod = "mod4"
terminal = "alacritty"
browser = "firefox"
archivos = "caja"
vs = "code"

keys = [
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "t", lazy.spawn(terminal), desc="Launch terminal"),

    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]
#gruvbox colros

negro1 = '#282828'
orange1 = '#d65d0e'
orange2 = '#fe8019'
yellow1 = '#d79921'
yellow2 = '#fadb2f'
red1 = '#cc241d'
red2 = '#fb4934'
gray1 = '#a89984'

# groups = [Group(i) for i in "123456789"]
__groups = {
        1: Group("\ue795", matches=[Match(wm_class=["Alacritty"])]),
        2: Group("\ue745", matches=[Match(wm_class=browser)]),
        3: Group("\ue61e", matches=[Match(title=["Visual Studio Code"])]),
        4: Group("\uf187", matches=[Match(wm_class=["caja"])]),
        }

groups = [__groups[i] for i in __groups]

def get_group_key(name):
    return [k for k, g in __groups.items() if g.name == name][0]

for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                str(get_group_key(i.name)),
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            Key(
                [mod, "shift"],
                str(get_group_key(i.name)),
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )
dgroups_key_binder = simple_key_binder(mod)
layouts = [
    layout.Max(
        border_width=3,
        border_focus="fd971f",
        change_size=10,
        margin=6,
        ),
    layout.MonadTall(
        border_width=3,
        border_focus = "#fd971f",
        margin=6,
        change_size=10,
        ),
]

widget_defaults = dict(
    font="Mononoki NF",
    fontsize=14,
    padding=2,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    margin=3,
                    padding=9,
                    fontsize=25,
                    highlight_method = "line",
                    highlight_color=["#1d2021","#fb2034"],
                    this_current_screen_border= "#cc241d",
                    active= "#fd971f",
                    inactive= "#665c54",
                    block_highlight_text_color="#fbf1c7",
                    ),
                widget.Prompt(),
                widget.Spacer(),
                widget.TextBox(
                    text = '\uf438',
                    foreground = gray1,
                    fontsize = 45,
                    padding = -3.5,
                    ),
                widget.CurrentLayout(
                    background = gray1,
                    foreground = negro1,
                    fontsize = 20,
                    ),
                widget.TextBox(
                    text = '\uf438',
                    foreground = red2,
                    background = gray1,
                    fontsize = 45,
                    padding=-3.5
                    ),
                widget.Net(
                format = " \uf1eb {down} ↓↑ {up}",
                    padding=2,
                    background= red2,
                    foreground= negro1,
                    ),
                widget.TextBox(
                    text = '\uf438',
                    background = red2,
                    foreground = orange2,
                    fontsize = 45,
                    padding=-3.5
                    ),
                widget.Battery(
                    format = ' \ue315 {percent:2.0%}|',
                    background= orange2,
                    foreground = negro1
                    ),
                widget.ThermalSensor(
                format = '\uf2c7 {temp:.0f}| ',
                background= orange2,
                foreground = negro1
                    ),
                widget.CPU(
                    background= orange2,
                    foreground= negro1,
                    format='\ue266 {freq_current}GHz/{load_percent}%'
                    ),
                widget.TextBox(
                    text='| \uf85a',
                    background= orange2,
                    padding=5,
                    fontsize=20,
                    foreground = negro1,
                    ),
                widget.Memory(
                    background=orange2,
                    foreground = negro1,
                    ),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Systray(),
                widget.TextBox(
                        text = '\uf438',
                        background = orange2,
                        foreground = yellow1,
                        fontsize = 45,
                        padding= -3.5
                        ),
                widget.Clock(
                        background=yellow1,
                        foreground = negro1,
                        format=" %I:%M %p"
                        ),
                widget.QuickExit(
                    background=yellow1,
                    foreground = negro1,
                    default_text='\uf011',
                    countdown_format='\uead2',
                    padding=15,
                    ),
            ],
            29,
            background = negro1
        ),
    ),
]

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

#dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

autostart = [
        "setxbmap es",
        "feh --bg-fill /home/docz/Imágenes/Wallpapers/1163866.jpg",
        "picom &",
        "nitrogen --restore &",
        #"xrandr --auto"
        "xrandr --output eDP1 --auto --output HDMI1 --auto --above eDP1"
        ]

for x in autostart:
    os.system(x)
