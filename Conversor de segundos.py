segundos = int(input("Por favor, entre com o número de segundos que deseja converter:"))

dias = segundos // 86400
segundosRest = segundos % 86400

horas = segundosRest // 3600
segundosRest= segundosRest % 3600

minutos = segundosRest // 60
segundosRest= segundosRest % 60

print(dias, "dias,", horas, "horas,", minutos, "minutos e ", segundosRest, "segundos.") 
