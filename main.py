import importlib

import runfiles
from absl import app, flags

flags.DEFINE_integer("day", None, "Challenge day to run")
flags.DEFINE_integer("part", None, "Can be 1 or 2 (for the challenge part)")

flags.mark_flags_as_required(["day", "part"])

FLAGS = flags.FLAGS


def main(argv):
    module_name = f'challenges.day_{FLAGS.day:02}'
    try:
        module = importlib.import_module(module_name)
    except ImportError:
        raise Exception(f"Module {module_name} can't be imported (does it exist?)")

    try:
        part_fn = getattr(module, f"part_{FLAGS.part}")
    except AttributeError:
        raise Exception(f"Function for part {FLAGS.part} not found in {FLAGS.day:02}.py")

    r = runfiles.Create()
    fstem = f"_main/input/day_{FLAGS.day:02}.txt"
    fname = r.Rlocation(fstem)
    if not fname:
        raise Exception(f"Can't find input file {fstem}")

    with open(fname, "r") as f:
        answer = part_fn(f)
        print(f"Result for day {FLAGS.day} part {FLAGS.part}: {answer}")

if __name__ == "__main__":
    app.run(main)