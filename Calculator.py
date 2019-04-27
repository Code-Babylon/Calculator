import math
import random
for x in range(10):
        while True:
                print("OPTIONS:")
                print("Enter 'add' to add two numbers")
                print("Enter 'subtract' to subtract two numbers")
                print("Enter 'multiply' to multiply two numbers")
                print("Enter 'divide' to divide two numbers")
                print("Enter 'prgms' to open up program list")
                print("Enter 'math' to open up math programs")
                print("Enter 'physics' to open up physics equations list")
                print("Enter 'quit' to end the program")
                user_input = input(": ")

                if user_input == "quit":
                      break
                elif user_input == "add":
                      num1 = float(input("Enter a number: "))
                      num2 = float(input("Enter another number: "))
                      result = str(num1 + num2)
                      print("The answer is " + result)
                elif user_input == "subtract":
                      num1 = float(input("Enter a number: "))
                      num2 = float(input("Enter another number: "))
                      result = str(num1 - num2)
                      print("The answer is " + result)
                elif user_input == "multiply":
                      num1 = float(input("Enter a number: "))
                      num2 = float(input("Enter another number: "))
                      result = str(num1 * num2)
                      print("The answer is " + result)
                elif user_input == "divide":
                      num1 = float(input("Enter a number: "))
                      num2 = float(input("Enter another number: "))
                      result = str(num1 / num2)
                      print("The answer is " + result)
                elif user_input == "prgms":
                        print("Enter 'sqrt'")
                        print("Enter 'quadform'")
                        print("Enter 'rand'")
                        print("Enter 'exit'")
                        user_input = input(": ")

                        if user_input == "exit":
                              break
                        elif user_input == "sqrt":
                                num = float(input("Enter number to square root: "))
                                result = str(num**0.5)
                                print("The answer is: " + result)
                        elif user_input == "quadform":
                                num1 = float(input("Enter A value: "))
                                num2 = float(input("Enter B value: "))
                                num3 = float(input("Enter C value: "))
                                result1 = str((-num2 + (num2**2-4*num1*num3)**0.5)/(num1 * 2))
                                result2 = str((-num2 - (num2**2-4*num1*num3)**0.5)/(num1 * 2))
                                print("The answer is: " + result1, result2)
                        elif user_input == "rand":
                                num1 = float(input("Enter lower value: "))
                                num2 = float(input("Enter higher value: "))
                                result = str(print(random.randint(num1, num2)))

                elif user_input == "physics":
                        print("Enter 'kinematics' for kinematic equations")
                        print("Enter 'energy' for energy equations")
                        print("Enter 'exit' to quit")
                        user_input = input(": ")

                        if user_input == "exit":
                                break
                        elif user_input == "kinematics":
                                print("Enter 'velocity'")
                                print("Enter 'distance'")
                                print("Enter 'velocity2'")
                                print("Enter 'back'")
                                user_input = input(": ")

                                if user_input == "back":
                                        break
                                elif user_input == "velocity":
                                        num1 = float(input("Enter velocity inital: "))
                                        num2 = float(input("Enter acceleration: "))
                                        num3 = float(input("Enter time: "))
                                        result = str(num1 + num2 * num3)
                                        print("The answer is: " + result)
                                elif user_input == "distance":
                                        num1 = float(input("Enter distance inital: "))
                                        num2 = float(input("Enter velocity inital: "))
                                        num3 = float(input("Enter time: "))
                                        num4 = float(input("Enter acceleration: "))
                                        result = str(num1 + (num2 * num3) + ((.5 * num4 * num3)**2))
                                        print("The answer is: " + result)
                                elif user_input == "velocity2":
                                        num1 = float(input("Enter velocity inital: "))
                                        num2 = float(input("Enter acceleration: "))
                                        num3 = float(input("Enter final distance: "))
                                        num3 = float(input("Enter distance inital: "))
                                        result = str((num1**2) + (2 * num2) * (num3 - num4))
                                        result2 = str(result**0.5)
                                        print("The answer is: " + result2)
                        elif user_input == "energy":
                                print("Enter 'kinetic'")
                                print("Enter 'potential'")
                                print("Enter 'back'")
                                user_input = input(": ")

                        if user_input == "back":
                                break
                        elif user_input == "kinetic":
                                num1 = float(input("Enter mass: "))
                                num2 = float(input("Enter velocity: "))
                                result = str(.5 * num1 * (num2 ** 2))
                                print("The answer is: " + result)

                elif user_input == "math":
                        print("Enter 'exponent'")
                        print("Enter 'log'")
                        print("Enter 'lawof'")
                        print("Enter 'exit'")
                        user_input = input(": ")

                        if user_input == "exit":
                              break
                        elif user_input == "exponent":
                                num1 = float(input("Enter base: "))
                                num2 = float(input("Enter exponent: "))
                                result = str(num1 ** num2)
                                print("The answer is " + result)
                        elif user_input == "log":
                                num1 = float(input("Enter x: "))
                                num2 = float(input("Enter base: "))
                                result = str(print(math.log(num1, num2)))
                        elif user_input == "lawof":
                                print("Enter 'cosine'")
                                print("Enter 'back'")
                                user_input = input(": ")

                                if user_input == "back":
                                        break
                                elif user_input == "cosine":
                                        num1 = float(input("Enter side 1: "))
                                        num2 = float(input("Enter side 2: "))
                                        num3 = float(input("Enter angle: "))
                                        result = str(print(math.sqrt((num1 ** 2) + (num2 ** 2) - 2 * num1 * num2 * (math.cos(math.radians(num3))))))
