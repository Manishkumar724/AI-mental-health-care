from django import forms

CHOICES = [
    (0, "Never"),
    (1, "Rarely"),
    (2, "Sometimes"),
    (3, "Often"),
]

class AssessmentForm(forms.Form):

    # --- Stress & Anxiety (Q1-Q5) ---
    q1  = forms.ChoiceField(label="I feel stressed or under pressure", choices=CHOICES, widget=forms.RadioSelect)
    q2  = forms.ChoiceField(label="I feel anxious or worried without a clear reason", choices=CHOICES, widget=forms.RadioSelect)
    q3  = forms.ChoiceField(label="I feel overwhelmed by my responsibilities", choices=CHOICES, widget=forms.RadioSelect)
    q4  = forms.ChoiceField(label="I struggle to relax even when I have free time", choices=CHOICES, widget=forms.RadioSelect)
    q5  = forms.ChoiceField(label="I experience physical symptoms of stress (e.g., headaches, tight chest)", choices=CHOICES, widget=forms.RadioSelect)

    # --- Depression & Mood (Q6-Q10) ---
    q6  = forms.ChoiceField(label="I feel sad or emotionally empty", choices=CHOICES, widget=forms.RadioSelect)
    q7  = forms.ChoiceField(label="I have lost interest in activities I used to enjoy", choices=CHOICES, widget=forms.RadioSelect)
    q8  = forms.ChoiceField(label="I feel hopeless about my future", choices=CHOICES, widget=forms.RadioSelect)
    q9  = forms.ChoiceField(label="I feel worthless or like a burden to others", choices=CHOICES, widget=forms.RadioSelect)
    q10 = forms.ChoiceField(label="I feel mentally exhausted even after rest", choices=CHOICES, widget=forms.RadioSelect)

    # --- Sleep & Physical Health (Q11-Q14) ---
    q11 = forms.ChoiceField(label="I have difficulty falling or staying asleep", choices=CHOICES, widget=forms.RadioSelect)
    q12 = forms.ChoiceField(label="I wake up feeling tired or unrefreshed", choices=CHOICES, widget=forms.RadioSelect)
    q13 = forms.ChoiceField(label="I experience changes in appetite (eating too much or too little)", choices=CHOICES, widget=forms.RadioSelect)
    q14 = forms.ChoiceField(label="I feel physically sluggish or low on energy throughout the day", choices=CHOICES, widget=forms.RadioSelect)

    # --- Social & Behavioral (Q15-Q17) ---
    q15 = forms.ChoiceField(label="I withdraw from friends, family or social activities", choices=CHOICES, widget=forms.RadioSelect)
    q16 = forms.ChoiceField(label="I feel irritable or easily frustrated with others", choices=CHOICES, widget=forms.RadioSelect)
    q17 = forms.ChoiceField(label="I rely on substances (e.g., alcohol, caffeine) to cope with my emotions", choices=CHOICES, widget=forms.RadioSelect)

    # --- Focus & Productivity (Q18-Q20) ---
    q18 = forms.ChoiceField(label="I have difficulty concentrating or making decisions", choices=CHOICES, widget=forms.RadioSelect)
    q19 = forms.ChoiceField(label="I procrastinate or struggle to complete tasks", choices=CHOICES, widget=forms.RadioSelect)
    q20 = forms.ChoiceField(label="I feel like my productivity and motivation have declined", choices=CHOICES, widget=forms.RadioSelect)