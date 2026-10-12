from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from leave.models import Leave

# Create your views here.
@login_required
def apply_leave(request):
    if request.method == 'POST':
        leave_type = request.POST['leave_type']
        start=request.POST['start']
        end=request.POST['end']
        reason=request.POST['reason']
        Leave.objects.create(user=request.user,leave_type = leave_type,start_date=start,end_date=end,reason=reason,status='pending')
        return redirect('staff_dashboard')
    return render(request,'apply_leave.html')

@login_required
def my_leave(request):
    leaves=Leave.objects.filter(user=request.user)
    return render(request,'my_leave.html',{'leaves':leaves})

@login_required
def view_leave(request):
    if request.user.profile.role != 'admin':
        return redirect("staff_dashboard")
    leaves=Leave.objects.all()
    return render(request,'view_leaves.html',{'leaves':leaves})

@login_required
def approve_leave(request,id):
    if request.user.profile.role !='admin':
        return redirect("staff_dashboard")
    leave=get_object_or_404(Leave,id=id)
    leave.status='Approved' #Leave.objects.filter(id=id).update(status='approved')
    leave.save()
    return redirect('view_leave')

@login_required
def reject_leave(request,id):
    if request.user.profile.role !='admin':
        return redirect("staff_dashboard")
    leave=get_object_or_404(Leave,id=id)
    leave.status='Reject'
    leave.save()
    return redirect('view_leave')
