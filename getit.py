#!/usr/bin/env python3

from mediafire.client import (MediaFireClient, File, Folder)

client = MediaFireClient()

client.login(app_id='45211')
client.download_file("mf:/i547ewwpknmh41l","thing")
