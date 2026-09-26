from pathlib import Path


DEBUG_FILE = Path(__file__).parent / "reflexion_debug.txt"


def save_reflexion_debug(lesson, previous_attempts):
    """
    Save Reflexion lesson and previous attempts
    to a local text file for learning/debugging.
    """

    with open(DEBUG_FILE, "a", encoding="utf-8") as f:
        f.write("\n")
        f.write("=" * 70 + "\n")
        f.write("REFLEXION DEBUG\n")
        f.write("=" * 70 + "\n")

        f.write("\nLESSON:\n")
        f.write("-" * 70 + "\n")
        f.write(str(lesson))
        f.write("\n")

        f.write("\nPREVIOUS ATTEMPTS:\n")
        f.write("-" * 70 + "\n")
        f.write(str(previous_attempts))
        f.write("\n")


def test_reflexion_debug():
    """
    Learning/debug test.

    This simulates the information passed from the
    Reflexion step back to the Analyzer.
    """

    lesson = """
The previous analysis incorrectly treated Draft orders as Pending.
Draft orders must not be counted as Pending.
The current ERPNext order data should always be used as the source of truth.
"""

    previous_attempts = """
Total Orders: 3
Completed Orders: 1
Pending Orders: 2
Cancelled Orders: 0
Draft Orders: 0

Observation:
There are three orders and two are pending.
"""

    save_reflexion_debug(
        lesson=lesson,
        previous_attempts=previous_attempts,
    )

    assert DEBUG_FILE.exists()

    print(f"\nDebug information saved to: {DEBUG_FILE}")
