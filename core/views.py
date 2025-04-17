from django.shortcuts import render

from students.models import Testimonial

# Create your views here.


def home_view(request, *args, **kwargs):
    testimonials = Testimonial.objects.all()
    context = {"testimonials": testimonials}
    return render(request, 'core/home.html', context)
