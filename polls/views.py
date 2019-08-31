from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from django.views import generic

from scales1 import scales
from .models import Choice, Question, Fretboard

#scale = 'F'
#tunings = ['E', 'A', 'D', 'G', 'B', 'E']


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def SelectBoard(request):
    #model = Fretboard
    return render(request, 'polls/select_board.html')

def GenBoard(request):
    fretboard = request.POST

    print(fretboard)

    tunings = []

    scale= fretboard['scale']

    tunings.append(fretboard['string1'])
    tunings.append(fretboard['string2'])
    tunings.append(fretboard['string3'])
    tunings.append(fretboard['string4'])
    tunings.append(fretboard['string5'])
    tunings.append(fretboard['string6'])

    scales.gen_board(scale, tunings)

    return HttpResponseRedirect(reverse('polls:select'))

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        scales.gen_board(scale, tunings)
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))