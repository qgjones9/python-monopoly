class deeds:
    def __init__(self, name, rent, rent_color_set, hideout, facility, mortgage, unmortgage):
        self.name = name
        self.rent = rent
        self.rent_color_set = rent_color_set
        self.hideout = hideout
        self.facility = facility
        self.mortgage = mortgage
        self.unmortgage = unmortgage

    def deed_name(self):
        print(self.name)

    def deed_rent(self):
        print(self.rent)

    def deed_rent_color_set(self):
        print(self.rent_color_set)

    def deed_hideout(self):
        print(self.hideout)

    def deed_facility(self):
        print(self.facility)

    def deed_mortgage(self):
        print(self.mortgage)

    def deed_unmortgage(self):
        print(self.unmortgage)

