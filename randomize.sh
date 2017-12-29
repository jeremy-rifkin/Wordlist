#!/bin/bash
# Randomize the master.txt file
# remember to run `dos2unix randomize.sh` on windows
touch random.txt
shuf master.txt -o random.txt
