# Complete Installation Guide - Both Tasks

**OpenFOAM GUI Screening Task**  
**Author**: Kasim  
**Date**: February 2026

This guide covers installation for both screening tasks:
- **Task 1**: Binary Tree Package (Python)
- **Task 2**: Blender Addon

---

## 📋 Quick Links

- [Task 1: Binary Tree Package](#task-1-binary-tree-package)
- [Task 2: Blender Addon](#task-2-blender-addon)
- [System Requirements](#system-requirements)
- [Verification](#verification)
- [Troubleshooting](#troubleshooting)

---

## System Requirements

### Task 1: Binary Tree Package

| Requirement | Specification |
|-------------|--------------|
| **Python** | 3.7 or higher |
| **pip** | Latest version |
| **OS** | Windows, Linux, macOS |
| **Dependencies** | PyYAML >= 6.0 |
| **Space** | < 5 MB |

### Task 2: Blender Addon

| Requirement | Specification |
|-------------|--------------|
| **Blender** | 3.0 or higher |
| **OS** | Windows, Linux, macOS |
| **Dependencies** | None (uses Blender's Python) |
| **Space** | < 1 MB |

---

## Task 1: Binary Tree Package

### Quick Install (3 Steps)

```bash
# Step 1: Navigate to package
cd binarytree_package

# Step 2: Install
pip install -e .

# Step 3: Verify
python -c "from binarytree import Node; print('✓ Task 1 OK')"
```

### Detailed Installation

#### Prerequisites

**Check Python Version**:
```bash
python --version
# Need: Python 3.7+
```

**Check pip**:
```bash
pip --version
```

**If pip missing**:
```bash
python -m ensurepip --upgrade
```

#### Installation Methods

**Method 1: Development Mode (Recommended)**
```bash
cd binarytree_package
pip install -e .
```
- ✅ Can edit source code
- ✅ Changes apply immediately
- ✅ Good for testing

**Method 2: Standard Install**
```bash
cd binarytree_package
pip install .
```
- ✅ Clean installation
- ✅ Production ready

**Method 3: User Install (No Admin)**
```bash
pip install --user -e .
```
- ✅ No admin rights needed
- ✅ User-specific install

#### Install Dependencies

```bash
# Install PyYAML
pip install pyyaml>=6.0

# Or use requirements file
pip install -r requirements.txt
```

#### Verify Installation

**Test 1: Import Test**
```bash
python -c "from binarytree import Node, BinaryTree; print('✓ Imports OK')"
```

**Test 2: Functionality Test**
```python
python << EOF
from binarytree import BinaryTree
tree = BinaryTree()
tree.insert("", 10)
tree.insert("L", 5)
assert tree.count_nodes() == 2
print("✓ Functionality OK")
EOF
```

**Test 3: YAML Test**
```python
python << EOF
from binarytree import BinaryTree, write_tree_to_yaml
import os
tree = BinaryTree()
tree.insert("", 10)
write_tree_to_yaml(tree.root, "test.yaml")
assert os.path.exists("test.yaml")
os.remove("test.yaml")
print("✓ YAML OK")
EOF
```

**Test 4: Run Test Suite**
```bash
cd binarytree_package
python tests/test_comprehensive.py
# Should show: ✓ ALL TESTS PASSED
```

### Common Issues - Task 1

**Problem**: "ModuleNotFoundError: No module named 'binarytree'"
```bash
# Solution 1: Check installation
pip list | grep binarytree

# Solution 2: Reinstall
pip install -e .
```

**Problem**: "Permission denied"
```bash
# Solution: User installation
pip install --user -e .
```

**Problem**: "pip: command not found"
```bash
# Solution: Use python -m pip
python -m pip install -e .
```

### Task 1 Complete When:

- [ ] Python 3.7+ installed
- [ ] Package installed successfully
- [ ] Imports work
- [ ] Basic test passes
- [ ] YAML test passes
- [ ] Test suite passes

---

## Task 2: Blender Addon

### Quick Install (4 Steps)

```
1. Open Blender (3.0+)
2. Edit → Preferences → Add-ons → Install
3. Select kasim_blender_addon/__init__.py
4. Enable "OpenFOAM Cube Array Manager"
```

**Access**: Press `N` in 3D Viewport → "Cube Array" tab

### Detailed Installation

#### Prerequisites

**Check Blender Version**:
```
Help → About Blender
Need: Version 3.0 or higher
```

**Download Blender** (if needed):
- Website: [blender.org](https://www.blender.org/download/)
- Get version 3.6+ or 4.0+

#### Installation Steps

**Step 1: Open Preferences**
```
Method 1: Edit → Preferences
Method 2: Press F4, then P
Method 3: Press F3, type "preferences"
```

**Step 2: Go to Add-ons**
- Click "Add-ons" tab on left side

**Step 3: Install Addon**
1. Click "Install..." button (top right)
2. Navigate to `kasim_blender_addon` folder
3. Select `__init__.py` file
4. Click "Install Add-on"

**Step 4: Enable Addon**
1. Search for "OpenFOAM" or "Cube Array"
2. Check the checkbox next to addon name
3. Addon is now active

**Step 5: Access Panel**
1. Go to 3D Viewport
2. Press `N` key
3. Click "Cube Array" tab

#### Alternative: Manual Installation

**Find Blender's Addons Directory**:

**Windows**:
```
%APPDATA%\Blender Foundation\Blender\[VERSION]\scripts\addons\
```

**Linux**:
```
~/.config/blender/[VERSION]/scripts/addons/
```

**macOS**:
```
~/Library/Application Support/Blender/[VERSION]/scripts/addons/
```

**Copy Addon**:
```bash
# Linux/macOS
cp -r kasim_blender_addon ~/.config/blender/3.6/scripts/addons/

# Windows
xcopy kasim_blender_addon "%APPDATA%\Blender Foundation\Blender\3.6\scripts\addons\kasim_blender_addon\" /E /I
```

**Restart Blender** and enable addon in preferences.

#### Verify Installation

**Test 1: Panel Visibility**
```
1. Press N in 3D Viewport
2. Look for "Cube Array" tab
3. Should show panel with sections
```
✅ Expected: Panel is visible

**Test 2: Create Array**
```
1. Set "Number of Cubes" to 4
2. Click "Create Cube Array"
3. Should see 2×2 grid of cubes
```
✅ Expected: 4 cubes appear

**Test 3: Range Validation**
```
1. Set "Number of Cubes" to 25
2. Click "Create Cube Array"
3. Should show error popup
```
✅ Expected: "The number is out of range" error

**Test 4: Delete**
```
1. Create array (9 cubes)
2. Select 3 cubes
3. Click "Delete Selected Cubes"
```
✅ Expected: 3 cubes deleted

**Test 5: Merge**
```
1. Create 2×2 array
2. Select 2 adjacent cubes
3. Click "Merge Selected Meshes"
```
✅ Expected: Cubes merge into one

### Common Issues - Task 2

**Problem**: Addon doesn't appear in preferences
```
Solution 1: Check Blender version (need 3.0+)
Solution 2: Select __init__.py, not folder
Solution 3: Check console for errors
```

**Problem**: Addon won't enable
```
Solution 1: Check console for Python errors
Solution 2: Disable conflicting addons
Solution 3: Reinstall addon
```

**Problem**: "Cube Array" tab not visible
```
Solution 1: Press N to show sidebar
Solution 2: Check addon is enabled
Solution 3: Make sure in 3D Viewport
```

**Problem**: Buttons don't work
```
Solution 1: Check you're in Object Mode
Solution 2: Select objects (for delete/merge)
Solution 3: Check console for errors
```

### Task 2 Complete When:

- [ ] Blender 3.0+ installed
- [ ] Addon installed
- [ ] Addon enabled in preferences
- [ ] "Cube Array" tab visible
- [ ] Test array creates successfully
- [ ] Delete works
- [ ] Merge works

---

## Verification Checklist

### Both Tasks Complete When:

#### Task 1: Binary Tree
- [ ] Python 3.7+ installed and working
- [ ] Package installed via pip
- [ ] Can import: `from binarytree import Node`
- [ ] Basic operations work
- [ ] YAML integration works
- [ ] All tests pass

#### Task 2: Blender Addon
- [ ] Blender 3.0+ installed and running
- [ ] Addon appears in preferences
- [ ] Addon is enabled
- [ ] Panel visible in sidebar
- [ ] Can create cube arrays
- [ ] Can delete selected cubes
- [ ] Can merge adjacent meshes

---

## Troubleshooting Both Tasks

### General Debugging Steps

1. **Check Versions**
   - Task 1: `python --version` (need 3.7+)
   - Task 2: Blender → Help → About (need 3.0+)

2. **Check Console Output**
   - Task 1: Terminal/command prompt
   - Task 2: Window → Toggle System Console

3. **Try Fresh Install**
   - Task 1: `pip uninstall binarytree_kasim -y` then reinstall
   - Task 2: Remove addon and reinstall

4. **Check File Paths**
   - Make sure you're in correct directory
   - Verify file structure is intact

5. **Read Error Messages**
   - Python errors usually point to the issue
   - Blender console shows Python errors

### Platform-Specific Issues

**Windows**:
- Use `python` or `py` command
- Check Python is in PATH
- Show hidden folders (%APPDATA%)

**Linux**:
- Use `python3` explicitly
- May need `sudo apt install python3-pip`
- Hidden folders start with dot

**macOS**:
- Use Homebrew Python or system Python
- Library folder may be hidden
- Use Finder → Go → Go to Folder

---

## Virtual Environment (Optional but Recommended)

### Why Use Virtual Environment?

✅ Isolated dependencies  
✅ No admin rights needed  
✅ Clean separation  
✅ Easy to delete  

### Setup Virtual Environment

```bash
# Create virtual environment
python -m venv openfoam_env

# Activate it
# On Linux/macOS:
source openfoam_env/bin/activate
# On Windows:
openfoam_env\Scripts\activate

# Install Task 1
cd binarytree_package
pip install -e .

# Verify
python -c "from binarytree import Node; print('✓ Works in venv')"

# When done
deactivate
```

---

## Post-Installation

### Next Steps for Task 1

1. **Read Documentation**: See README_TASK1.md
2. **Try Examples**: Run examples/example_usage.py
3. **Run Tests**: Execute tests/test_comprehensive.py
4. **Start Coding**: Create your first tree!

```python
from binarytree import BinaryTree

tree = BinaryTree()
tree.insert("", 10)
tree.insert("L", 5)
tree.insert("R", 15)
tree.print_tree()
```

### Next Steps for Task 2

1. **Read Documentation**: See README_TASK2.md
2. **Try Examples**: See EXAMPLES.md
3. **Test Features**: Follow TESTING.md
4. **Create First Array**: Press N → Cube Array!

```
Set cubes: 9
Click: Create Cube Array
Result: 3×3 grid appears!
```

---

## Installation Summary

### Time Required

**Task 1**: 5-10 minutes
- Install Python (if needed): 5 min
- Install package: 2 min
- Verify installation: 3 min

**Task 2**: 2-5 minutes
- Install Blender (if needed): varies
- Install addon: 2 min
- Verify installation: 3 min

**Total**: 10-15 minutes for both tasks

### Disk Space

**Task 1**: < 5 MB
- Package: ~2 MB
- Dependencies: ~3 MB

**Task 2**: < 1 MB
- Addon: < 100 KB
- (Blender itself: ~300 MB if downloading)

---

## Getting Help

### Resources

**Task 1 Documentation**:
- README_TASK1.md - Complete guide
- INSTALLATION_TASK1.md - Detailed install
- TESTING.md - Test procedures

**Task 2 Documentation**:
- README_TASK2.md - Complete guide
- INSTALLATION_TASK2.md - Detailed install
- EXAMPLES.md - Usage examples
- TESTING.md - Test checklist

### Support Channels

1. **Read error messages carefully**
2. **Check console output**
3. **Refer to troubleshooting sections**
4. **Verify system requirements**

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
Install: Edit → Preferences → Add-ons → Install
Enable: Check checkbox
Access: Press N → Cube Array tab
Test: Create array with N=9
```

---

## Final Checklist

Before proceeding to use the tasks, verify:

### Task 1: Binary Tree Package
- [ ] Python 3.7+ installed
- [ ] pip working
- [ ] Package installed (`pip list | grep binarytree`)
- [ ] Can import modules
- [ ] Tests pass
- [ ] Ready to use

### Task 2: Blender Addon  
- [ ] Blender 3.0+ installed
- [ ] Addon installed and enabled
- [ ] Panel visible in sidebar
- [ ] Test array works
- [ ] All features functional
- [ ] Ready to use

---

**Both tasks should be fully functional after following this guide. If you encounter any issues, refer to the detailed troubleshooting sections or the task-specific installation guides.**

**For detailed usage instructions:**
- **Task 1**: See README_TASK1.md
- **Task 2**: See README_TASK2.md

**Installation complete! You're ready to use both screening tasks.**
