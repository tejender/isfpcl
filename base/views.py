from django.shortcuts import render

# Create your views here.
def Home(request):
    storage_service ={
        '1':{
            'name':'Cold Storage Large',
            'features':[                                
                'Temperature-controlled storage',
                'Versatile storage options',
                'Flexible rental options',
                'Affordable rates',
            ],
            'img_url':'https://apal.org.au/wp-content/uploads/2019/08/Apples-in-cold-storage-DSC_9302-web.jpg',
            },
            '2':{
            'name':'Cold Storage Medium',
            'features':[                                
                'Temperature-controlled storage',
                'Versatile storage options',
                'Flexible rental options',
                'Affordable rates',
            ],
            'img_url':'https://5.imimg.com/data5/IQ/SV/IC/SELLER-485160/apple-degreening-cold-storage-room-1000x1000.JPG',
            }
        }
    

    rental_service ={
        '1':{
            'name':'Power Sprayer',
            'img_url':'https://m.media-amazon.com/images/I/81WMYDCU30L._SL1500_.jpg',
        },
        '2':{
            'name':'Power Tiller',
            'img_url':'https://www.vsttractors.com/sites/default/files/styles/product_listing/public/2021-12/95_listing.png?itok=ZsVTKF06',
        },
        '3':{
            'name':'Power Chain Saw',
            'img_url':'https://5.imimg.com/data5/KZ/LT/UW/IOS-4151186/product-jpeg-500x500.png',
        },
        '4':{
            'name':'Grass Cutter',
            'img_url':'https://m.media-amazon.com/images/I/51gx2huRGZL._SL1107_.jpg',
        },
        '5':{
            'name':'Power Sprayer',
            'img_url':'https://m.media-amazon.com/images/I/61PfySaqLzL._SL1500_.jpg',
        },
        
    }
    
    context = {'storage_service':storage_service,'rental_service':rental_service}
    
    return render(request, 'base/home.html',context)


def Contact(request):
    return render(request, 'base/contact.html')

def About(request):
    return render(request, 'base/about.html')