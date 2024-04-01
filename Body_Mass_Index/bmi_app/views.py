from django.shortcuts import render

# Create your views here.
def calculate_bmi(request):
    if request.method == 'POST':
        height = float(request.POST['height'])
        weight = float(request.POST['weight'])
        bmi = weight / (height ** 2)
        category = ''
        if bmi < 18.5:
            category = 'Under Weight'
        elif 18.5 < bmi < 25:
            category = 'Normal Weight'
        elif 25 < bmi < 30:
            category = 'Over Weight'
        else :
            category = 'Obessity'
        context = {'bmi': round(bmi, 2), 'category': category}
        return render(request, 'outcome.html', context)
    return render(request, 'calculate.html')