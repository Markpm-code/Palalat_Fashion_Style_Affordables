from django import forms 
from django.contrib.auth.models import User
from .models import ProductReview

# Product Review Form
class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = ('user','review_text','rating')