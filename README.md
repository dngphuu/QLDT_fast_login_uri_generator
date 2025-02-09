# QLDT Fast Login Script

A Python script that generates a fast login link for the PTIT QLDT (Quản Lý Đào Tạo) system.

## Trash talk

The PTIT QLDT system's login process involves a slow redirect step that can be frustrating during time-sensitive activities like course registration. This script generates a direct login link that bypasses the redirect, significantly reducing login time.

Pro tip: Generate your fast login link about 20 minutes before course registration opens to ensure quick access when you need it most!

## Features

-   Generates a fast login URL that bypasses manual login
-   Automatically copies the generated URL to clipboard
-   Saves the generated URL to a text file

## Prerequisites

-   Python 3.x
-   Required packages (install via `pip`)

## Setup

1. Clone this repository
2. Install required packages:
    ```bash
    pip install -r requirements.txt
    ```
3. Create a `.env` file in the project root with your credentials:
    ```
    USERNAME=your_qldt_username
    PASSWORD=your_qldt_password
    ```

## Usage

Run the script directly:

```bash
python get_fast_login.py
```

The script will:

1. Generate a fast login URL using your credentials
2. Display the URL in the console
3. Automatically copy the URL to clipboard
4. Save the URL to `fast_login_link.txt`

Simply copy the generated URL and paste it into your browser to log in instantly!

## Output

The generated link will be saved to `fast_login_link.txt` and can be used to directly access your QLDT account.

## Security Notes

-   Keep your `.env` file secure and never commit it to version control
-   The generated login link contains sensitive information - handle with care
-   Links expire after a certain period (~ 30 minutes)

## Troubleshooting

1. If you get environment variable errors:

    - Check that your .env file exists in the same directory as the script
    - Ensure there are no spaces around the = sign in .env file
    - Make sure your credentials are correct

2. If the script runs but the link doesn't work:

    - The link expires after ~30 minutes
    - Generate a new link and try again
    - Check that you're copying the entire link

3. If the script fails to run:
    - Ensure Python and required packages are installed
    - Try running `pip install -r requirements.txt` again
    - Check if you have write permissions in the directory

## License

MIT License
