from django.shortcuts import render
from .models import Course
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CourseForm
from .forms import CourseDeleteForm
from .forms import CourseUpdateForm
# Courses Page View
def courses(request):
    courses = Course.objects.all()
    print(courses)
    return render(request, "courses/courses.html", {"courses": courses})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, "courses/course details.html", {"course": course})

# In your courses/views.py
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('courses')  # or wherever you want to redirect
    else:
        form = CourseForm()
    return render(request, 'courses/addcourses.html', {'form': form})
    
def update_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseUpdateForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_detail', course.id)
    else:
        form = CourseUpdateForm(instance=course)
    return render(request, 'courses/updatecourse.html', {'form': form, 'course': course})

def delete_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('courses')
    form = CourseDeleteForm(instance=course)
    return render(request, 'courses/coursedelete.html', {'form': form, 'course': course})