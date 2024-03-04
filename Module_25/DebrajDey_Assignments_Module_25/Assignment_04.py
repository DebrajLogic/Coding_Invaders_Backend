class Calculate:
    def add(self, a=0, b=0, c=0):
        return a + b + c


new_sum = Calculate()

print(f'Sum Value: {new_sum.add()}')
print(f'Sum Value: {new_sum.add(1, 1)}')
print(f'Sum Value: {new_sum.add(1, 1, 1)}')
