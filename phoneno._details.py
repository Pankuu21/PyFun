import phonenumbers
from phonenumbers import timezone,geocoder,carrier
if __name__=='__main__':
    while(True):
        number=input("Enter your number with +__" )
        phone=phonenumbers.parse(number)
        time=timezone.time_zones_for_number(phone)
        car=carrier.name_for_number(phone,"en")
        reg=geocoder.description_for_number(phone,"en")
        print(phone)
        print(time)
        print(car)
        print(reg)
        i=input("you want to continue? y/n")
        if i=="n":
            break
