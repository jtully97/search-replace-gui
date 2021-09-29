#!/bin/bash

# Prior to running you must set permissions for this script to work.
# Set all permissions by running the command  - $chmod 755 'script-name'.sh - in your terminal/command prompt.
# Replacing 'script-name' with the name of the script.

DRY_RUN_Y_N=$1
SITE=$2
ENV=$3
SEARCH=$4
REPLACE=$5

if [[ "$DRY_RUN_Y_N" = "yes" ]]
then
    # Search replace dry run
    terminus wp $SITE.$ENV -- search-replace "$SEARCH" "$REPLACE" --url="$SEARCH" --all-tables --dry-run 2>&1 | tee terminal-output.txt
    exit 0
    
elif [[ "$DRY_RUN_Y_N" = "no" ]]
then
    # Search replace 
    terminus wp $SITE.$ENV -- search-replace "$SEARCH" "$REPLACE" --url="$SEARCH" --all-tables 2>&1 | tee terminal-output.txt
    echo "Complete!"
    exit 0
fi
