from django.shortcuts import render
from . import words
from .forms import GameForm


def index(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['the_letters'])
            the_game_letters = form.cleaned_data['the_letters']
            answer = words.solve(the_game_letters)
            print(answer)
        context = {
            'form': form,
            'answer': answer
        }
        return render(request, 'index.html', context)
    else:
        form = GameForm()

    return render(request, 'index.html', {'form': form})
