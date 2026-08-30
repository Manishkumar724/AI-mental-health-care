from django.shortcuts import render, redirect
from .forms import AssessmentForm
from .models import Assessment
from django.contrib.auth.decorators import login_required


@login_required(login_url="/accounts/login/")
def assessment_view(request):

    if request.method == "POST":
        form = AssessmentForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data

            # Get all 20 answers
            answers = {f"q{i}": int(cd[f"q{i}"]) for i in range(1, 21)}

            # Category scores
            stress_score     = answers["q1"] + answers["q2"] + answers["q3"] + answers["q4"] + answers["q5"]
            depression_score = answers["q6"] + answers["q7"] + answers["q8"] + answers["q9"] + answers["q10"]
            sleep_score      = answers["q11"] + answers["q12"] + answers["q13"] + answers["q14"]
            social_score     = answers["q15"] + answers["q16"] + answers["q17"]
            focus_score      = answers["q18"] + answers["q19"] + answers["q20"]

            total_score = stress_score + depression_score + sleep_score + social_score + focus_score

            # Risk level  (max possible = 60)
            if total_score <= 15:
                level = "low"
                message = "Your mental health appears to be in a good place. Keep maintaining your healthy habits and routines."
                color   = "green"
            elif total_score <= 35:
                level = "moderate"
                message = "You are experiencing some mental health challenges. Consider incorporating more self-care and stress-relief practices."
                color   = "orange"
            else:
                level = "high"
                message = "Your responses suggest significant mental health strain. We strongly encourage you to speak with a mental health professional."
                color   = "red"

            # Category risk labels
            def cat_level(score, max_score):
                pct = score / max_score
                if pct <= 0.33:
                    return "Low"
                elif pct <= 0.66:
                    return "Moderate"
                return "High"

            categories = [
                {"name": "Stress & Anxiety",       "score": stress_score,     "max": 15, "level": cat_level(stress_score, 15),     "icon": "😰"},
                {"name": "Depression & Mood",       "score": depression_score, "max": 15, "level": cat_level(depression_score, 15), "icon": "😔"},
                {"name": "Sleep & Physical Health", "score": sleep_score,      "max": 12, "level": cat_level(sleep_score, 12),      "icon": "😴"},
                {"name": "Social & Behavioral",     "score": social_score,     "max": 9,  "level": cat_level(social_score, 9),      "icon": "👥"},
                {"name": "Focus & Productivity",    "score": focus_score,      "max": 9,  "level": cat_level(focus_score, 9),       "icon": "🎯"},
            ]

            # Tips based on highest category
            tips_map = {
                "Stress & Anxiety":       ["Try 5-minute deep breathing exercises daily", "Practice progressive muscle relaxation", "Write down your worries and challenge them"],
                "Depression & Mood":      ["Set one small achievable goal each day", "Spend time in nature or sunlight", "Reach out to a trusted friend or family member"],
                "Sleep & Physical Health":["Maintain a consistent sleep schedule", "Limit screen time 1 hour before bed", "Engage in light exercise like walking"],
                "Social & Behavioral":    ["Schedule regular check-ins with loved ones", "Join a group activity or hobby class", "Consider speaking to a counselor"],
                "Focus & Productivity":   ["Break tasks into smaller steps", "Use the Pomodoro technique (25-min focus sessions)", "Minimize distractions during work hours"],
            }

            # Find worst category
            worst = max(categories, key=lambda c: c["score"] / c["max"])
            tips = tips_map.get(worst["name"], [])

            Assessment.objects.create(
                user=request.user,
                **answers,
                score=total_score,
                level=level,
                stress_score=stress_score,
                depression_score=depression_score,
                sleep_score=sleep_score,
                social_score=social_score,
                focus_score=focus_score,
            )

            return render(request, "assessment_result.html", {
                "result":      level,
                "color":       color,
                "message":     message,
                "total_score": total_score,
                "max_score":   60,
                "categories":  categories,
                "tips":        tips,
                "worst":       worst["name"],
            })

    else:
        form = AssessmentForm()

    return render(request, "assessment.html", {"form": form})


@login_required(login_url="/accounts/login/")
def assessment_history(request):
    assessments = Assessment.objects.filter(user=request.user).order_by("-date")
    return render(request, "assessment_history.html", {"assessments": assessments})