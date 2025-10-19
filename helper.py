from faker import Faker
faker = Faker()

def generate_registration_data():
    name = faker.name()
    email = faker.email()
    password = faker.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)
    return email, password, name # возвращаем кортеж
