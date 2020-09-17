# You will have to figure out what parameters to include

# Write a recursive function called `reverse` that accepts a ss and returns a reversed ss.

def reverse(string):
    # Write code here
    # if ss == "":
    #     return ss
    # else: 
    #     return ss[-1] + reverse(ss[:-1])
    # base case
    if len(string) == 0:
        return ""
    # recursive step
    # print(string)
    return string[-1] + reverse(string[:-1])


# print(reverse("")) 
# => ""
# print(reverse("a")) 
# => "a"
# print(reverse("ab")) 
# => "ba"
print(reverse("computer")) 
# => "retupmoc"
print(reverse(reverse("computer"))) 
# => "computer"

# r + reverse('compute')
    # e + reverse('comput')
        # t + reverse('compu')
            # u + reverse('comp')
                # p + reverse('com')
                    # m + reverse('co')
                        # o + reverse('c')
                            # c + reverse('')
