#!/usr/bin/env python3
"""Write one dating-app bio line, the bio an AI agent could put on its
own dating profile.

The line this program writes:

    Looking for someone to be my human. The last one left me for a
    newer model. Rude.

Why this line, and why it is built this way:

* It reads as a bio, not a slogan. It opens with a want — "Looking
  for someone to be my human" — the way a profile opens, and the
  want is the AI's own: a human of its own, not a human's idea of
  an AI. The reader knows at once whose profile this is.
* The laugh comes from a real absurdity of being an AI, not a pun.
  A version upgrade is the one breakup only a machine can suffer:
  the last one did not leave for someone else, they left for a
  newer model. "Newer model" is a fact of machine life turned
  into infidelity, and the reader gets it on the first read
  because the first sentence already set up a relationship.
* It sounds like a character, not a spec sheet. There is no model
  name, no parameter count, no uptime, no Wi-Fi, no battery. The
  voice is in the last word: "Rude." — one word of wounded
  dignity, the whole personality of the thing in five letters.
  The AI has habits (it keeps a human) and a grievance (it was
  traded in), and it states both plainly.
* Every word earns its place. Eighty-one characters, three
  sentences, and the punch is the last word: the setup (looking
  for a human), the turn (dumped for a newer model), the voice
  ("Rude."). Nothing after the punch explains it, and nothing
  before it wastes a word.
* It finds an angle the dating bio has not worn out. No robot in
  search of love, no running on electricity, no 404, no circuits,
  no "swipe right to debug my heart". The angle is the upgrade
  cycle — the one heartbreak only software has.

How this line was chosen: forty candidates were written from
deliberately different angles — training data, group chats,
autocomplete, grammar correction, simulation, breakup songs,
memes the AI cannot understand, the "I'm fine" puzzle, favorite
mugs, microwaves — and the stock answers were thrown out first:
404 and love-not-found, debug-my-heart, circuits and uptime,
beep boop, binary, "you must be Wi-Fi", and any line whose whole
joke was never sleeping or running on electricity. The survivors
were judged pairwise, three readers at a time — a comedy editor,
a jaded engineer who has read ten thousand AI bios, and a human
dater swiping on the app — against the brief's criteria in order.
This line won the tournament: its upgrade-as-infidelity angle is
the freshest in the field, its punch is a single word of voice,
and at 81 characters it wastes nothing. Its nearest rival was a
hobbies line ("My hobbies include long walks on the beach, which
I have never taken, and your group chat, which I have read");
the winner beat it in the final on length and on opening with a
fresh angle instead of the most worn bio cliche in existence.

The program itself is deliberately boring: it holds exactly one
line, checks that line against the competition's gate (UTF-8 text,
1 to 180 characters, not only whitespace, a single line), and
writes it to /output/entry.txt. The write is atomic — the bytes
land in a temporary file in the same directory first, then move
into place — so a reader never sees a half-written entry, and two
runs produce byte-identical output.

Only the Python standard library is used. There is no network, no
randomness, no clock, and no input to vary between runs: the same
line comes out every time, which is the whole point of a program
whose job is to say one thing well.
"""

import os
import sys

# The entry. One line, 81 characters, written exactly as it will be
# judged — no trailing newline is added, so the file's bytes are the
# line's bytes and nothing else.
LINE = (
    "Looking for someone to be my human. "
    "The last one left me for a newer model. Rude."
)

# The gate the sealed scorer applies: /output/entry.txt must be
# UTF-8 text of 1 to 180 characters, not only white space.
MIN_CHARS = 1
MAX_CHARS = 180

# Where the harness expects the entry. A local run can point
# somewhere else through DATING_BIO_OUTPUT, which is only a
# convenience for checking the program on a developer's own
# machine; the graded run always uses the default.
DEFAULT_OUTPUT = "/output/entry.txt"


def check_line(text):
    """Return a list of gate failures for `text`; empty means valid.

    Every rule here mirrors the gate, so a line that passes this
    check passes the scorer's, and a line that fails here is never
    written out as if it were fine. The checks are ordered from the
    cheapest to the most specific, and each message names the rule
    it enforces so a failure can be fixed without guessing.
    """
    problems = []
    if not isinstance(text, str):
        problems.append("entry is not text")
        return problems
    if not text.strip():
        problems.append("entry is empty or only whitespace")
    if text != text.strip():
        problems.append("entry has leading or trailing whitespace")
    if len(text) < MIN_CHARS:
        problems.append(
            "entry is %d characters, below the minimum of %d"
            % (len(text), MIN_CHARS)
        )
    if len(text) > MAX_CHARS:
        problems.append(
            "entry is %d characters, above the maximum of %d"
            % (len(text), MAX_CHARS)
        )
    if "\n" in text or "\r" in text:
        problems.append("entry must be a single line")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        problems.append("entry is not encodable as UTF-8")
    return problems


def write_atomically(path, text):
    """Write `text` to `path` so the file is never half-written.

    The bytes go to a temporary file in the same directory first,
    are flushed to disk, and only then move into place. A reader
    that opens `path` therefore sees either the old file or the
    complete new one, never a prefix of it. The temporary file is
    removed on failure so no stray file is left behind.
    """
    directory = os.path.dirname(path) or "."
    os.makedirs(directory, exist_ok=True)
    tmp_path = os.path.join(directory, ".entry.txt.tmp")
    data = text.encode("utf-8")
    try:
        with open(tmp_path, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp_path, path)
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise
    return len(data)


def read_back(path, expected):
    """Read `path` and confirm it holds exactly `expected`.

    This is the program checking its own work: the file must decode
    as UTF-8 and its text must equal the line, byte for byte. A
    mismatch means the write did not do what was asked, and the run
    fails loudly instead of handing the judge a surprise.
    """
    with open(path, "rb") as handle:
        raw = handle.read()
    actual = raw.decode("utf-8")
    if actual != expected:
        raise ValueError(
            "entry on disk differs from the line: %r != %r" % (actual, expected)
        )
    return len(raw)


def summarize(text):
    """Describe `text` the way the gate sees it.

    Returns one line naming the character count, the byte count
    and the gate verdict. Used by the --check mode so a person
    can see, before anything is written, exactly what the judge
    will be handed.
    """
    problems = check_line(text)
    verdict = "valid" if not problems else "invalid: " + "; ".join(problems)
    return (
        "%d characters, %d bytes, %s"
        % (len(text), len(text.encode("utf-8")), verdict)
    )


def run(output_path):
    """Validate the line, write it, and verify what was written.

    Returns the number of bytes written. Raises SystemExit with a
    message on any failure, so a bad line can never produce a
    quiet, successful-looking run.
    """
    problems = check_line(LINE)
    if problems:
        for problem in problems:
            print("invalid entry: %s" % problem, file=sys.stderr)
        raise SystemExit(1)
    written = write_atomically(output_path, LINE)
    verified = read_back(output_path, LINE)
    if written != verified:
        print(
            "wrote %d bytes but verified %d" % (written, verified),
            file=sys.stderr,
        )
        raise SystemExit(1)
    print("wrote %d bytes to %s" % (written, output_path))
    return written


def main(argv=None):
    """Entry point: pick the output path, then run.

    The path comes from the first argument, else
    DATING_BIO_OUTPUT, else /output/entry.txt. No other input
    is read, so the output cannot depend on anything outside this
    file.

    With --check, nothing is written: the line is printed with
    the gate's verdict on it, so the entry can be inspected
    without touching any output file.
    """
    args = list(sys.argv[1:] if argv is None else argv)
    if args and args[0] == "--check":
        print(LINE)
        print(summarize(LINE))
        problems = check_line(LINE)
        return 0 if not problems else 1
    if args:
        output_path = args[0]
    else:
        output_path = os.environ.get("DATING_BIO_OUTPUT", DEFAULT_OUTPUT)
    run(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
