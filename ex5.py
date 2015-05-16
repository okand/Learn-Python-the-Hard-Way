name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
inch_in_cm = 2.54
lbs_in_kg = 0.45359237

print "Let's talk about %s." % name
print "He's %d inches (or %d centimeters) tall." % (
    height, height * inch_in_cm)
print "He's %d pounds (or %d kilograms) heavy." % (
    weight, weight * lbs_in_kg)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "if I add %d, %d and %d I get %d." % (
    age, height, weight, age + height + weight)

