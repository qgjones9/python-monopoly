class deeds:
    ''' The deeds class will be utilized to describe Title Deeds'''

    def __init__(self, name, rent, rent_color_set, rent_one_house, rent_two_house,
                 rent_three_house, rent_four_house, rent_facility, hideout_cost, facility_cost, mortgage, unmortgage):

        # Class variables for usage when creating space objects

        self.name = name
        self.rent = rent
        self.rent_color_set = rent_color_set
        self.rent_one_house = rent_one_house
        self.rent_two_house = rent_two_house
        self.rent_three_house = rent_three_house
        self.rent_four_house = rent_four_house
        self.sent_facility = rent_facility
        self.hideout = hideout_cost
        self.facility = facility_cost
        self.mortgage = mortgage
        self.unmortgage = unmortgage

    def deed_name(self):
        print(self.name)

    def deed_rent(self):
        print(self.rent)

    def deed_rent_color_set(self):
        print(self.rent * 2)

    def deed_rent_one_house(self):
        print(self.rent_one_house)

    def deed_rent_two_house(self):
        print(self.rent_two_house)

    def deed_rent_three_house(self):
        print(self.rent_three_house)

    def deed_rent_four_house(self):
        print(self.rent_four_house)

    def deed_rent_facility(self):
        print(self.facility)

    def hideout_cost(self):
        print(self.hideout_cost)

    def facility_cost(self):
        print(self.facility_cost)

    def deed_mortgage(self):
        print(self.mortgage)

    def deed_unmortgage(self):
        print(self.unmortgage)

    def deed_details(self):
        print('Deed name : ' + str(self.name),
              'Rent: ' + str(self.rent),
              'Rent with color set: ' + str(self.rent_color_set),
              'Rent with 1 Hideout: '+ str(self.rent_one_house),
              'Rent with 2 Hideout: ' + str(self.rent_two_house),
              'Rent with 3 Hideout: ' + str(self.rent_three_house),
              'Rent with 4 Hideout: ' + str(self.rent_four_house),
              'Hideout Cost: ' + str(self.hideout),
              'Facility Cost: ' + str(self.facility),
              'Mortgage cost: ' + str(self.mortgage),
              'Unmortgage cost: ' + str(self.unmortgage), sep='\n')
