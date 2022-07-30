def max_sequence(arr):
    maximum = 0
    local_maximum = 0
    for el in arr:
        print('el=', el)
        if local_maximum > 0:
            local_maximum += el
            print('local+el when local >0', local_maximum)
            if local_maximum < 0:
                local_maximum = 0
            elif local_maximum > maximum:
                maximum = local_maximum
                print('maximum', maximum)
        elif el > 0:
            local_maximum += el
            print('local elif=', local_maximum)

    return maximum

# best solution
#  def maxSequence(arr):
#      max,curr=0,0
#      for x in arr:
#          curr+=x
#          if curr<0:curr=0
#          if curr>max:max=curr
#      return max

print(max_sequence([-2, -3, 4, -1, -2, 1, 5, -3]))


