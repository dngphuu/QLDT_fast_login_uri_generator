#!/bin/bash
echo "Running QLDT Fast Login Generator..."
python3 get_fast_login.py

if [ -f fast_login_link.txt ]; then
    if [ "$(uname)" == "Darwin" ] && command -v pbcopy >/dev/null 2>&1; then
        # macOS with pbcopy
        cat fast_login_link.txt | pbcopy
        echo "Link has been copied to clipboard!"
    elif command -v xclip >/dev/null 2>&1; then
        # Linux with xclip
        cat fast_login_link.txt | xclip -selection clipboard
        echo "Link has been copied to clipboard!"
    else
        # Fallback: Just display the link
        echo "Here's your login link (clipboard utilities not found):"
        echo "---------------------------------------------------"
        cat fast_login_link.txt
        echo "---------------------------------------------------"
        echo "TIP: Select the link above and copy it manually"
    fi
else
    echo "Error: fast_login_link.txt not found"
fi
