

import os, django, random
import pandas as pd

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MyRestaurant.settings")

django.setup()

from faker import Faker
from Restaurant.models import Customer
from django.contrib.auth.models import User
#import pandas as pd

#d1=range(2012-05-25, 2012-06-27)
d1 = pd.date_range(start='2018-08-08', end = '2018-08-15', freq='H')


def create_customer(N):
    fake = Faker()
    for _ in range(10):

        name = fake.name()

        Customer.objects.create(name=name + "   How are You!!!!!!",
                           # author=User.objects.get(id=id),
                          #  slug="-".join(title.lower().split()),

                            address=fake.address(),
                            intime=random.choice(d1),
                            outtime=random.choice(d1),
                            )

       # address = fake.address(),
        #intime = timezone.now(),
        #outthime = timezone.timedelta(),

        # id = random.randint(1, 4)
        # status = random.choice(['Higher Class', 'Middle Class'])
       # Customer.objects.create(title=title + "Post!!!",
       # author = User.objects.get(id=id),
       # slug = "-" .join(title.lower().split()),




create_customer(10)
print("DATA IS POPULATED SUCCESSFULLY!!!")