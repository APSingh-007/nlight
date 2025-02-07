#!/usr/bin/python3

import os
import click

@click.group()
def night_light():
    """Control Night Light on GNOME"""
    pass

@night_light.command()
def on():
    """Turn on Night Light"""
    os.system("gsettings set org.gnome.settings-daemon.plugins.color night-light-enabled true")
    click.echo("Night Light turned ON.")

@night_light.command()
def off():
    """Turn off Night Light"""
    os.system("gsettings set org.gnome.settings-daemon.plugins.color night-light-enabled false")
    click.echo("Night Light turned OFF.")

@night_light.command()
def toggle():
    """Toggle Night Light"""
    status = os.popen("gsettings get org.gnome.settings-daemon.plugins.color night-light-enabled").read().strip()
    if status == "true":
        os.system("gsettings set org.gnome.settings-daemon.plugins.color night-light-enabled false")
        click.echo("Night Light turned OFF.")
    else:
        os.system("gsettings set org.gnome.settings-daemon.plugins.color night-light-enabled true")
        click.echo("Night Light turned ON.")

if __name__ == "__main__":
    night_light()
