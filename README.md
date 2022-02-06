# Primel Solver
*An interactive solver for Primel.*

[Primel](https://converged.yt/primel/) is a 5-digit prime number guessing game, in which the colour of digits will change to show how close a guess was to the prime. Using this information, the goal is to guess the 5-digit prime within 6 guesses.

This solver does this, from start to finish. Executables for Windows can be found in the `build` folder.

## Creating Standalone Executables

Those who do not trust the pre-built executables in the `build` folder, or those who are simply not using Windows, can instead choose to use the `.py` files in the `src` folder to create their own executables.

All of the provided `.py` files in the `src` folder can be run in the IDE but [PyInstaller](http://www.pyinstaller.org/) can be used to create standalone executables based on the OS that PyInstaller is run on.

First, ensure that PyInstaller is installed:

```Bash
pip install pyinstaller
```

To create a standalone executable we can use the following steps (which assume the use of Anaconda, but obvious modifications can be made for other distributions):

1. In the Anaconda Prompt, navigate to the directory containing the `.py` file.
2. `pyinstaller.exe --onefile filename.py`
3. Find the executable in the `dist` directory.
4. To clean up, delete everything but the produced executable.
