
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import reverse, render
from django.views import generic
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from .forms import ContactForm
from shop.models import Product
from .models import About, Scarfs, Paintings, ImageGallery


def IndexView(request):
    feat_item = Product.objects.filter(feat_item=True)
    about = About.objects.all()
    scarfs = Scarfs.objects.all()
    paintings = Paintings.objects.all()
    context = {
        'feat_item' : feat_item,
        'about': about,
        'scarfs':scarfs,
        'paintings':paintings,
    }
    return render(request, "home/index.html", context)


class GalleryView(ListView):
     model = ImageGallery
     template_name = "home/gallery.html"
     context_object_name = "images"


class TermsView(TemplateView):
    template_name = "home/terms.html"


class PrivacyView(TemplateView):
    template_name = "home/privacy.html"


class ContactView(generic.FormView):
    form_class = ContactForm
    template_name = "home/contact.html"

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
