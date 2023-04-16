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



def Storage(request):
    storage_service ={
        '1':{
            'name':'Cold Storage Large',
            'details':{
                
                'capacity':{
                    'icon':'<i class="fa-solid fa-warehouse"></i>',
                    'value':'1000 Tons',
                },
                'pricing':{
                    'icon':'<i class="fa-solid fa-indian-rupee-sign"></i>',
                    'value':'1000'
                    },
                'location':{
                    'icon':'<i class="fa-solid fa-location-dot"></i>',
                    'value':'Kathmandu'
                },
                'temprature':{
                    'icon':'<i class="fa-solid fa-temperature-three-quarters"></i>',
                    'value':'Temprature Controlled'
                },
                'security':{
                    'icon':'<i class="fa-solid fa-lock"></i>',
                    'value':'security'
                },
                'accessibility':{
                    'icon':'<i class="fa-solid fa-eye"></i>',
                    'value':'24/7 accessibility'
                },  

            },
            
            'img_url':'https://apal.org.au/wp-content/uploads/2019/08/Apples-in-cold-storage-DSC_9302-web.jpg',
            },
            '2':{
            'name':'Cold Storage Medium',
            'details':{
               'capacity':{
                    'icon':'<i class="fa-solid fa-warehouse"></i>',
                    'value':'1000 Tons',
                },
                'pricing':{
                    'icon':'<i class="fa-solid fa-indian-rupee-sign"></i>',
                    'value':'1000'
                    },
                'location':{
                    'icon':'<i class="fa-solid fa-location-dot"></i>',
                    'value':'Kathmandu'
                },
                'temprature':{
                    'icon':'<i class="fa-solid fa-temperature-three-quarters"></i>',
                    'value':'Temprature Controlled'
                },
                'security':{
                    'icon':'<i class="fa-solid fa-lock"></i>',
                    'value':'security'
                },
                'accessibility':{
                    'icon':'<i class="fa-solid fa-eye"></i>',
                    'value':'24/7 accessibility'
                },  
 
            },
            
            'img_url':'https://5.imimg.com/data5/IQ/SV/IC/SELLER-485160/apple-degreening-cold-storage-room-1000x1000.JPG',
            }
        }
    service_features={                                
                'Temperature controlled storage':{
                    'description':' Our cold storage units are equipped with state-of-the-art temperature control systems, ensuring that your fruits stay fresh and healthy for longer periods of time.',
                },
                'Versatile storage options':{
                    'description':'We offer a range of storage options to meet your unique needs, from small-scale to large-scale storage. Our units can accommodate different types of fruits and are designed to keep them fresh and in optimal condition.',
                },
                'Flexible rental options':{
                    'description':'We understand that your storage needs may vary over time, which is why we offer flexible rental options. You can rent our units on a short-term or long-term basis, depending on your needs.',
                },
                'Affordable rates':{
                    'description':' Our rates are competitive and affordable, making our cold storage units accessible to a wide range of customers. We believe that everyone should have access to high-quality storage solutions, regardless of their budget.',
                },
            }
    context={'storage_service':storage_service,'service_features':service_features}
    
    return render(request, 'base/storage.html',context)

def Contact(request):
    return render(request, 'base/contact.html')

def About(request):
    return render(request, 'base/about.html')