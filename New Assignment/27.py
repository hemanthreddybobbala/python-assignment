def varidic_args(*args,**kargs):
    total = sum(args)
    scale = kargs.get('scale',1)
    return total * scale
print(varidic_args(1,3,4,5))





