from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)

    def validate(self):
        # Перевірка формату номера телефону (10 цифр)
        if len(self.value) != 10 or not self.value.isdigit():
            raise ValueError("Номер телефону повинен містити 10 цифр")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        new_phone = Phone(phone)
        new_phone.validate()
        self.phones.append(new_phone)

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        self.remove_phone(old_phone)
        self.add_phone(new_phone)

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        raise ValueError("Телефон не знайдено")

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        if record.name.value in self.data:
            raise ValueError("Контакт вже існує")
        self.data[record.name.value] = record

    def find(self, name):
        if name in self.data:
            return self.data[name]
        raise ValueError("Контакт не знайдено")

    def delete(self, name):
        if name not in self.data:
            raise ValueError("Контакт не знайдено")
        del self.data[name]
