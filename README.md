# Installation Guide

**OpenFOAM GUI Screening Task**  
**Author**: Kasim  
**Date**: February 2026

This guide walks you through installing both parts of the screening task: a Python binary tree package and a Blender addon. The whole process should take about 10-15 minutes.

---

## What You're Installing

**Task 1 - Binary Tree Package**: A Python library for working with binary tree data structures, with built-in YAML file support for saving and loading trees.

**Task 2 - Blender Addon**: A tool for creating and managing cube arrays in Blender, with intelligent merging features for building geometric structures.

---

## System Requirements

### For Task 1 (Binary Tree Package)
- Python 3.7 or newer
- pip (Python package installer)
- About 5 MB of disk space
- Works on Windows, Linux, and macOS

### For Task 2 (Blender Addon)
- Blender 3.0 or newer
- About 1 MB of disk space
- Works on Windows, Linux, and macOS

---

## Task 1: Installing the Binary Tree Package

### Quick Installation (3 steps)

```bash
# Navigate to the package folder
cd binarytree_package

# Install it
pip install -e .

# Test that it works
python -c "from binarytree import Node; print('Success!')"
```

If you see "Success!" printed out, you're all set!

### Detailed Installation

#### Check Your Python Version

First, make sure you have Python 3.7 or newer:

```bash
python --version
```

If you see something like "Python 3.9.7" or any version 3.7 or higher, you're good to go.

If you need to install Python:
- **Windows**: Download from python.org
- **Linux**: Run `sudo apt install python3 python3-pip`
- **macOS**: Run `brew install python3` (if you have Homebrew)

#### Check pip

You'll also need pip (it usually comes with Python):

```bash
pip --version
```

If pip isn't installed:

```bash
python -m ensurepip --upgrade
```

#### Install the Package

There are a few ways to install the package. I recommend the first method:

**Method 1: Development Mode** (recommended)

This creates a link to your source code, so any changes you make will take effect immediately:

```bash
cd binarytree_package
pip install -e .
```

**Method 2: Standard Installation**

This copies the files to your Python installation:

```bash
cd binarytree_package
pip install .
```

**Method 3: User Installation** (if you don't have admin rights)

```bash
cd binarytree_package
pip install --user -e .
```

#### Install Dependencies

The package needs PyYAML to work with YAML files. It should install automatically, but if it doesn't:

```bash
pip install pyyaml
```

### Verify the Installation

Let's make sure everything works:

**Test 1: Can you import it?**

```bash
python -c "from binarytree import Node, BinaryTree; print('Imports work!')"
```

**Test 2: Does it actually work?**

```python
python << EOF
from binarytree import BinaryTree

tree = BinaryTree()
tree.insert("", 10)
tree.insert("L", 5)
tree.insert("R", 15)

assert tree.count_nodes() == 3
print("Everything works!")
EOF
```

**Test 3: Run the full test suite**

```bash
cd binarytree_package
python tests/test_comprehensive.py
```

You should see a bunch of checkmarks and "ALL TESTS PASSED" at the end.

### Common Problems

**"pip: command not found"**

Try using `python -m pip` instead:

```bash
python -m pip install -e .
```

**"Permission denied"**

Use the user installation method:

```bash
pip install --user -e .
```

Or create a virtual environment (see the section below).

**"ModuleNotFoundError: No module named 'binarytree'"**

Check if it's installed:

```bash
pip list | grep binarytree
```

If it's not there, try installing again. If it is there but imports still fail, you might have multiple Python installations. Try:

```bash
which python  # Linux/macOS
where python  # Windows
```

Then use that specific Python path to install.

### Using a Virtual Environment (Optional but Recommended)

Virtual environments keep your project dependencies separate. Here's how to set one up:

```bash
# Create the virtual environment
python -m venv tree_env

# Activate it
source tree_env/bin/activate          # Linux/macOS
tree_env\Scripts\activate             # Windows

# Install the package
cd binarytree_package
pip install -e .

# When you're done working
deactivate
```

---

## Task 2: Installing the Blender Addon

### Quick Installation (4 steps)

1. Open Blender (version 3.0 or newer)
2. Go to Edit → Preferences → Add-ons
3. Click "Install..." and select `kasim_blender_addon/__init__.py`
4. Enable "OpenFOAM Cube Array Manager" by checking the box

To use it: Press N in the 3D Viewport, then click the "Cube Array" tab.

### Detailed Installation

#### Check Your Blender Version

Open Blender and go to Help → About Blender. You need version 3.0 or newer.

If you need to download Blender, get it from blender.org. Versions 3.6 or 4.0+ are recommended.

#### Install the Addon

**Step 1: Open Preferences**

You can do this in three ways:
- Menu: Edit → Preferences
- Quick: Press F4, then P
- Search: Press F3, type "preferences", hit Enter

**Step 2: Go to Add-ons**

Click the "Add-ons" tab on the left side of the Preferences window.

**Step 3: Install the File**

1. Click the "Install..." button in the top right
2. Navigate to where you extracted the files
3. Go into the `kasim_blender_addon` folder
4. Select the `__init__.py` file (important: select the file, not the folder)
5. Click "Install Add-on"

**Step 4: Enable It**

1. In the search box, type "OpenFOAM" or "Cube Array"
2. You should see "OpenFOAM Cube Array Manager"
3. Check the box next to it
4. The addon is now active!

**Step 5: Find the Panel**

1. Go to the 3D Viewport (the main window with the grid)
2. Press N to open the sidebar
3. Look for a tab called "Cube Array"
4. Click it to see the tools

### Verify the Installation

Let's test that everything works:

**Test 1: Can you see the panel?**

Press N in the 3D Viewport and look for the "Cube Array" tab. If you see it, you're good!

**Test 2: Create a test array**

1. Set "Number of Cubes" to 4
2. Click "Create Cube Array"
3. You should see 4 cubes appear in a 2×2 grid

**Test 3: Try the range validation**

1. Set "Number of Cubes" to 25
2. Click "Create Cube Array"
3. You should get an error message saying "The number is out of range"

If all three tests work, you're all set!

### Common Problems

**Addon doesn't appear in the add-ons list**

- Make sure you selected `__init__.py`, not the folder
- Check that you're using Blender 3.0 or newer
- Look at the console for error messages (Window → Toggle System Console)

**Addon won't enable**

- Open the system console and try to enable it again
- Look for Python error messages
- Make sure no other addon is conflicting with it

**Can't see the "Cube Array" tab**

- Press N to make sure the sidebar is visible
- Verify the addon is enabled in Preferences
- Make sure you're in the 3D Viewport, not another editor

**Buttons don't do anything**

- Make sure you're in Object Mode (check the top left of the viewport)
- For delete/merge operations, you need to select objects first
- Check the console for error messages

### Manual Installation (Alternative Method)

If the standard installation doesn't work, you can manually copy the addon:

**Find Blender's addon folder:**

- **Windows**: `C:\Users\YourName\AppData\Roaming\Blender Foundation\Blender\3.6\scripts\addons\`
- **Linux**: `~/.config/blender/3.6/scripts/addons/`
- **macOS**: `~/Library/Application Support/Blender/3.6/scripts/addons/`

(Replace "3.6" with your Blender version)

**Copy the folder:**

```bash
# Linux/macOS
cp -r kasim_blender_addon ~/.config/blender/3.6/scripts/addons/

# Windows Command Prompt
xcopy kasim_blender_addon "%APPDATA%\Blender Foundation\Blender\3.6\scripts\addons\kasim_blender_addon\" /E /I
```

Then restart Blender and enable the addon in Preferences.

---

## What to Do After Installing

### For Task 1 (Binary Tree Package)

Try creating your first tree:

```python
from binarytree import BinaryTree

tree = BinaryTree()
tree.insert("", 10)      # Root node
tree.insert("L", 5)      # Left child
tree.insert("R", 15)     # Right child

tree.print_tree()
print(tree.inorder())    # [5, 10, 15]
```

For more details, see README_TASK1.md.

### For Task 2 (Blender Addon)

Try creating your first array:

1. Press N in the 3D Viewport
2. Click the "Cube Array" tab
3. Set "Number of Cubes" to 9
4. Click "Create Cube Array"

You should see a 3×3 grid of cubes appear!

For more examples and details, see README_TASK2.md.

---

## Uninstalling

### Removing Task 1

```bash
pip uninstall binarytree_kasim
```

To completely clean up:

```bash
pip uninstall binarytree_kasim -y
pip cache purge
```

### Removing Task 2

1. Open Blender
2. Edit → Preferences → Add-ons
3. Find "OpenFOAM Cube Array Manager"
4. Click the arrow to expand it
5. Click "Remove"
6. Restart Blender

---

## Troubleshooting Tips

### General Advice

1. **Read error messages carefully** - they usually tell you what's wrong
2. **Check versions** - make sure you meet the requirements
3. **Try a fresh install** - sometimes starting over helps
4. **Use virtual environments** - they prevent a lot of problems

### Platform-Specific Notes

**Windows**:
- Hidden folders: Enable "Show hidden files" in File Explorer
- Python command: Try both `python` and `py`
- Paths: Use either `\` or `/` in file paths

**Linux**:
- Python command: Usually `python3` instead of `python`
- Hidden folders: Press Ctrl+H in file manager
- Permissions: Use `--user` flag if you're not root

**macOS**:
- Library folder: Press Shift+Cmd+G in Finder, then type the path
- Python: System Python or Homebrew Python both work
- Paths: Don't use sudo, use `--user` instead

---

## Getting Help

If you run into problems:

1. Check the error message carefully
2. Look at the troubleshooting section above
3. Review the detailed guides:
   - README_TASK1.md for the Python package
   - README_TASK2.md for the Blender addon
4. Check the console output for more details

---

## Installation Checklist

Before you start using the tools, make sure:

### Task 1
- [ ] Python 3.7+ is installed
- [ ] Package installs without errors
- [ ] You can import modules (`from binarytree import Node`)
- [ ] Basic tests pass
- [ ] Test suite runs successfully

### Task 2
- [ ] Blender 3.0+ is installed
- [ ] Addon appears in preferences
- [ ] Addon is enabled (box is checked)
- [ ] "Cube Array" tab shows up when you press N
- [ ] Test array creates successfully

---

## Quick Reference

### Task 1 Commands

```bash
# Install
pip install -e .

# Verify
python -c "from binarytree import Node; print('OK')"

# Test
python tests/test_comprehensive.py

# Uninstall
pip uninstall binarytree_kasim
```

### Task 2 Steps

```
Install: Edit → Preferences → Add-ons → Install → Select __init__.py
Enable: Check the box next to the addon
Access: Press N → Click "Cube Array" tab
Test: Set cubes to 9, click Create
```

---

That's it! Both tasks should now be installed and ready to use. The whole process takes about 10-15 minutes, and you'll need about 6 MB of disk space total.

If you want to learn how to use these tools, check out the README files for each task.