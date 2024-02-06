#!/usr/bin/python3
"""Defines an object's attribute lookup function."""


def lookup(obj):
    """Returns a list of an object's available attributes."""
    return (dir(obj))
