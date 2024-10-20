# Downloads Folder Organizer

This Python script automatically organizes files in your Downloads folder by categorizing them into subfolders based on their file types.

## Features

- Organizes files into predefined categories
- Moves folders into a separate "Folders" directory
- Handles various file types including documents, PDFs, images, videos, audio files, and more

## Requirements

- Python 3.x
- No additional libraries required (uses only built-in modules)

## Usage

1. Save the script as `organize_downloads.py` (or any preferred name).
2. Run the script:
   ```
   python organize_downloads.py
   ```
3. The script will automatically organize files in your Downloads folder.

## Categories

The script organizes files into the following categories:

- Office_docs: .docx, .pptx, .xlsx, .doc, .ppt, .xls
- Pdfs: .pdf
- Images: .jpg, .jpeg, .png, .gif, .svg
- Videos: .mp4, .mkv, .webm
- Audio: .mp3, .wav
- Compressed: .zip, .7z, .gz, .deb, .rar
- Html: .htm, .html, .php
- Text: .txt, .md, .ini, .sh, .csv
- Executables: .exe, .msi, .bat, .sh
- Folders: All directories not matching the above categories

## How It Works

1. The script accesses the user's Downloads folder.
2. It iterates through all items in the folder.
3. For files, it determines the file type and moves them to the appropriate category folder.
4. For folders, it moves them to the "Folders" directory (unless they are one of the category folders).

## Notes

- The script uses the user's home directory to locate the Downloads folder.
- Category folders are created if they don't already exist.
- Be cautious when running this script, as it will reorganize your entire Downloads folder.

## Customization

You can modify the `categories` dictionary in the script to add or change file type categorizations.

## Disclaimer

Use this script at your own risk. It's recommended to backup your Downloads folder before running the script for the first time.