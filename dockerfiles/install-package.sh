#!/bin/bash
set -e

# Split the first argument into an array of words
contribs=("$@")
poetry config virtualenvs.create false
for arg in "${contribs[@]}"
do
    echo "Trying to install autogoal_$arg"
    # take core build out
    case $arg in 
        core)
            cd /home/coder/autogoal/autogoal && poetry install --no-dev --no-interaction --no-root
            cd /home/coder/autogoal && pip install -e autogoal
        ;;
        remote)
            cd /home/coder/autogoal/autogoal-remote && poetry install --no-dev --no-interaction --no-root
            cd /home/coder/autogoal && pip install -e autogoal-remote
        ;;
        common)
            cd /home/coder/autogoal/autogoal-contrib/autogoal_contrib && poetry install --no-dev --no-interaction --no-root
            cd /home/coder/autogoal/autogoal-contrib && pip install -e autogoal_contrib
        ;;
        *)
            cd "/home/coder/autogoal/autogoal-contrib/autogoal_$arg" && poetry install --no-dev --no-interaction --no-root
            cd "/home/coder/autogoal/autogoal-contrib" && pip install -e "autogoal_$arg"
        ;;
    esac
done

