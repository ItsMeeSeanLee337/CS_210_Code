#3.1
city_temp_greater_than_70 = [city for temperature in city_temp 
                             if temperature > 70]

#3.2
studentStatus = [(year,living,time) for year in 'FSJE'
                 for living in 'RC'
                 for time in 'FP']

#3.3
combinations = [(n,m) for n in range (1,11) 
                for m in range(1,11) 
                if ((n + m) % 3) == 0]