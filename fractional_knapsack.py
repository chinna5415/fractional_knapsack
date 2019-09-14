#fractional knapsack
global n
n = int(input('enter the number of items : '))

class Fractional:
  def __init__(self,k):
    self.k = k
    self.weight = []
    self.price = []
    self.ratio = []
    self.append_price = []
  def get_data(self):
      for i in range(n):
        x = int(input('enter the price of item : '))
        self.price.append(x)
        y = int(input('enter the weight of item : '))
        self.weight.append(y)
        self.ratio.append(x/y)
  def sort(self):
    for i in range(len(self.ratio)):
      for j in range(i):
        if (self.ratio[j] > self.ratio[j+1]):
          price_temp = self.price[j]
          weight_temp = self.weight[j]
          ratio_temp = self.ratio[j]
          self.price[j] = self.price[j+1]
          self.weight[j] = self.weight[j+1]
          self.ratio[j] = self.ratio[j+1]
          self.price[j+1] = price_temp
          self.weight[j+1] = weight_temp
          self.ratio[j+1] = ratio_temp
          
    print('\nprice\n')
    print(self.price)
    print('\nweight\n')  
    print(self.weight)
    print('\nratio\n')
    print(self.ratio)
    
  def knapscak(self):
    sum = 0
    for i in range(n-1,0,-1):
      if (self.k == 0 or self.k < 1):
        break;
      if (self.weight[i] <= self.k) :
          self.k = self.k - self.weight[i]
          self.append_price.append(self.price[i])
      else :
          fractional = self.k / self.weight[i]
          self.k = self.k - (fractional*self.weight[i])
          self.append_price.append(self.price[i] * fractional)
     
    for i in range(len(self.append_price)):
      sum += self.append_price[i]
    return sum

knapscak_weight = int(input('enter the knapscak weight : '))  
F = Fractional(knapscak_weight)
F.get_data()
F.sort()
print('Maximum benfit : ',F.knapscak())