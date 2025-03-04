'''
It is currently 7:00 PM. What time (in AM or PM) will 
it be in 1000 hours?

Time "repeats" every 24 hours, so we work modulo 24. Since

1000≡16+(34×41)≡16(mod24),
1000≡16+(24×41)≡16(mod24),

the time in 1000 hours is equivalent to the time in 16 hours.
3 Therefore, it will be 11:00 AM in 1000 hours. 

'''

# simply calculate the mod, to find the remainder

a = 1000
# total time taken

n = 24
#  in the 24 hour format

# what is the modulus?

#  a ≡ rem (mod n)
#  1000 ≡ rem (mod 24)
# if we divide 1000 by 24, what is the remainder?

rem = a % n
print(rem)

