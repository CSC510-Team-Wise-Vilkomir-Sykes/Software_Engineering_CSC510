#!/bin/bash

# Using grep, find the pid of the infinite.sh script
pid=$(ps aux | grep infinite.sh | awk '{print $2}')

# Kill the process
kill $pid 2>/dev/null && echo "Process killed" || echo "Process not found"