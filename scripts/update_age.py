from datetime import date
import re
from pathlib import Path

BIRTHDAY = date(1999, 12, 10)
README = Path(__file__).resolve().parent.parent / "README.md"


def calculate_age(birthday: date, today: date = date.today()) -> int:
    return today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))


def main() -> None:
    text = README.read_text(encoding="utf-8")
    new_age = str(calculate_age(BIRTHDAY))
    updated = re.sub(
        r"(<!-- BEGIN_AGE -->).*?(<!-- END_AGE -->)",
        rf"\g<1>{new_age}\g<2>",
        text,
        flags=re.S,
    )
    if updated != text:
        README.write_text(updated, encoding="utf-8")
        print(f"idade atualizada para {new_age}")
    else:
        print("nada a mudar")


if __name__ == "__main__":
    main()
