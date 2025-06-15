
from flask import Flask, render_template, request

app = Flask(__name__)

# === Study notes, past papers, and media resources ===

study_notes = {
    "Maths": {
        "Algebra": {
            "notes": "Simplifying expressions and solving equations, e.g., 2x + 3 = 7.",
            "papers": "https://www.testpapers.co.za/gr10-mathematics",
            "video": "https://www.youtube.com/embed/VlSGABOBHew"
        },
        "Trigonometry": {
            "notes": "Understand ratios in right-angled triangles (sin, cos, tan).",
            "papers": "https://www.testpapers.co.za/gr10-mathematics",
            "video": "https://www.youtube.com/embed/KPU7ugbYKp0"
        }
    },
    "Afrikaans": {
        "Taalstrukture": {
            "notes": "Parts of speech, sentence construction, and punctuation rules.",
            "papers": "https://www.sapapers.co.za/grade-10/afrikaans-fal",
            "video": "https://www.youtube.com/embed/ulvtNoSZ5-M"
        }
    },
"Life Orientation": {
    "Self-awareness and Self-esteem": {
        "notes": "Factors influencing self-awareness; strategies to build self-esteem.",
        "papers": "https://www.testpapers.co.za/gr-10/life-orientation",
        "video": "https://www.youtube.com/embed/Dc-VOPaVnQA"
    },
    "Democracy and Human Rights": {
        "notes": "Human rights, responsibilities, and combating discrimination.",
        "papers": "https://www.sapapers.co.za/grade-10/life-orientation",
        "video": "https://www.youtube.com/embed/X0wV7ghSW6o"
    },
    "Physical Education": {
        "notes": "Importance of exercise, safety measures, and fitness activities.",
        "papers": "https://www.education.gov.za/Curriculum/NationalSeniorCertificate%28NSC%29Examinations/Grade10Exams.aspx",
        "video": "https://www.youtube.com/embed/cxf7pTFgluo"
    }
}
}
@app.route('/', methods=["GET", "POST"])
def home():
    son_name ="Victor"

    subject = None
    topic = None
    note = None
    paper_link = None
    video = None

    if request.method == 'POST':
        subject = request.form.get('subject', '').strip()
        topic = request.form.get('topic', '').strip()

        topic_data = study_notes.get(subject, {}).get(topic)
        if topic_data:
            note = topic_data.get('notes')
            paper_link = topic_data.get('papers')
            video = topic_data.get('video')

    return render_template('home.html',
                           son_name=son_name,
                           subject=subject,
                           topic=topic,
                           note=note,
                           paper_link=paper_link,
                           video=video,
                           study_notes=study_notes)


if __name__ == '__main__':
    app.run(debug=True)
