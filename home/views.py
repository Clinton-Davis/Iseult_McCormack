
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import reverse, render
from django.views import generic
from django.views.generic import TemplateView
from .forms import ContactForm
from shop.models import Product
from shop.models import Category


def IndexView(request):
    feat_item = Product.objects.filter(feat_item=True)
    category = Category.objects.all()
    context = {
        'feat_item' : feat_item,
        'category': category
    }
    return render(request, "index.html", context)


class AboutView(TemplateView):
    template_name = "about.html"


class TermsView(TemplateView):
    template_name = "terms.html"


class PrivacyView(TemplateView):
    template_name = "privacy.html"


class ContactView(generic.FormView):
    form_class = ContactForm
    template_name = "contact.html"

    def get_success_url(self):
        return reverse("contact")

    def form_valid(self, form):
        """"Getting clean data from the form and creating
        a message to get sent to default email."""
        messages.success(self.request,
                         "Thank you for getting in touch with us. We have received your message.")
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        message = form.cleaned_data.get('message')

        full_message = f"""
        Received message below from {name}, {email}
        ___________________________
        {message}

        """
        send_mail(
            subject="Message from Focus contact form",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.NOTIFY_EMAIL]
        )
        return super(ContactView, self).form_invalid(form)
