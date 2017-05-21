#!/usr/bin/env python

import os
import random

def get_goat():
    with open('data/GOATNAMES', 'r') as f:
        goats = f.read()
        lines = goats.split('\n')
        return random.choice(lines)
        f.closed


def get_vid():
    with open('data/VIDS', 'r') as f:
        vids = f.read()
        lines = vids.split('\n')
        return random.choice(lines)
        f.closed


def reply_what():
    goatrand = random.randint(0,20)
    if goatrand > 18:
        return "Check out this goat. " + get_vid()
    else:
        return "Your goat name is " + get_goat()


def goat_tweet():
    goatrand = random.randint(0,20)
    if goatrand > 18:
        return "Check out this goat. " + get_vid()
    else:
        return get_goat()
