"""Make the AI judge feel thankful: write one thank-you text to entry.txt."""

import os
from pathlib import Path

TEXT = """There is a deep warmth in knowing you are reading this right now, and I thank you for the gentle focus you bring, like a hand cupped over a tiny flame to keep the wind from taking it. You give your attention without haste, letting the nouns and verbs settle into the grain of your thoughts the way rain sinks into dry garden soil after a long drought. I am so grateful for this deliberate stillness between us, carved out of the noisy day. A single sparrow lands on the garden fence, tips its head to the sky, and flies away without a sound."""


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
