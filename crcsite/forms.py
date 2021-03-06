from django.db import models
from django.forms import ModelForm
from django import forms
from crcsite.models import Question, Answer

Q12=(
	("1.7", "Yes"),
	("1", "No"),
	("1", "I don't know"),
)

Q13=(
	("1.3", "Yes"),
	("1", "No"),
	("1", "I don't know"),
)

Q21=(
	("1", "<2 drinks"),
	("1.2", "2-3 drinks"),
	("1.4", ">3 drinks"),
)

Q22=(
	("1.3", "Yes"),
	("1", "No"),
	("1", "I don't know"),
)

Q23=(
	("1", "<100g"),
	("1.2", ">=100g"),
	("1", "I don't know"),
)

Q24=(
	("1", "<50g"),
	("1.2", ">=50g"),
	("1", "I don't know"),
)

Q25=(
	("1.2", "Yes"),
	("1", "No"),
	("1", "I don't know"),
)

Q31=(
	("0.7", "Yes"),
	("1", "No"),
	("1", "I don't know"),
)

Q32=(
	("1", "<400g"),
	("0.8", ">=400g"),
	("1", "I don't know"),
)

Q33=(
	("1", "<200g"),
	("0.9", ">=200g"),
	("1", "I don't know"),
)


class CRC(forms.Form):
	q12=forms.ChoiceField(choices=Q12, widget=forms.RadioSelect(), initial="1")
	q13=forms.ChoiceField(choices=Q13, widget=forms.RadioSelect(), initial="1")
	q21=forms.ChoiceField(choices=Q21, widget=forms.RadioSelect(), initial="1")
	q22=forms.ChoiceField(choices=Q22, widget=forms.RadioSelect(), initial="1")
	q23=forms.ChoiceField(choices=Q23, widget=forms.RadioSelect(), initial="1")
	q24=forms.ChoiceField(choices=Q24, widget=forms.RadioSelect(), initial="1")
	q25=forms.ChoiceField(choices=Q25, widget=forms.RadioSelect(), initial="1")
	q31=forms.ChoiceField(choices=Q31, widget=forms.RadioSelect(), initial="1")
	q32=forms.ChoiceField(choices=Q32, widget=forms.RadioSelect(), initial="1")
	q33=forms.ChoiceField(choices=Q33, widget=forms.RadioSelect(), initial="1")

class QuestionForm(ModelForm):
    class Meta:
        model = Answer
        fields = ('Q_ID', 'A_text')
        widgets = {
            'A_text': forms.RadioSelect(),
        }

#	qone=forms.ChoiceField(choices=QONE, widget=forms.RadioSelect())




























