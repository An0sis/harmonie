# tailwind_watcher.py
import os
import subprocess


def run_tailwind_watch():
    """
    Runs TailwindCSS in watch mode for automatic recompilation.
    """
    os.chdir('home')
    command = [
        'npx',
        'tailwindcss',  # Make sure that this points to your tailwindcss file in your project.
        '-i', './static/src/input.css',  # input
        '-o', './static/src/output.css',  # output
        '--watch'
    ]
    print(os.getcwd())
    subprocess.run(command)
    print('TailwindCSS watcher started.')


run_tailwind_watch()
