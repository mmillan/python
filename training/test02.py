"""_summary_
    """
import datetime

fecha1 = datetime.datetime.now()

Num = 0
String = "Mary had a little lamb"

while Num < 10000:
    String = String.lower()
    String = String.upper()
    print(String)
    Num += 1

fecha2 = datetime.datetime.now()

print(fecha2-fecha1)
