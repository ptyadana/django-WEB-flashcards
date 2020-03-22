from django.shortcuts import render
from random import randint

# Create your views here.
def home(request):
    """home page"""
    return render(request,'flashcard_app/home.html',{})

def addition(request):
    """addition page"""

    #generate two new random numbers for quizz
    new_num_1 = randint(0,9)
    new_num_2 = randint(0,9)

    #check the request method
    if request.method == 'POST':
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']

        #color scheme for bootstrap alert boxes
        alert_color = 'danger'

        try:
            answer = int(answer)
            old_num_1 = int(old_num_1)
            old_num_2 = int(old_num_2)
            
            correct_answer = old_num_1 + old_num_2

            #check the answer and display the result
            if answer == correct_answer:
                result = 'Correct! '
                msg = f'{old_num_1} + {old_num_2} = {correct_answer}'
                alert_color = 'success'

                return render(request,'flashcard_app/addition.html',{
                    'alert_color':alert_color,
                    'msg':msg,
                    'result':result,
                    'new_num_1':new_num_1,
                    'new_num_2':new_num_2
                    })
            else:
                result = 'Incorrect! '
                msg = f'{old_num_1} + {old_num_2} = {correct_answer}'
                alert_color = 'warning'

                return render(request,'flashcard_app/addition.html',{
                    'alert_color':alert_color,
                    'msg':msg,
                    'result':result,
                    'new_num_1':new_num_1,
                    'new_num_2':new_num_2
                    })
        except ValueError:
            msg = 'The answer is invalid. Please try again.'
            return render(request,'flashcard_app/addition.html',{
                'alert_color':alert_color,
                'msg':msg,
                'new_num_1':old_num_1,
                'new_num_2':old_num_2
                })

    return render(request,'flashcard_app/addition.html',{
        'new_num_1':new_num_1,
        'new_num_2':new_num_2,
    })   

def subtraction(request):
    """subtraction page"""

    #generate two new random numbers for quizz
    new_num_1 = randint(0,9)
    new_num_2 = randint(0,9)

    #check the request method
    if request.method == 'POST':
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']

        #color scheme for bootstrap alert boxes
        alert_color = 'danger'

        try:
            answer = int(answer)
            old_num_1 = int(old_num_1)
            old_num_2 = int(old_num_2)
            
            correct_answer = old_num_1 - old_num_2

            #check the answer and display the result
            if answer == correct_answer:
                result = 'Correct! '
                msg = f'{old_num_1} - {old_num_2} = {correct_answer}'
                alert_color = 'success'

                return render(request,'flashcard_app/subtraction.html',{
                    'alert_color':alert_color,
                    'msg':msg,
                    'result':result,
                    'new_num_1':new_num_1,
                    'new_num_2':new_num_2
                    })
            else:
                result = 'Incorrect! '
                msg = f'{old_num_1} - {old_num_2} = {correct_answer}'
                alert_color = 'warning'

                return render(request,'flashcard_app/subtraction.html',{
                    'alert_color':alert_color,
                    'msg':msg,
                    'result':result,
                    'new_num_1':new_num_1,
                    'new_num_2':new_num_2
                    })
        except ValueError:
            msg = 'The answer is invalid. Please try again.'
            return render(request,'flashcard_app/subtraction.html',{
                'alert_color':alert_color,
                'msg':msg,
                'new_num_1':old_num_1,
                'new_num_2':old_num_2
                })

    return render(request,'flashcard_app/subtraction.html',{
        'new_num_1':new_num_1,
        'new_num_2':new_num_2,
    })   

def multiplication(request):
    """multiplication page"""
    return render(request,'flashcard_app/multiplication.html',{})

def division(request):
    """division page"""
    return render(request,'flashcard_app/division.html',{})