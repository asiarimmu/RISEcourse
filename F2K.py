#convert F to K
#run the module or type f5
def F2K():
    F = float(input('Enter temp. in degree Fahreinheit: '))
    K = (F + 459.67) * 5 / 9
    print('Temperature in Kelvin is {:08.4f} K'.format(K))
    
