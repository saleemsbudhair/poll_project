import django.db.models
from django.shortcuts import render, redirect

from .forms import CreatePollForm
from .models import Poll, PollOption, Vote


def home(request):
    most_recent_pools = Poll.objects.order_by('-date_created')
    top_3_polls = Poll.objects.annotate(votes_count=django.db.models.Count('votes')).order_by('-votes_count')[:3]
    vots = Poll.objects.annotate(votes_count=django.db.models.Count('votes')).order_by('-votes_count')[:3]
    context = {
        'polls': most_recent_pools,
        'top_3_polls': top_3_polls,
    }
    return render(request, 'poll/home.html', context)


def create(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            question = form.cleaned_data['question']
            poll = Poll.objects.create(question=question)
            option_1 = PollOption.objects.create(name=form.cleaned_data['option_1'], poll=poll)
            option_2 = PollOption.objects.create(name=form.cleaned_data['option_2'], poll=poll)
            if form.cleaned_data['option_3']:
                option_3 = PollOption.objects.create(name=form.cleaned_data['option_3'], poll=poll)
            if form.cleaned_data['option_4']:
                option_4 = PollOption.objects.create(name=form.cleaned_data['option_4'], poll=poll)
            return redirect('home')
        else:
            context = {
                'form': form,

            }
            return render(request, 'poll/create.html', context)
    else:
        form = CreatePollForm()
        context = {
            'form': form
        }

        return render(request, 'poll/create.html', context)


def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)

    if request.method == 'POST':
        selected_option = request.POST['poll']
        poll_option = PollOption.objects.get(pk=selected_option)
        Vote.objects.create(poll=poll, poll_option=poll_option)
        return redirect('results', poll.id)

    context = {
        'poll': poll
    }
    return render(request, 'poll/vote.html', context)


def results(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    context = {
        'poll': poll,
    }
    return render(request, 'poll/results.html', context)
