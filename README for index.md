# Directory Dashboard

A web-based dashboard for navigating and viewing a directory structure of files and folders. Built with HTML, JavaScript, and Tailwind CSS, it features a collapsible tree view and modals to display file contents, with specific support for fetching and showing Python (`.py`) file contents. The dashboard has a modern, dark-themed, responsive design.

## Features

- **Collapsible Directory Tree**: Expand/collapse folders to browse the directory structure.
- **File Interaction**:
    - **Python Files (`.py`)**: Click to fetch and display the file’s contents in a modal.
    - **Images (`.png`, `.jpg`, `.jpeg`, `.gif`)**: Displays a placeholder image (replaceable with actual images if hosted).
    - **Text Files (`.txt`, `.json`, `.csv`)**: Shows a placeholder message with the file path.
    - **Media Files (`.mp3`, `.mp4`)**: Shows a placeholder message with the file path.
- **Copy Path**: Copy the file path (e.g., `week1/000/0.py`) to the clipboard from the modal.
- **Responsive Design**: Works on desktop and mobile devices.
- **No External Dependencies**: Uses only Tailwind CSS via CDN.

## Prerequisites

- A directory structure with files (e.g., `week1/000/0.py`, `week1/000/function1.JPG`) in the correct paths.
- A local web server to serve files, as browsers restrict direct file access due to security policies. Options:
    - **XAMPP**: Apache-based server for Windows, macOS, or Linux.
    - **Python**: Lightweight server using `python -m http.server`.

## Setup Instructions

### Option 1: Using XAMPP

1. **Install XAMPP**:
    
    - Download and install XAMPP from [https://www.apachefriends.org](https://www.apachefriends.org).
    - Ensure Apache is enabled in the XAMPP control panel.
2. **Place Files**:
    
    - Copy `index.html` to the XAMPP `htdocs` directory (e.g., `C:\xampp\htdocs` on Windows or `/Applications/XAMPP/htdocs` on macOS).
    - Place the directory structure (`week1`, `week2`, etc.) in `htdocs`, ensuring files like `week1/000/0.py` are accessible.
3. **Start Apache**:
    
    - Open the XAMPP control panel and start the Apache server.
    - Allow Apache to listen on port 80 if prompted.
4. **Access the Dashboard**:
    
    - Open a browser and navigate to `http://localhost/index.html`.
    - The dashboard should display the directory tree.
5. **Test File Access**:
    
    - Expand `week1` > `000` and click `0.py`. The modal should show the contents of `0.py`.
    - If the file doesn’t load, verify it exists at `htdocs/week1/000/0.py` and Apache is running.

### Option 2: Using Python’s `http.server`

1. **Ensure Python is Installed**:
    
    - Confirm Python 3 is installed (`python --version` or `python3 --version`).
    - Available on Windows, macOS, or Linux.
2. **Place Files**:
    
    - Save `index.html` in the root directory with `week1`, `week2`, etc.
    - Ensure the directory structure matches the expected paths (e.g., `week1/000/0.py`).
3. **Start the Server**:
    
    - Open a terminal in the root directory (where `index.html` is located).
    - Run:
        
        ```bash
        python -m http.server 8000
        ```
        
    - The server will serve files on port 8000.
4. **Access the Dashboard**:
    
    - Open a browser and navigate to `http://localhost:8000/index.html`.
    - The dashboard should display the directory tree.
5. **Test File Access**:
    
    - Expand `week1` > `000` and click `0.py`. The modal should show the contents of `0.py`.
    - If the file doesn’t load, verify it exists at `week1/000/0.py` relative to the server’s root.

## Usage

- **Navigate the Tree**: Click folder names (yellow, with 📁 icon) to expand/collapse subfolders.
- **View Python Files**: Click a `.py` file (e.g., `0.py`) to fetch and display its contents in a modal.
- **View Other Files**:
    - Images: Shows a placeholder image (update `index.html` for local images).
    - Text/Media: Displays a placeholder message with the file path.
- **Copy Path**: Click "Copy Path" in the modal to copy the file path (e.g., `week1/000/0.py`).
- **Close Modal**: Click "Close" to dismiss the modal.

## Customizing for Local Files

If you have actual files (e.g., images, Python scripts):

1. **Update Image Paths**:
    
    - In `index.html`, modify the `getFileIconAndStyle` function for images:
        
        ```javascript
        action: `showModal('Image: ${file}', '<img src="./${fullPath}" alt="${file}" class="w-full h-auto rounded"><p class="mt-2">Image file at ${fullPath}</p>', '${fullPath}')`
        ```
        
    - Ensure images (e.g., `week1/000/function1.JPG`) are in the correct directory.
2. **Add Syntax Highlighting (Optional)**:
    
    - Include Prism.js for Python code highlighting:
        
        ```html
        <link href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-dark.min.css" rel="stylesheet" />
        <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-python.min.js"></script>
        ```
        
    - Update the Python modal content in `showPythonModal` to:
        
        ```javascript
        document.getElementById('modal-content').innerHTML = `<pre><code class="language-python">${content}</code></pre><p class="mt-2">Python script at ${path}</p>`;
        ```
        

## Troubleshooting

- **Python File Not Loading**:
    - Ensure the file exists (e.g., `week1/000/0.py`) in the server’s root directory.
    - Verify the server is running (`http://localhost:8000` for Python or `http://localhost` for XAMPP).
    - Check the browser console (Right-click > Inspect > Console) for errors like `404 Not Found` or CORS issues.
- **Image Not Displaying**:
    - Update the `src` in `getFileIconAndStyle` to use local paths (e.g., `./week1/000/function1.JPG`).
    - Ensure the file is accessible via the server.
- **Modal Not Appearing**:
    - Confirm JavaScript is enabled in the browser.
    - Check for console errors.
- **Server Issues**:
    - For XAMPP, ensure Apache is running and port 80 is not blocked.
    - For Python, try a different port if 8000 is in use (e.g., `python -m http.server 8080`).

## Notes

- The dashboard uses the hardcoded `directoryStructure` in `index.html` to match the provided folder/file structure.
- A local server is required to fetch file contents due to browser security restrictions.
- For advanced features (e.g., search, code editing, media playback), modify `index.html` or add a backend (e.g., Flask).

## Example

To view `week1/000/0.py`:

1. Ensure `0.py` exists in `week1/000/`.
2. Start the server (XAMPP or `python -m http.server 8000`).
3. Open `http://localhost:8000/index.html` (or `http://localhost` for XAMPP).
4. Expand `week1` > `000`, click `0.py`, and the modal will display the file’s contents.