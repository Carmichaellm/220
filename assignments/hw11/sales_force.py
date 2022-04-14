from sales_person import SalesPerson

class SalesForce:
    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        sale_file = open(file_name, 'r')
        for line in sale_file.readlines():
            self.sales_people.append(line)

    def quota_report(self, quota):
        for i in range(len(self.sales_people)):
            self.sales_people[i] = self.sales_people[i].split(',')
            self.sales_people[i][2] = self.sales_people[i][2].split()
            total = 0.0
            for j in self.sales_people[i][2]:
                total = total + float(j)
            self.sales_people[i][2] = total
            if self.sales_people[i][2] >= quota:
                self.sales_people[i][2].append(True)
            else:
                self.sales_people[i][2].append(False)
        return  self.sales_people

    def top_seller(self):
        top = self.sales_people[0][2]
        top_list = [self.sales_people[0]]
        for i in range(len(self.sales_people)):
            if self.sales_people[i][2] > top:
                top_list = [self.sales_people[i]]
            if self.sales_people[i][2] == top:
                top_list.append(self.sales_people[i])
        return top_list

    def individual_sales(self, employee_id):
        for i in range(len(self.sales_people)):
            if self.sales_people[i] == employee_id:
                return self.sales_people[i][1]
        return None

    def get_sale_frequencies(self):
        freq = {}
        for i in range(len(self.sales_people)):
            freq[self.sales_people[i][2]] = freq.get(self.sales_people[i][2], 0) + 1
        return freq