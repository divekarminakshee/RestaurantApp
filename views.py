from django.shortcuts import render
from .models import Customer
import pandas as pd
from django.http import HttpResponseRedirect
from django.urls import resolvers
#from django.core.urlresolvers import reverse
# Create your views here.




def index(request):

    #template=loader.get_template('polls/index.html')

    return render(request, 'Restaurant/index.html')


def customer_list(request):
    customers = Customer.objects.all()
    context= {
        'customers': customers,
    }
    return render(request, 'restaurant/index.html',context)


#def YOUR_VIEW_DEF(request, pk):
 #   return render(request,'restaurant/deatils.html')
"""
def create_new_product(request):
    if request.method == 'POST':
        '''Execute the code here'''
    return render (request, 'Restaurant/base.html')
    
"""
#import mypythoncode
import numpy as np

###########################################################
#Method to calculate average of number of customers

def detail1(request):

    if request.method == 'POST':
        day=request.POST.get('handle')
    #reading csv file
    readfile = pd.read_csv("C:\\Users\\SAI\\PycharmProjects\\MyRestaurant\\User.csv")
    #groupby on column day
    user_grp = readfile.groupby(['day'])
    unique_date = user_grp.date.unique()
    Key_value = unique_date.index.values
    list_day = list(Key_value)
    total = user_grp.date.count()
    for i in range(6):
        if list_day[i] == day:
            no_of_users=int(total[i] / len(unique_date[i]))
            context={
                'day':day,

                'ans': no_of_users
            }
            print(total[i] / len(unique_date[i]))
    return render(request, 'Restaurant/New.html',context)

##################################################################################################
    # return render(request, 'Restaurant/detail.html')
    # day = request.POST.post('mytextbox')
    # mypythoncode.mypythonfunction( int(request.GET.get('mytextbox')) )


    #if(request.GET.get('mybtn')):


"""
def view_name(request):
    if request.method=="POST":
        screenname=request.POST.get("handle",None)

        return render(request,'Restaurant\index.htmll',{})
"""