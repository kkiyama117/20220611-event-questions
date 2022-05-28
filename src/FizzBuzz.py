for num in range(1, 101):
    string = ""

    # ここから記述
    # list等でまとめてjoinした方が呼び出し回数的には良いが指定の範囲内なので不採用
    if num % 3 == 0 and num % 5 == 0:
        string = string.join("FizzBuzz")
    elif num % 3 == 0:
        string = string.join("Fizz")
    elif num % 5 == 0:
        string = string.join("Buzz")
    else:
        string = string.join(str(num))
    # ここまで記述

    print(string)
