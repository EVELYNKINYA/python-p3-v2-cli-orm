from faker import Faker

fakegen = Faker()
#For testing purposes
def populate(N=5):
    for _ in range(N):
        #Create the fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        print(fake_url, fake_date, fake_name)

if __name__ == '__main__':
    print("populating script!")
    populate(20)
    print("populating complete!")