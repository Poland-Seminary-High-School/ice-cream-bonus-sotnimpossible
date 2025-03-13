prompt = 'enter silly ice cream fix-ins :3\n'
prompt += 'type done when youre done\n'
toppings = []
while True:
    topping=input(prompt)
    if topping.lower()=='done':
        break
    else:
        toppings.append(topping)
        print('put some', topping, 'on your silly ice cream')
print('your ice cream contains', toppings,'\nthank you for shopping at ice cream dot com or whatever')
#i mean yeah i already made it print the list yesterday bc i got bored whoops