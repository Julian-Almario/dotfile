from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os


mod = "mod4"
terminal = 'alacritty'
web = 'firefox'
notes = 'obsidian'
flashcards = 'anki'
cad = 'FreeCAD'
refadmin = 'Zotero'
epidemiology = 'jamovi'

# Colors
text_light = '#ebdbb2'

black = '#282828'
red = '#cc241d'
green = '#98971a'
yellow = '#d79921'
blue = '#458588'
purple = '#b16286'
aqua = '#689d6a'
orange = '#d65d0e'


keys = [
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
     

    # keys programs
    Key([mod], "t", lazy.spawn(terminal), desc="Launch terminal"),
    


    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),

    # Global keys important
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawn("rofi -show drun -show-icons -b -theme gruvbox-dark"), desc="Rofi"),
]

for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )


groups = [
    Group("1"),
    Group("2", matches=[Match(wm_class=[web])]),
    Group("3", matches=[Match(wm_class=[notes,flashcards])]),
    Group("4", matches=[Match(wm_class=[cad])]),
    Group("5", matches=[Match(wm_class=[epidemiology,refadmin])]),
    ]


# Switch windows in groups
for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc=f"Switch to group {i.name}",
            ),
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc=f"Switch to & move focused window to group {i.name}",
            ),
        ]
    )

layouts = [
    layout.Max(),
    layout.MonadTall(
        border_focus=orange,
        margin = 5
        )
    ]

widget_defaults = dict(
    font="Mononoki NF",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    highlight_method='block',
                    foreground=text_light,
                    this_current_screen_border=orange
                    ),
                widget.WindowName(),
                widget.Systray(),
                 widget.TextBox(
                    "",
                    fontsize=35,
                    padding=-1,
                    foreground=blue
                    ),
                widget.Battery(
                    format='{percent:2.0%}',
                    foreground=text_light,
                    background=blue
                    ),
                widget.CPU(
                    foreground=text_light,
                    background=blue
                    ),
                widget.ThermalSensor(
                    foreground=text_light,
                    background=blue
                    ),
                widget.Net(
                    format='{down:.0f}{down_suffix} ↓↑ {up:.0f}{up_suffix}',
                    foreground=text_light,
                    background=blue
                    ),
                widget.TextBox(
                    "",
                    fontsize=35,
                    padding=-1,
                    foreground=orange,
                    background=blue
                    ),
                widget.Memory(
                    foreground=text_light,
                    background=orange
                    ),
                widget.TextBox(
                    "",
                    fontsize=35,
                    padding=-1,
                    foreground=green,
                    background=orange
                    ),
                widget.Clock(
                    format="%I:%M %p",
                    foreground=text_light,
                    background=green,
                    )
            ],
            16,
            background=black
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
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
auto_minimize = True
wl_input_rules = None
wl_xcursor_theme = None
wl_xcursor_size = 24

wmname = "LG3D"


autostart = [
    "setxkbmap latam",
    "feh --bg-fil $HOME/Imágenes/Wallpapers/83.jpg",
    "picom &"
        ]


for x in autostart:
    os.system(x)
