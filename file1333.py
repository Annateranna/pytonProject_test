def total_z():
    n, z1, z2 = int(input()), complex(input()), complex(input())
    z_1 = z1.conjugate()
    z_2 = z2.conjugate()
    print(z1**n + z2**n + z_1**n + z_2**(n + 1))
