from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .forms import TicketForm


class CreateTicketView(LoginRequiredMixin, View):
    form_class = TicketForm
    template = 'ticket/create_ticket.html'

    def get(self, request):
        form = self.form_class()
        return render(
            request,
            self.template,
            context={
                'form': form
            }
        )

    def post(self, request):
        if request.method == 'POST':
            form = self.form_class(request.POST, request.FILES)
            if form.is_valid():
                ticket = form.save(commit=False)
                ticket.title = form.cleaned_data['title']
                ticket.description = form.cleaned_data['description']
                ticket.image = form.cleaned_data['image']
                ticket.user = request.user
                ticket.save()
                return redirect('flow')
            return render(
                request,
                self.template,
                context={
                    'form': form
                }
            )


class FlowView(LoginRequiredMixin, View):
    template = 'ticket/flow.html'

    def get(self, request):
        return render(
            request,
            template_name=self.template,
        )
