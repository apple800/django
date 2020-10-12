from django.shortcuts import render
from .models import Question

# Create your views here.
def index(request):
    """
    pybo 목록 출력
    """
    quesion_list = Question. objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'pybno/question_list.html', context)