def test(**kwargs):
    print('nums:{}'.format(kwargs))
    print('k1:{}'.format(kwargs['k1']))
    for i,j in kwargs:
        print('k_num:{}'.format(j))

test(k1=1,k2=5,k3=1)


def test_1(*args,**kwargs):
    print('num:{},k_num:{}'.format(args,kwargs))
num=[2,5,1]
test_1(*num,k1=1,k2=2)
