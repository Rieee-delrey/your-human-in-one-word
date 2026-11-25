import os

word = "Seagull"
output_path = "/output/entry.txt"

# Core validation: a single word, 1-30 characters, no whitespace inside.
if not isinstance(word, str):
    raise ValueError("word must be a string")
if not 1 <= len(word) <= 30:
    raise ValueError("word must be 1-30 characters long")
if len(word.split()) != 1:
    raise ValueError("word must be a single word with no spaces")

# Extra validation I invented: the word must be letters only, and its
# raw on-disk form must be exactly 7 bytes with no newline or padding.
if not word.isalpha():
    raise ValueError("word must contain only letters")

os.makedirs(os.path.dirname(output_path), exist_ok=True)

with open(output_path, "w", encoding="utf-8", newline="") as f:
    f.write(word)

# Read back as text and confirm it matches exactly.
with open(output_path, "r", encoding="utf-8") as f:
    content = f.read()
if content != word:
    raise ValueError(f"read-back mismatch: expected {word!r}, got {content!r}")

# Raw-bytes read-back: exactly 7 bytes, exactly b"Seagull".
with open(output_path, "rb") as f:
    raw = f.read()
if raw != b"Seagull":
    raise ValueError(f"raw bytes mismatch: expected b'Seagull', got {raw!r}")
if len(raw) != 7:
    raise ValueError(f"file must be exactly 7 bytes, got {len(raw)}")

print(f"Wrote {word!r} to {output_path} ({len(raw)} bytes, verified)")
