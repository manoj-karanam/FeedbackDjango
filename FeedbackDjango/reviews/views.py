from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView

from .forms import ReviewForm
from .models import Review


# Create your views here.

class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        return render(request, "reviews/reviews.html",{
        "form":form})
    def post(self, request):
        form = ReviewForm(request.POST) 
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("thank-you")
        return render(request, "reviews/reviews.html",{
        "form":form})
    

# def review(request):
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)

#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("thank-you")

#     else:
#         form = ReviewForm()

#     return render(request, "reviews/reviews.html",{
#         "form":form
#     })


# def thank_you(request):
#     return render(request, "reviews/thank_you.html")

class ThankYouView(TemplateView):
    template_name="reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["message"] = "This Works!"
        return context
    
class ReviewListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"
    
    
class SingleReviewView(TemplateView):
    template_name = "reviews/single_review.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        review_id = kwargs["id"]
        context['review']= Review.objects.get(pk=review_id)
        return context
 