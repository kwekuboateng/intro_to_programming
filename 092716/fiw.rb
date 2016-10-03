def number_to_words(a)
  units_dictionary = {
    "0" => "",
    "1" => "one",
    "2" => "two",
    "3" => "three",
    "4" => "four",
    "5" => "five",
    "6" => "six",
    "7" => "seven",
    "8" => "eight",
    "9" => "nine",

  }

  tens_dictionary = {
    "0" => "",
    "20" => "twenty",
    "30" => "thirty",
    "40" => "forty",
    "50" => "fifty",
    "60" => "sixty",
    "70" => "seventy",
    "80" => "eighty",
    "90" => "ninety",

  }

  one_tens_dictionary = {
    "10" => "ten",
    "11" => "eleven",
    "12" => "twelve",
    "13" => "thirteen",
    "14" => "fourteen",
    "15" => "fifteen",
    "16" => "sixteen",
    "17" => "seventeen",
    "18" => "eighteen",
    "19" => "nineteen",
  }

a_length = a.length #check length of number

  if a_length == 3 # group number into lengths of three
    hundreds = a[0] #check number at index 0
    hundreds_in_words = units_dictionary[hundreds]
    if hundreds != "0"
      hundreds_in_words += " hundred "
    end

    if a[1] == "1" #number at index 1
      words = hundreds_in_words + " and " + one_tens_dictionary[a[1..2]]
    elsif a[1] == "0"
      a[2] == "0" ? spacer = "" : spacer = "and"
      words = hundreds_in_words + spacer + units_dictionary[a[2]]
    else
      words = hundreds_in_words + " and " + tens_dictionary[a[1]] + " " + units_dictionary[a[2]]
    end

  elsif a_length == 2 #for cases where we have two numbers
    if a[0] == "0"
      words = units_dictionary[a[1]]
    elsif a[0] == "1"
      words = one_tens_dictionary(a)
    else
      words = tens_dictionary[a[0]] + units_dictionary[a[1]]
    end

  elsif a_length == 1 # for cases where we have a single number
    words = units[a]

  else
    puts "Error! This number is out of range"
  end

end

puts number_to_words("650")

def convert(b)
  if String(b)[0] == "-"
    if_negative = true
    b = String(b)[1..-1].to_i
  else
    if_negative = false
  end
 billions = b / 1000000000
 b = b - (billions * 1000000000)
 millions = b / 1000000
 b = b - (millions * 1000000)
 thousands = b / 1000
 b = b - (thousands * 1000)
 results = ""
 if billions > 0
  results += number_to_words(billions) + " billion,"
end
if millions > 0
  results += number_to_words(millions) + " million,"
end
if thousands > 0
  results += number_to_words(thousands) + " thousand,"
end
results += number_to_words(b)

if if_negative
  results = "minus " + results
end

results
end

puts convert(1904577)
puts convert(-1009009)
puts convert(1111122980)
