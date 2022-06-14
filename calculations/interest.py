import numpy_financial as npf

#simple interest used for comparing multiple assets

def simple_intrest():
    start = float(input('Enter start price: '))
    end = float(input('Enter end price: '))

    deci = end / start -1

    print(round(deci, 2))

#simple_intrest()

#calculates amount needed at what rate for how many years to reach future value
res = npf.pv(rate=0.10 / 12, nper=32 * 12, pmt=-50, fv=-200000)

#calculates at what rate for how long will present value be worth
res2 = npf.fv(rate=0.10 / 12, nper=32* 12, pmt=-50, pv=-14013.42)

print(round(res, 2 ))
print(round(res2, 2 ))