@echo off
echo Running QLDT Fast Login Generator...
python get_fast_login.py
if exist fast_login_link.txt (
    type fast_login_link.txt | clip
    echo Link has been copied to clipboard!
) else (
    echo Error: fast_login_link.txt not found
)
pause
