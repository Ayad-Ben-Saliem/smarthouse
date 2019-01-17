#!/bin/bash

ssh -o TCPKeepAlive=yes -o ServerAliveInterval=30 -R smarthouse.serveo.net:80:127.0.0.1:8000 serveo.net


