#!/usr/bin/env python3

# Raise Exception when format of data went wrong
class DataFormatError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
