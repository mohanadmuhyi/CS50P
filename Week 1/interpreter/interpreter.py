equation = input("Expression: ")
x, operator, y = equation.split(" ")

match operator:
    case "+":
        print(float(x) + float(y))
    case "-":
        print(float(x) - float(y))
    case "/":
        print(float(x) / float(y))
    case "*":
        print(float(x) * float(y))
