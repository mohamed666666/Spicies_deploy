
import pandas as pd

from django.core.files.images import ImageFile
from store.models import Product,Category

from django.http.response import JsonResponse

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpRequest

def loadingdata(request):
    print("Clean old Products data")
    Product.objects.all().delete()
    path ="/home/mohamed/Codes/Web/Foodies/store/raw_data.csv"
        # Read the movie csv file as a dataframe
    productsdf = pd.read_csv(path)
        # Iterate each row in the dataframe

    for index, row in productsdf.iterrows():
            
            catname = row["categries"]
            try:
                cat=Category.objects.get(name=catname)
            except ObjectDoesNotExist:
                cat=Category(name=catname)
                cat.save()
            title = row["name"]
            describtion =str(row["descrption"])+str(row["name"])+str(row["ingridiance"])+str(row["weight"])+"g"
            

            try:
                imgtemp =ImageFile(open("media/images/"+str(row["id"])+".jpg", "rb")) 
            #img=ImageFieldFile(instance=None,field=Product.img.field,upload_to="images/",name='')
            except FileNotFoundError:
                imgtemp=ImageFile(open("media/images/"+str(0)+".jpg", "rb")) 
            price=float(row["price"])
            afterdisc=float(row["pricedesc"])
            w=row["weight"]
            # Populate Product object for each row
            product=Product(created_by=request.user ,
                 category=cat,
                            title=title,
                            describtion=describtion,
                            img=imgtemp,
                            price=price,
                            afterdiscont=afterdisc,
                            whight=w
            
            )
            # Save movie object
            
            product.save()
            print(f"product: {title}, {price} saved...")
    return  JsonResponse({'success': 'Return something'})

 


