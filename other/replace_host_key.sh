#!/bin/bash

ssh-keygen -R $1 || true
ssh-keyscan -H $1 >> ~/.ssh/known_hosts
