"""Load DUMMY sample students into the database (safe to run more than once).

Usage:  python seed.py

All names, emails and phone numbers below are fictional (example.com addresses and
reserved-style numbers). Never put real student data in this project.
"""

from datetime import date

from app import models  # noqa: F401
from app.database import Base, SessionLocal, engine
from app.models import Student

SAMPLE_STUDENTS = [
    ("Aarav Sharma", date(2004, 8, 15), "aarav.sharma@example.com", "+91 90000 00001", "Computer Science", "Mumbai, Maharashtra", date(2022, 7, 1)),
    ("Diya Patel", date(2005, 3, 22), "diya.patel@example.com", "+91 90000 00002", "Electronics", "Pune, Maharashtra", date(2023, 7, 1)),
    ("Rohan Mehta", date(2006, 1, 10), "rohan.mehta@example.com", None, "Computer Science", "Thane, Maharashtra", date(2024, 7, 1)),
    ("Ananya Iyer", date(2005, 11, 5), "ananya.iyer@example.com", "+91 90000 00004", "Mechanical", "Chennai, Tamil Nadu", date(2023, 7, 1)),
    ("Kabir Singh", date(2003, 6, 30), None, "+91 90000 00005", "Electronics", "Delhi", date(2021, 7, 1)),
    ("Meera Nair", date(2006, 9, 18), "meera.nair@example.com", "+91 90000 00006", "Computer Science", "Kochi, Kerala", date(2024, 7, 1)),
    ("Vihaan Gupta", date(2004, 12, 2), "vihaan.gupta@example.com", "+91 90000 00007", "Civil", "Jaipur, Rajasthan", date(2022, 7, 1)),
    ("Isha Reddy", date(2005, 7, 27), "isha.reddy@example.com", "+91 90000 00008", "Electronics", "Hyderabad, Telangana", date(2023, 7, 1)),
    ("Arjun Das", date(2002, 2, 14), "arjun.das@example.com", None, "Mechanical", "Kolkata, West Bengal", date(2020, 7, 1)),
    ("Saanvi Joshi", date(2006, 5, 9), "saanvi.joshi@example.com", "+91 90000 00010", "Computer Science", "Nashik, Maharashtra", date(2024, 7, 1)),
]


def main() -> None:
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    added = 0
    try:
        for name, dob, email, phone, course, address, enrolled in SAMPLE_STUDENTS:
            if email and db.query(Student).filter(Student.email == email).first():
                continue
            if not email and db.query(Student).filter(Student.name == name).first():
                continue
            db.add(
                Student(
                    name=name,
                    date_of_birth=dob,
                    email=email,
                    phone=phone,
                    course=course,
                    address=address,
                    enrollment_date=enrolled,
                )
            )
            added += 1
        db.commit()
    finally:
        db.close()
    print(f"Seeded {added} new dummy student(s).")


if __name__ == "__main__":
    main()
