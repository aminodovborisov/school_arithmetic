# -*- coding: utf-8 -*-

class SumLikeSchool:

    def adding_zeros(self, num_str, inp_len):
        delta = inp_len - len(num_str)
        zeros = ''
        for i in range(0, delta):
            zeros += '0'
        return zeros + num_str
    
    def replace_nth(self, inp_string, new_sym, index_of_new):
        if index_of_new <= len(inp_string):
            new_string = inp_string[0 : index_of_new] + new_sym + inp_string[index_of_new + 1 :]
        else:
            new_string = inp_string
        return new_string

    # Сложение двух чисел столбиком.
    def sum_like_school(self, smd_one, smd_two):

        # Прежде всего: слагаемые должны быть строками.
        # Кроме того, количество цифр должно быть одинаковым, 
        # при необходимости дополняем короткое число нулями слева.
        smd_one_str = str(smd_one)
        smd_two_str = str(smd_two)
        if len(smd_one_str) > len(smd_two_str):
            smd_two_str = self.adding_zeros(smd_two_str, len(smd_one_str))
        elif len(smd_one_str) < len(smd_two_str):
            smd_one_str = self.adding_zeros(smd_one_str, len(smd_two_str))
        
        summary = '0' * len(smd_one_str)  # Переменная для итоговой суммы
        move_digit = 0  # Десятки очередной суммы для переноса в левый разряд
        for i in range(len(smd_one_str) - 1, -1, -1):  # Идём справа налево
            dgt_one = int(smd_one_str[i])
            dgt_two = int(smd_two_str[i])

            # Складываем две очередных цифры и учитываем перенесённые десятки 
            # из суммы предыдущих цифр
            pre_sum_number = dgt_one + dgt_two + move_digit

            if pre_sum_number > 9:  # Сумма двух цифр больше десяти?
                move_digit = pre_sum_number // 10  # Десятки для переноса влево

                # Для итоговой суммы фиксируем разряд единиц
                sum_digit = str(pre_sum_number - move_digit * 10)
                summary = self.replace_nth(summary, sum_digit, i)
            else:
                move_digit = 0  # Нечего переносить влево

                # Фиксируем результат
                sum_digit = str(pre_sum_number)  
                summary = self.replace_nth(summary, sum_digit, i)
        
        if move_digit  == 0:
            return summary
        else:
            return str(move_digit) + summary
            

sumlike = SumLikeSchool()

big_num_one = 980890980978582896546254175578256867582397545239765593673542028795620861904648667408460630686205682577672554972656086233
big_num_two = 167397753548588975297848256875
big_sum = sumlike.sum_like_school(big_num_one, big_num_two)

print(big_sum)
print(big_num_one + big_num_two)
