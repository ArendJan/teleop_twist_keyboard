#!/bin/bash

function pidwait()
{
    while [ -e "/proc/$1/exe" ]; do
        echo "Process $1 still running..."
        sleep 1
    done
    echo "Process $1 is done"
}
pidwait $1
