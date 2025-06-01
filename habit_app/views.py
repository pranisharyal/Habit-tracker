from datetime import date, timedelta
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from habit_app.models import Habit

# Create your views here.
def habit_list(request):
    habits = Habit.objects.all()
    return render(
        request,
        "habit_list.html",
        {"habits": habits},
    )

def add_habit(request):
    print(request.method)
    if request.method == "GET":
        return render(request,"habit_create.html")
    else:
        Habit.objects.create(name=request.POST["name"])
    return HttpResponseRedirect("/")

def habit_delete(request,id):
    habit = Habit.objects.get(id=id)
    habit.delete()
    return HttpResponseRedirect("/")

def mark_done(request, id):
    habit = get_object_or_404(Habit, id=id)
    today = date.today()
    yesterday = today - timedelta(days=1)

    if habit.last_marked_date != today:
        if habit.last_marked_date == yesterday:
            habit.streak += 1
        else:
            habit.streak = 1  # Reset streak since yesterday wasn’t marked

        habit.last_marked_date = today
        habit.save()
    return HttpResponseRedirect("/")

def view_streak(request):
    today = date.today()
    yesterday = today - timedelta(days=1)

    habits = Habit.objects.all()

    # Optional: Update streaks if they’re broken
    for habit in habits:
        if habit.last_marked_date and habit.last_marked_date < yesterday:
            habit.streak = 0
            habit.save()

    return render(request, 'view_streak.html', {'habits': habits})


def edit_habit(request, id):
    habit = get_object_or_404(Habit, id=id)

    if request.method == "POST":
        habit.name = request.POST["name"]
        habit.save()
        return HttpResponseRedirect("/")
    
    return render(request, "habit_edit.html", {"habit": habit})

def view_charts(request):
    habits = Habit.objects.all()
    names = [habit.name for habit in habits]
    streaks = [habit.streak for habit in habits]

    return render(request, "habit_charts.html", {
        "names": names,
        "streaks": streaks
    })
