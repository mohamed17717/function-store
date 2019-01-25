from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse

from .models import Function, Tag
from .forms import FunctionForm

# Create your views here.

def show_functions(request, functions, context={}):
    context.update({'functions': functions})
    return render(request, 'functions.html', context) 

def Home(request):
    ## show all fucntions
    ## in other cases last 20
    functions = Function.objects.all()
    return show_functions(request, functions)



def ShowFunction(request, slug):
    # functions = get_object(Function, slug= slug)
    functions = Function.objects.all().filter(slug= slug)
    context = {'functions': functions}
    return render(request, 'function.html', context) 

def AddFunction(request):
    if request.method == 'POST':
        form = FunctionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('functions:home')

        else:
            return redirect('functions:add_function')

    else:
        form = FunctionForm
        context = {'form': form, 'btn': 'Add'}
        return render(request, 'addfunction_form.html', context)

def get_object(Class, **kwargs):
    try:
        return Class.objects.get(**kwargs)
    except ObjectDoesNotExist:
        return None

def EditFunction(request, slug):
    function = get_object(Function, slug= slug)
    if function:
        if request.method == 'POST':
            form = FunctionForm(request.POST, instance=function)
            if form.is_valid():
                form.save()
                return redirect('functions:home')

            else:
                return redirect('functions:edit_function')

        else:
            form = FunctionForm(instance=function)
            context = {'form': form, 'btn': 'Update', 'slug': slug}
            return render(request, 'addfunction_form.html', context)

    else:
        return HttpResponse('Function Not Found')

def AllFunction_Tag(request, tag):
    ## get data row data from the Tag table
    ## get the clm functions (many to many)
    # then retrieve all the data
    # 
    # i use the lines of home() cuz there are very same
    # the differnce only the functions which sent  
    functions = get_object(Tag, name= tag).functions.all()
    return show_functions(request, functions)

def redirect_prev_page(request):
    previous_path = '/'+ '/'.join(request.META.get('HTTP_REFERER').split('/')[3:])
    return redirect(previous_path)

def RemoveFunction_Tag(request, slug, tag):
    ## i will edit in 2 tables
    ## get the rows
    function    = get_object(Function, slug=slug)
    removed_tag = get_object(Tag, name=tag)

    ## edit the rows to new vals
    new_tags = function.tags.split(' ')
    new_tags.remove(tag)
    new_tags = ' '.join(new_tags) or 'empty_tags'

    function.tags = new_tags
    removed_tag.functions.remove(function)

    ## save the rows
    function.save()
    removed_tag.save()

    return redirect_prev_page(request)
    
def unique(iterable):
    vals = ()
    count = []
    for item in iterable:
        ## exist in list
        try:
            index = vals.index(item)
            count[index] += 1
        ## not exist in list
        except ValueError:
            vals  += (item,)
            count += (1,)
    return vals , count

def TagSearch(request):
    if request.method == 'POST':
        query = request.POST.get('q')
        if query:
            q_tags = query.split(' ')
            functions = ()

            ## get all functions in each tag
            for tag in q_tags:
                tag = get_object(Tag, name= tag)
                if tag:
                    functions += tuple(tag.functions.all())

            ## unique functions and get number of repeatation for each
            functions, counts = unique(functions)

            ## sort them accroding to count number
            functions = tuple([function for _, function in sorted(zip(counts, functions), key= lambda elm: elm[0], reverse=True)])
            
            return show_functions(  request, functions, context={'query_value': request.POST['q']}  )
        
        return HttpResponse('this is wrong query')

    return redirect('functions:home')

def contact(request):
    return render(request, 'contact.html', {})