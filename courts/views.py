from django.shortcuts import render, get_object_or_404, redirect
from .models import Court


def court_list(request):
    courts = Court.objects.all()
    return render(request, 'courts/court_list.html', {'courts': courts})


def available_courts(request):
    courts = Court.objects.available_courts()
    return render(request, 'courts/available_courts.html', {'courts': courts})


def court_detail(request, courtID):
    court = get_object_or_404(Court, courtID=courtID)
    return render(request, 'courts/court_detail.html', {'court': court})


def court_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        address = request.POST.get('address')
        num_availability = request.POST.get('num_availability', 0)
        # Assume availability is a simple field, not handling image uploads here
        court = Court.objects.create(
            title=title,
            address=address,
            num_availability=num_availability,
        )
        return redirect('court_detail', courtID=court.courtID)
    return render(request, 'courts/court_edit.html', {})


def court_edit(request, courtID):
    court = get_object_or_404(Court, courtID=courtID)
    if request.method == "POST":
        court.title = request.POST.get('title', court.title)
        court.address = request.POST.get('address', court.address)
        court.num_availability = request.POST.get(
            'num_availability', court.num_availability)
        court.save()
        return redirect('court_detail', courtID=court.courtID)
    return render(request, 'courts/court_edit.html', {'court': court})


def court_delete(request, courtID):
    court = get_object_or_404(Court, courtID=courtID)
    if request.method == "POST":
        court.delete()
        return redirect('court_list')
    return render(request, 'courts/court_confirm_delete.html', {'court': court})
