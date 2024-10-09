#!/bin/bash

# Using grep, find the pid of the infinite.sh script

# echo $(ps aux)

cd .. && chmod +x infinite.sh && infinite.sh

pid=$(ps aux | grep infinite.sh | awk '{print $2}')

# Kill the process
kill $pid 2>/dev/null && echo "Process killed" || echo "Process not found"