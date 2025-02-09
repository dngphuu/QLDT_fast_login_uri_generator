# QLDT Fast Login Script

A Python script that generates a fast login link for the PTIT QLDT (Quản Lý Đào Tạo) system.

## Trash talk

The PTIT QLDT system's login process involves a slow redirect step that can be frustrating during time-sensitive activities like course registration. This script generates a direct login link that bypasses the redirect, significantly reducing login time.

Pro tip: Generate your fast login link about 20 minutes before course registration opens to ensure quick access when you need it most!

## Features

-   Generates a fast login URL that bypasses manual login
-   Saves the generated URL to a text file

## Prerequisites

-   Python 3.x
-   Required packages (install via `pip`):
    ```
    pip install -r requirements.txt
    ```
-   (Optional) For Linux users: `xclip` package for clipboard support
    ```bash
    # Ubuntu/Debian
    sudo apt-get install xclip
    # Fedora
    sudo dnf install xclip
    ```

## Setup

1. Clone this repository
2. Create a `.env` file in the project root with your credentials:
    ```
    USERNAME=your_qldt_username
    PASSWORD=your_qldt_password
    ```

## Usage

### Windows Users (Easiest Method)

1. Double click `get_link_and_copy.bat`
2. The script will:
    - Generate a fast login URL
    - Save it to `fast_login_link.txt`
    - Automatically copy the URL to your clipboard
3. Just paste (Ctrl+V) the link in your browser!

### Linux/Mac Users (Easiest Method)

1. Make the script executable (first time only):
    ```bash
    chmod +x get_link_and_copy.sh
    ```
2. Run the script:
    ```bash
    ./get_link_and_copy.sh
    ```
3. The script will:
    - Generate a fast login URL
    - Save it to `fast_login_link.txt`
    - Try to copy to clipboard if possible, or display the link for manual copying
4. Copy the link and paste (Cmd/Ctrl+V) it in your browser!

### Manual Method

Run the script directly:

```bash
python get_fast_login.py
```

The script will:

1. Generate a fast login URL using your credentials
2. Display the URL in the console
3. Save the URL to `fast_login_link.txt`

## Output

The generated link will be saved to `fast_login_link.txt` and can be used to directly access your QLDT account.

## Security Notes

-   Keep your `.env` file secure and never commit it to version control
-   The generated login link contains sensitive information - handle with care
-   Links expire after a certain period (~ 30 minutes)

## License

MIT License
