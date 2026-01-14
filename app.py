from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def kinno():

    ROOMS = [
    {"id": 1, "code": "CR-101", "capacity": 45, "type": "classroom", "status": "active"},
    {"id": 2, "code": "CR-102", "capacity": 50, "type": "classroom", "status": "active"},
    {"id": 3, "code": "LAB-01", "capacity": 40, "type": "lab", "status": "active"},
    {"id": 4, "code": "HALL-A", "capacity": 120, "type": "hall", "status": "active"},
    ]

    room_lookup = {room["id"]: room for room in ROOMS}


    PERIODS = [
    {"id": 1, "label": "1", "start": "08:00", "end": "08:50", "type": "lesson"},
    {"id": 2, "label": "2", "start": "08:50", "end": "09:40", "type": "lesson"},
    {"id": 0, "label": "BREAK", "start": "09:40", "end": "10:00", "type": "break"},
    {"id": 3, "label": "3", "start": "10:00", "end": "10:50", "type": "lesson"},
    {"id": 4, "label": "4", "start": "10:50", "end": "11:40", "type": "lesson"},
    {"id": 0, "label": "LUNCH", "start": "11:40", "end": "12:40", "type": "lunch"},]

    period_lookup = {p["id"]: p for p in PERIODS}


    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    timetable = [
      {
           "type": "lesson",
           "period_id": 1,
           "cells": [
        {"subject": "Cyber Security", "teacher": "Mr. Nkurunziza", "room_id":1},
        {"subject": "Python Programming", "teacher": "Ms. Uwimana", "room_id":2},
        {"subject": "Cloud Computing", "teacher": "Mr. Habimana", "room_id":3},
        {"subject": "Linux Server", "teacher": "Mr. Mugenzi", "room_id":4},
        {"subject": "Cyber Security", "teacher": "Mr. Nkurunziza", "room_id": 1},
    ]
        },

        {
            "type": "break",
            "label": "BREAK",
            "period_id": 0
        },

        { "type":"lesson",
          "period_id": 2,
           "cells":[{"subject": "Mathematics", "teacher": "Ms. Mukamana"},
            {"subject": "Mathematics", "teacher": "Ms. Mukamana"},
            {"subject": "Python Programming", "teacher": "Ms. Uwimana"},
            {"subject": "Free Time", "teacher": ""},
            {"subject": "Professional Ethics", "teacher": "Mr. Kayitesi"}]
        },

        {
            "type":"lunch",
            "label":"LUNCH",
            "period_id": 0
        }
    ]
    
    for row in timetable:
      if row.get("type") == "lesson":
        for cell in row["cells"]:
            room_id = cell.get("room_id")
            room = room_lookup.get(room_id) if room_id else None

            cell["room_code"] = room["code"] if room else "N/A"

    for row in timetable:
      period = period_lookup.get(row["period_id"])
      if period:
        row["period_label"] = period["label"]
        row["start"] = period["start"]
        row["end"] = period["end"]
        

    return render_template(
        "index.html",
        days=days,
        timetable=timetable
    )
if __name__ == '__main__':
    app.run(debug=True)