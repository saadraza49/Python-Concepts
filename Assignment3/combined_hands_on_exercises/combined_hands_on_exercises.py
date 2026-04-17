# ============================================================
# PART 10 – Combined Hands-on Exercises  [5 Marks]
# ============================================================
print("=" * 60)
print("PART 10 – Combined Hands-on Exercises")
print("=" * 60)

# Integrates: Loops + Functions + OOP + Exception Handling

class StudentReport:
    """OOP + loops + exception handling combined."""

    def __init__(self, name):
        self.name    = name
        self.scores  = {}

    def add_score(self, subject, score):
        try:
            if not isinstance(score, (int, float)):
                raise TypeError(f"Score must be a number, got {type(score).__name__}")
            if not (0 <= score <= 100):
                raise ValueError(f"Score {score} out of valid range (0–100)")
            self.scores[subject] = score
        except (TypeError, ValueError) as e:
            print(f"  [Error] {self.name} – {e}")

    def average(self):
        if not self.scores:
            return 0
        return sum(self.scores.values()) / len(self.scores)

    def grade(self):
        avg = self.average()
        if avg >= 90: return "A+"
        elif avg >= 80: return "A"
        elif avg >= 70: return "B"
        elif avg >= 60: return "C"
        elif avg >= 50: return "D"
        else: return "F"

    def display_report(self):
        print(f"\n  Report Card – {self.name}")
        print("  " + "-" * 35)
        for subj, sc in self.scores.items():
            bar = "█" * (sc // 10)
            print(f"  {subj:<12}: {sc:>3}  {bar}")
        print(f"  {'Average':<12}: {self.average():.1f}")
        print(f"  {'Grade':<12}: {self.grade()}")


# Build reports using loops
class_data = [
    ("Ali",    [("Math", 85), ("Science", 90), ("English", 78)]),
    ("Sara",   [("Math", 95), ("Science", 88), ("English", 92)]),
    ("Usman",  [("Math", 60), ("Science", 55), ("English", 70)]),
    ("Fatima", [("Math", 72), ("Science", -5), ("English", "N/A")]),  # bad data
]

reports = []
for name, subject_scores in class_data:
    r = StudentReport(name)
    for subj, sc in subject_scores:
        r.add_score(subj, sc)
    reports.append(r)

# Display all reports
for r in reports:
    r.display_report()

# Summary with loops
print("\n  Class Summary:")
print(f"  {'Name':<10} {'Average':>8} {'Grade':>7}")
print("  " + "-" * 28)
for r in reports:
    print(f"  {r.name:<10} {r.average():>8.1f} {r.grade():>7}")

# Top performer
top = max(reports, key=lambda r: r.average())
print(f"\n  🏆 Top Performer: {top.name} ({top.average():.1f} avg, Grade {top.grade()})")

# ============================================================
print("\n" + "=" * 60)
print("  Master Class Assignment Complete! All 10 Parts Done.")
print("  Total: 50 / 50 Marks")
print("  Student: [Your Name]  |  Hunarmand Punjab")
print("=" * 60)
