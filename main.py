#!/usr/bin/python3

import subprocess

def run_command(command):
    result = subprocess.run(command, stdout=subprocess.PIPE)
    return result.stdout

def run_command_text(command):
    return run_command(command).decode("utf-8")

def main():
    mpvc = "/usr/bin/mpvc"

    out = run_command_text([mpvc])
    
    if out.startswith("No files added to "):
        print(out)
        return

    status = False
    raw = out.split("\n")[1].split("[")[1].split("]")[0]
    map = { "playing": True, "paused": False }
    status = False
    try:
        status = map[raw]
    except KeyError:
        print("Error getting mpvc status")
        print("raw = " + raw)
        return

    if status:
        print(run_command_text([mpvc, "pause"]))
    else:
        print(run_command_text([mpvc, "resume"]))

if __name__ == "__main__":
    main()
