from django.shortcuts import render, redirect, reverse
from .forms import *
from .models import *

def ticket_view(request):
    form = TicketForm()
    message_form  = TicketMessageForm()

 
    if request.method == 'POST':
        form = TicketForm(request.POST)
        message_form = TicketMessageForm(request.POST, request.FILES)

        if form.is_valid():
            ticket = Tickets.objects.create(
                user = request.user,
                title = form.data['title'],
                priority = form.data['priority'],
            )
            ticket.save()
            if message_form.is_valid():
                message = TicketMessage.objects.create(
                    ticket = ticket,
                    user = request.user,
                    message = message_form.data['message'],
                    file = form.data['file']
                )
                message.save()
                print('ddddddddd')
                return redirect(reverse('ticket:ticket'))
            else:
                print(message_form.errors)
        else:
            print(form.errors)
    return render(request, 'ticket.html', context={'form':form, 'message_form':message_form})



def ticket_detail(request, pk):
    form = TicketMessageForm()
    ticket = Tickets.objects.get(id=pk)
    ticket_message = TicketMessage.objects.filter(ticket=ticket)

    return render(request, 'ticket_detail.html', context={'ticket':ticket, 'ticket_message':ticket_message, 'form':form})




def ticket_message(request, id):
    form = TicketMessageForm(request.POST, request.FILES)
    ticket = Tickets.objects.get(id=id)
    if form.is_valid():
        print('sfdgfhgd')
        message = TicketMessage.objects.create(
            user = request.user,
            ticket = ticket,
            message = form.data['message'],
            file = form.data['file']
            
        )
        message.save()
        if request.user.is_superuser:
            ticket.status = '1'
        else:
            ticket.status = '3'
        ticket.save()
        
    else:
        print(form.errors)
    return redirect("ticket:ticket_detail", id)
    


def delete_ticket(request, id):
    ticket = Tickets.objects.get(id=id)
    ticket.delete()
    return redirect('accounts:profile_view')


