breakfast = ["cheerios", "trix", "frosties"]

def cereal_time(breakfast):
  for each_cereal in breakfast:
    last_letter = each_cereal[-1]
    if last_letter == "s":
      print(each_cereal, "are yummy!")
    else:
      print(each_cereal, "is yummy!")

cereal_time(breakfast)