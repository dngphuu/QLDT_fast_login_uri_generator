# QLDT Fast Login Script

A Python script for instant PTIT QLDT (Quản Lý Đào Tạo) system login.

## 🚀 Why Use This?

The PTIT QLDT system's standard login process is slow and involves multiple redirects. This script generates a direct login link that:

-   Bypasses the slow redirect process
-   Reduces login time significantly
-   Perfect for time-critical activities like course registration

> 💡 **Pro Tip**: Generate your fast login link 5-10 minutes before course registration opens!

## ✨ Features

-   One-click login URL generation
-   Automatic clipboard copy
-   URL backup in text file
-   Simple command-line interface

## 🔧 Prerequisites

-   Python 3.x
-   Internet connection
-   QLDT account credentials

## 📦 Quick Start

1. Install required packages:

    ```bash
    pip install -r requirements.txt
    ```

2. Create `.env` file with your credentials:

    ```
    USERNAME=your_qldt_username
    PASSWORD=your_qldt_password
    ```

3. Run the script:
    ```bash
    python get_fast_login.py
    ```

## 🎯 How to Use

1. Open terminal in project directory
2. Run `python get_fast_login.py`
3. Wait for the link generation
4. Paste the link in your browser (it's automatically copied!)

## 🔑 Security Notes

-   Never share your generated links
-   Keep your `.env` file private
-   Links expire after ~30 minutes
-   Generate new links as needed

## ⚠️ Common Issues

### "Environment variables not found"

-   Check `.env` file exists
-   Verify credentials format
-   No spaces around '=' sign

### "Link doesn't work"

-   Link might be expired
-   Generate a new link
-   Check complete URL was copied

### "Script won't run"

-   Run as administrator
-   Check Python installation
-   Verify required packages

## 📝 Files Description

-   `get_fast_login.py` - Main Python script
-   `requirements.txt` - Package dependencies
-   `.env` - Your credentials (create this)
-   `fast_login_link.txt` - Generated URL backup

## ⚖️ License

MIT License - Feel free to modify and share!

## 🤝 Contributing

Found a bug or want to improve the script? PRs are welcome!
