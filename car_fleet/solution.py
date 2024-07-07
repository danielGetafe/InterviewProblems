class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars_dict = {
            position_item: speed_item
            for position_item, speed_item in zip(position, speed)
        }
        ordered_car_list = sorted(cars_dict.items())
        cars_count = len(position)
        stack = [ordered_car_list[0]]
        second_car_index = 1
        while second_car_index < cars_count:
            if (
                stack
                and stack[-1][1] > ordered_car_list[second_car_index][1]
                and (ordered_car_list[second_car_index][0] - stack[-1][0])
                / (stack[-1][1] - ordered_car_list[second_car_index][1])
                <= (target - ordered_car_list[second_car_index][0])
                / ordered_car_list[second_car_index][1]
            ):
                stack.pop()
                continue
            stack.append(ordered_car_list[second_car_index])
            second_car_index += 1
        return len(stack)
