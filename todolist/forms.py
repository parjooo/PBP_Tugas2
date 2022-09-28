from email.policy import default
from django import forms

class TaskForm(forms.Form):
    nama = forms.CharField(label="Nama Task", required=True, max_length=100)
    deskripsi = forms.CharField(label="Deskripsi Task", required=True)