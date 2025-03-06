CodingMonth = {"Enero":0, "Febrero":3, "Marzo":3, "Abril":6, "Mayo":1, "Junio":4,"Julio":6, "Agosto":2, "Septiembre":5, "Octubre":0, "Noviembre":3, "Diciembre":5}
CodingDay = {0:"Domingo", 1:"Lunes", 2:"Martes", 3:"Miércoles", 4:"Jueves", 5:"Viernes", 6:"Sábado"}
CodingCentury = {0: 6, 1: 4, 2: 2, 3: 0}


def dayCalculator(day, month, year):
    month = month.capitalize()
    centuryCode = (year // 100) % 4
    yearCode = (year % 100 + (year % 100) // 4) % 7

    leapYearCorrection = -1 if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) and (month in ["Enero", "Febrero"]) else 0

    codeDay = (CodingCentury[centuryCode] + yearCode + CodingMonth[month] + day + leapYearCorrection) % 7
    return CodingDay[codeDay]
