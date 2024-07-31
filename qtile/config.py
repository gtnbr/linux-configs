from libqtile import bar, layout, qtile, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os
import subprocess
import time

from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration, RectDecoration

color = [
    "e7ecf0",
    "1c1a24",
    "ad3d4a",
    "69a328",
    "fa9652",
    "3d497f",
    "7c3b5a",
    "5fada1",
    "9fada1",
    "9c9c9c"
]

lslash10 = {
    "decorations": [
        PowerLineDecoration(path="forward_slash", size=10)
    ]
}

rslash10 = {
    "decorations": [
        PowerLineDecoration(path="back_slash", size=10)
    ]
}

@hook.subscribe.startup
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])

mod = "mod4"
terminal = guess_terminal()

keys = [
    Key([mod], "j", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "k", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "i", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "m", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "i", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "control"], "j", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "k", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "i", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "delete", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    #OPEN programs keybinds
    Key([mod], "space", lazy.spawn("thunar"), desc="Launch file explorer"),
    Key([mod], "e", lazy.spawn("firefox"), desc="Launch firefox"),
    Key([mod], "s", lazy.spawn("spotify-launcher"), desc="Launch spotify"),
    Key([mod], "c", lazy.spawn("code .config/qtile/config.py"), desc="Open .config/qtile/config.py"),
    Key([mod], "v", lazy.spawn("code"), desc="Launch VSCodium"),
    Key([mod], "d", lazy.spawn("discord"), desc="Launch VSCodium"),
    Key([mod], "grave", lazy.spawn('rofi -show drun'), desc="Open rofi"),
    Key([mod], "q", lazy.spawn('lowriter'), desc="Open word"),
    Key([mod], "x", lazy.spawn('localc'), desc="Open excel"),
    Key([mod], "o", lazy.spawn('obsidian'), desc="Open obsidian")
]

for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}"
        )
    )

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )

layouts = [
    # layout.Columns(
    #     border_focus_stack=["#d75f5f", "#8f3d3d"],
    #     border_width=0,
    #     margin=10
    #     ),
    # layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    layout.Bsp(
        border_width=0,
        margin=10
    ),
    # layout.Matrix(
    #     border_width=0,
    #     margin=10
    # ),
    layout.MonadTall(
        border_focus_stack=["#d75f5f", "#8f3d3d"],
        border_width=0,
        margin=10
        ),
    # layout.MonadWide(
    #     border_width=0,
    #     margin=10
    # ),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="SourceCodeVF",
    fontsize=14,
    margin = 3.5,
    background = "#1c1a2455"
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Image(
                    filename = "~/.icons/qtile-bar/map-solid.svg",
                    background= color[5],
                    margin = 7,
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('rofi -show drun')},
                    **lslash10
                ),
                widget.GroupBox(
                    background=color[6],
                    active=color[1],
                    this_current_screen_border=color[4],
                    highlight_method="block",
                    inactive=color[0],
                    borderwidth=1,
                    padding_y=0,
                    **lslash10
                ),
                widget.Image(
                    filename = "~/.icons/qtile-bar/earth-americas-solid(1).svg",
                    background= color[4],
                    margin = 7,
                    mouse_callbacks = {'Button1': lazy.spawn("firefox")},
                    **lslash10
                ),
                widget.Spacer(
                    length=8,
                ),
                widget.Image(
                    filename = "~/.icons/qtile-bar/compass-solid.svg",
                    margin_y = 7.3,
                    margin_x = 0
                ),
                widget.Prompt(
                    margin=0
                ),
                widget.WindowName(
                    margin=0,
                ),
                widget.Chord(
                    chords_colors={
                        "launch": (color[5], color[0]),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Systray(),
                widget.Volume(
                    get_volume_command=True,
                    fmt="{}%"
                ),
                widget.OpenWeather(
                    location="liverpool",
                    format="{icon}",
                    **rslash10
                ),
                widget.Cmus(),
                widget.Clock(
                    format="%H:%M",
                    foreground=color[1],
                    background=color[4],
                    mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("alacritty -e bash -c \"cal -m -y; read\"")},
                    **rslash10
                ),
                widget.Clock(
                    format="%a",
                    foreground=color[0],
                    background=color[6],
                    mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("alacritty -e bash -c \"cal -m -y; read\"")},
                ),
                widget.Clock(
                    padding=0,
                    format="%d/%m/%y",
                    foreground=color[0],
                    background=color[6],
                    mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("alacritty -e bash -c \"cal -m -y; read\"")},
                ),
                widget.Spacer(
                    length=6,
                    background=color[6],
                    **rslash10
                ),
                widget.QuickExit(
                    background = color[5],
                    default_text="[X]",
                    countdown_format="[{}]"
                ),
            ],
            28,
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

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 24

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"