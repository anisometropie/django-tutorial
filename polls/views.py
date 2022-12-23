from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone

from .models import Question, Choice

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list
#     }
#     return HttpResponse(template.render(context, request))

# ————> we can simplify this into

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
    
# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#         context = {
#             'question': question
#         }
#     except:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', context)

# ————> we can simplify this into

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
            'question': question
        }
    return render(request, 'polls/detail.html', context)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def newPoll(request):
    return render(request, 'polls/newPoll.html')

def newPollSubmit(request):
    newQuestion = Question(
        question_text=request.POST['question_text'],
        pub_date=timezone.now()
        )
    newQuestion.save()
    for i in range(1,3):
        choiceName = f'choice{i}'
        if choiceName in request.POST:
            choice = Choice(
                question=newQuestion,
                choice_text=request.POST[choiceName],
            )
            choice.save()
    context={'question': newQuestion}
    return render(request, 'polls/detail.html', context)