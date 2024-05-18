# product
#! notlarını post-it'e sığacak kadar yap ve açıklayıcı olsun tek bir satırda tüm işleri yazma
# DONE: Tabi kullanıcı bilgisini de first_name, email, is_admin bilgileri olmali
# TODO: Email check edilsin
# TODO: product ismi olmalı, fiyatı olmalı, inidirim yapılabilmeli
# TODO: birden fazla türü olabilir ( dİGİTAL, FİZİKSEL
# TODO: Indirim bilgisini girebilecek kullanicinin is_admin bilgisinin olup olmadığına bakılmalı
# TODO: Bir ürüne en fazla bir kez indirim yapılsın
# TODO: Max discount bilgisi ürünlere en baştan eklensin, indirim uygularken geçememliyiz. 
# TODO: Stock bilgisi olsun, sıfırın altına düşemesin, stokta ürün var mı bakılsın
# TODO: min_stock bilgisi olsun, min_Stock bilgisine göre sipariş edilmesi gereken urunleri bilelim (ürünlerimin deposundaki sayıyı bilelim min stok 10sa ve bende 5 varsa uyarı vermeli. Telefon üretimindeki ekran sayısı gibi hammade için de geçerlidir.)
# TODO: ürün digital ise min_stock bilgisi ignore edilmeli
# TODO: discount percent mı net mi 
# TODO: Net_price bilgisine ihtiyacımız var

# TODO: Method ? is_dicount_applied, is_user_admin, is_min_stock, is_product_digital, apply_discount, check_max_discount, has_stock,

class User:
    # user.first_name = "Emre" diye bir atama yaptığımızda bu bilgiyi dir() ile görebiliriz. __dict__ ile de dict şeklinde gösterir. İlk oluştuğunda bilgi koymasam da ekleyebilirim. Ancak ben oluştuğunda bazı bilgilerin olmasını istiyorum.
    __password = "lorem" #! gizli bilgidir, __ ile yapılır, oluşturulurken gelmez, class içindedir

    # user: str = 111 dediğimde aslında kontrol yapmaz ama bazı paketler vardır, bunlara uygun olup olmadığını kontrol eder. Flake-8 kullanılabilir. Unit test gibidir.
    # google javascript style guide var, airbnb style guide var, bunu kullanmak istiyorum diyebiliyorsun.
    # ruff da bunların hızını göstermiş, ruff da böyle bir denetleyici, 

    def __init__(self, first_name, last_name, email, is_admin):
        if not User.is_email_correct(email): # not self.is_email_correct(email) yazarsak fonksiyona self, email yazılabilir ya da methoda email değil self verebiliriz. staticmethod dersek de çalışır, 
            raise ValueError("Email doğru değil...")
        self.first_name = first_name # self ile öğretilir, attribute olarak geçer
        self.last_name = last_name
        self._email = email # _ değiştirme lütfen demek için
        self.is_admin = is_admin

    def __str__(self):
        return f"{self.first_name} {self.last_name[0]} {self.is_admin}"

    def __repr__(self): # artık sadece user_1 dediğimde str olarak gelir.
        # return f"{self.first_name} {self.last_name[0]} {self.is_admin}"
        import json
        return json.dumps(self.__dict__) # ilk user yazdığımda da dict gelecek

    # her bir method instance için çalışacağından self bilgisi gerekebilir. 
    #objeye ait değildir, dışarda tutulabilecek bir fonksiyonu kendi içinde tutuyor. 
    @staticmethod #^ kullanıcıdan bağımsızdır. self demediğin sürece dışardan alır.
    def is_email_correct(email): # self bilgisinden bağımsız çalışabilir.
        import re
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        # easy-expressions ile daha okunabilir yazıyor.
        return re.fullmatch(regex, email)

class Product:
    PRODUCT_TYPES = ("DIGITAL", "NORMAL", )
    def __init__(self, user_info, name, price, product_type):
        if not product_type in self.PRODUCT_TYPES:
            raise ValueError("Product Tipi doğru değil...")
        if not isinstance(user_info, User):
            raise ValueError("User bilgisi dogru objeden üretilmedi")
        self.created_by = user_info #* user_1 yazılırsa buraya geliyor tüm bilgiler.
        self.name = name
        self.price = price
        self.product_type = product_type
        self.discount = None

        #* burada yer alacakların önce fieldlar, attributelar ve methodlar görsel çalışma yapılır ve nerede ne ekleyeceğimiz belli olur. Şeması olur. Methodlar yazılır pass ile yazılır, sonra içi doldurulur
    
    def set_discount(self, discount):
        if not self.created_by.is_admin :
            raise PermissionError ("Bu kullanici admin degil indirim uygulayamaz")
        self.discount = discount


user_1 = ()