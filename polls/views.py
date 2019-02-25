from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse    # To use HTTP protocols 
from .models import Question
from django.template import loader
from django.shortcuts import get_object_or_404
from .models import Choice
from django.http import HttpResponseRedirect
from django.urls import reverse
# To make views generic
from django.views import generic

from django.utils import timezone
# Create your views here.
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    # def get_queryset(self):
    #     """ Return last 5 questions """
    #     return Question.objects.order_by('-pub_date')[:5]
    def get_queryset(self):
        """
        Return the last 5 published questions(not including those set to be published in future date)
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    # template_name = 'polls/detail.html'
    # context_object_name = 'question'
    # def get_queryset(self):
    #     """ Return the question details """
    model = Question
    template_name = "polls/detail.html"
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsVeiw(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def votes(request, question_id):
    # return HttpResponse("You are voting on question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError,Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html',{
            'question':question,
            'error_message': "You didn't select a choice.",
        })
    else:
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))

# Commenting code as we are goning to make lot more changes to the views to make them generic
'''
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list' : latest_question_list,
    }
    return HttpResponse(template.render(context,request))
    # context = {'latest_question_list': latest_question_list}
    # return render(request,'polls/index.html', context)


def detail(request,question_id):
    # response =  "You are looking at the response of question %s."
    # return HttpResponse("You are looking at the response of question %s." % question_id)

    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, 'polls/detail.html',{'question': question})

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html',{'question': question})


def results(request, question_id):
    # response = "You are looking at the results of question %s."
    # return HttpResponse(response % question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question' : question})

def votes(request, question_id):
    # return HttpResponse("You are voting on question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError,Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html',{
            'question':question,
            'error_message': "You didn't select a choice.",
        })
    else:
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
'''
