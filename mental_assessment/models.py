from django.db import models
from django.contrib.auth.models import User


class Assessment(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Stress & Anxiety (Q1-Q5)
    q1  = models.IntegerField(default=0)
    q2  = models.IntegerField(default=0)
    q3  = models.IntegerField(default=0)
    q4  = models.IntegerField(default=0)
    q5  = models.IntegerField(default=0)

    # Depression & Mood (Q6-Q10)
    q6  = models.IntegerField(default=0)
    q7  = models.IntegerField(default=0)
    q8  = models.IntegerField(default=0)
    q9  = models.IntegerField(default=0)
    q10 = models.IntegerField(default=0)

    # Sleep & Physical Health (Q11-Q14)
    q11 = models.IntegerField(default=0)
    q12 = models.IntegerField(default=0)
    q13 = models.IntegerField(default=0)
    q14 = models.IntegerField(default=0)

    # Social & Behavioral (Q15-Q17)
    q15 = models.IntegerField(default=0)
    q16 = models.IntegerField(default=0)
    q17 = models.IntegerField(default=0)

    # Focus & Productivity (Q18-Q20)
    q18 = models.IntegerField(default=0)
    q19 = models.IntegerField(default=0)
    q20 = models.IntegerField(default=0)

    score            = models.IntegerField(default=0)
    level            = models.CharField(max_length=20, default="Low")

    # Category scores
    stress_score     = models.IntegerField(default=0)
    depression_score = models.IntegerField(default=0)
    sleep_score      = models.IntegerField(default=0)
    social_score     = models.IntegerField(default=0)
    focus_score      = models.IntegerField(default=0)

    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.level} ({self.date.strftime('%d %b %Y')})"