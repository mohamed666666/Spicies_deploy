
import pandas as pd

from django.core.files.images import ImageFile
from store.models import Product,Category

from django.http.response import JsonResponse

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpRequest

def loadingdata(request):
    print("Clean old Products data")
    Product.objects.all().delete()
    path ="/home/mohamed/Codes/Web/deployment/Spicies_deploy/data.csv"
        # Read the movie csv file as a dataframe
    productsdf = pd.read_csv(path)
        # Iterate each row in the dataframe

    for index, row in productsdf.iterrows():
            
            catname = row["categries"]
            try:
                cat=Category.objects.get(name=catname)
            except ObjectDoesNotExist:
                cat=Category(name=catname,name_ar=row["categries_ar"])
                cat.save()
            title = row["name"]
            title_ar=row["name_ar"]
            describtion =str(row["name"])+" "+str(row["weight"])+"g"
            describtion_ar="g"+str(row["name_ar"])+" "+str(row["categries_ar"])+" "+str(row["weight"])

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
                            title_ar=title_ar,
                            describtion=describtion,
                            describtion_ar=describtion_ar,
                            img=imgtemp,
                            price=price,
                            afterdiscont=afterdisc,
                            whight=w
            
            )
            # Save movie object
            
            product.save()
            print(f"product: {title}, {price} saved...")
    return  JsonResponse({'success': 'Return something'})

 


