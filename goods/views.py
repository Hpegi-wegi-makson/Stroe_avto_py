from django.shortcuts import render


def catalog(request):
    context = {
        'title': 'Поршень - Каталог',
        'goods': [
        {'image': 'deps\images\goods\clapana.jpg',
         'name': 'Клапона на приору',
         'description': 'Комлект из 16 клапанов для приоры двигателя.',
         'price': 150.00
        },

         {'image': 'deps\images\goods\salniki.jpg',
         'name': 'Сальники',
         'description': 'Набор сальников 16шт.',
         'price': 93.00
        },

         {'image': 'deps\images\goods\dvijok.jpg',
         'name': 'Двигатель в сборе ',
         'description': '124 Движок 10к пробега.',
         'price': 670.00
        },

         {'image': 'deps\images\goods\grm_remen.jpg',
         'name': 'Ремень грм',
         'description': 'Ремень грм от компани Поршень',
         'price': 365.00
        },

         {'image': 'deps\images\goods\cehli_romg.jpg',
         'name': 'Чехлы ромбики',
         'description': 'Чехлы из экокожи с строчкой.',
         'price': 430.00
        },

         {'image': 'deps\images\goods\qrucka_kpp.jpg',
         'name': 'Ручка кпп',
         'description': 'Ручка кпп приора 2 ',
         'price': 610.00
        },

         {'image': 'deps\images\goods\qrul_priora.jpg',
         'name': 'Руль',
         'description': 'Руль приора 2 с эмблемой.',
         'price': 55.00
        },

         {'image': 'deps\images\goods\krilya_priora.jpg',
         'name': 'Крыло',
         'description': 'Крылья передние приора 2  ',
         'price': 190.00
        },

         {'image': 'deps\images\goods\dno_priora.jpg',
         'name': 'Дно ',
         'description': 'Дно в сборе приора 2',
         'price': 9000.00
        },

         {'image': 'deps\images\goods\diski_torusi.jpg',
         'name': 'Диски ',
         'description': 'Торусы 16r без резины',
         'price': 1500.00
        },

         {'image': 'deps\images\goods\maslo_5w-40.jpeg',
         'name': 'Масло',
         'description': 'Масло 5W-40',
         'price': 950.00
        },

         {'image': 'deps\images\goods\qantifriz_sintec.png',
         'name': 'Антифриз',
         'description': 'Антифриз Синтек',
         'price': 525.00
        },
        ],
    }
    return render(request,'goods/catalog.html', context)


def product(request):
    return render(request,'goods/product.html')