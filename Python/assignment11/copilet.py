"""
Python 函式練習完整解答
包含 Level 1-3 的所有函式實作與測試
"""
import math
from typing import Union, List, Optional, Any
from collections import Counter
import statistics
import re
import keyword

# ====== Level 1: 基礎數學函式 ======
def add_two_numbers(a: float, b: float) -> float:
    """將兩個數字相加"""
    return a + b

def calculate_circle_area(radius: float) -> float:
    """計算圓形面積"""
    if radius < 0:
        raise ValueError("半徑不能為負數")
    return math.pi * radius * radius

def add_all_nums(*args) -> float:
    """計算任意數量參數的總和"""
    total = 0
    for num in args:
        if not isinstance(num, (int, float)):
            raise TypeError(f"參數 {num} 不是數字類型")
        total += num
    return total

def convert_celsius_to_fahrenheit(celsius: float) -> float:
    """將攝氏溫度轉換為華氏溫度"""
    return (celsius * 9/5) + 32

def check_season(month: Union[int, str]) -> str:
    """根據月份回傳季節"""
    month_names = {
        'january': 1, 'february': 2, 'march': 3, 'april': 4,
        'may': 5, 'june': 6, 'july': 7, 'august': 8,
        'september': 9, 'october': 10, 'november': 11, 'december': 12
    }
    
    if isinstance(month, str):
        month = month_names.get(month.lower())
        if month is None:
            raise ValueError("無效的月份名稱")
    
    if not 1 <= month <= 12:
        raise ValueError("月份必須在 1-12 之間")
    
    if 3 <= month <= 5:
        return "春季"
    elif 6 <= month <= 8:
        return "夏季"
    elif 9 <= month <= 11:
        return "秋季"
    else:
        return "冬季"

def calculate_slope(x1: float, y1: float, x2: float, y2: float) -> float:
    """計算兩點間的斜率"""
    if x1 == x2:
        raise ValueError("垂直線無法計算斜率")
    return (y2 - y1) / (x2 - x1)

def solve_quadratic_eqn(a: float, b: float, c: float) -> tuple:
    """解二次方程式 ax² + bx + c = 0"""
    if a == 0:
        raise ValueError("不是二次方程式 (a=0)")
        
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return x1, x2
    elif discriminant == 0:
        x = -b / (2*a)
        return (x,)
    else:
        return tuple()

# ====== Level 1: 列表處理函式 ======
def print_list(items: list) -> None:
    """列印列表中的每個元素"""
    for item in items:
        print(item)

def reverse_list(items: list) -> list:
    """反轉列表（使用循環）"""
    return items[::-1]  # 或用迴圈實作

def capitalize_list_items(items: List[str]) -> List[str]:
    """將列表中的每個字串首字母大寫"""
    return [str(item).capitalize() for item in items]

def add_item(items: list, item: Any) -> list:
    """在列表末尾添加元素"""
    items = items.copy()  # 避免修改原列表
    items.append(item)
    return items

def remove_item(items: list, item: Any) -> list:
    """從列表中移除指定元素"""
    items = items.copy()  # 避免修改原列表
    if item in items:
        items.remove(item)
    return items

# ====== Level 1: 數列計算 ======
def sum_of_numbers(n: int) -> int:
    """計算從1到n的數字總和"""
    if n < 0:
        raise ValueError("請提供非負整數")
    return sum(range(1, n + 1))

def sum_of_odds(n: int) -> int:
    """計算從1到n的奇數總和"""
    return sum(x for x in range(1, n + 1) if x % 2 == 1)

def sum_of_even(n: int) -> int:
    """計算從1到n的偶數總和"""
    return sum(x for x in range(2, n + 1, 2))

# ====== Level 2: 統計與進階函式 ======
def evens_and_odds(n: int) -> tuple:
    """計算從1到n中偶數和奇數的個數"""
    if n < 1:
        raise ValueError("請提供正整數")
    odds = sum(1 for x in range(1, n + 1) if x % 2 == 1)
    evens = n - odds
    return odds, evens

def factorial(n: int) -> int:
    """計算n的階乘"""
    if n < 0:
        raise ValueError("階乘不接受負數")
    if n == 0:
        return 1
    return n * factorial(n - 1)

def is_empty(item: Any) -> bool:
    """檢查項目是否為空"""
    if item is None:
        return True
    try:
        return len(item) == 0
    except TypeError:
        return False

def calculate_stats(numbers: List[float]) -> dict:
    """計算數列的統計資訊"""
    if not numbers:
        raise ValueError("列表不能為空")
    
    return {
        "mean": statistics.mean(numbers),
        "median": statistics.median(numbers),
        "mode": statistics.mode(numbers),
        "range": max(numbers) - min(numbers),
        "variance": statistics.variance(numbers),
        "std_dev": statistics.stdev(numbers)
    }

# ====== Level 3: 資料分析函式 ======
def is_prime(n: int) -> bool:
    """檢查數字是否為質數"""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def has_unique_elements(items: list) -> bool:
    """檢查列表中的元素是否唯一"""
    return len(items) == len(set(items))

def same_data_type(items: list) -> bool:
    """檢查列表中的元素是否具有相同資料類型"""
    if not items:
        return True
    return all(isinstance(x, type(items[0])) for x in items)

def is_valid_variable(name: str) -> bool:
    """檢查是否為有效的 Python 變數名稱"""
    if not isinstance(name, str):
        return False
    # Python 變數名規則的正則表達式
    pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
    return bool(re.match(pattern, name)) and name not in keyword.kwlist

# ====== 測試函式 ======
def test_all_functions():
    """測試所有函式"""
    print("=== 測試基礎數學函式 ===")
    print(f"add_two_numbers(2, 3) = {add_two_numbers(2, 3)}")
    print(f"calculate_circle_area(2) = {calculate_circle_area(2):.2f}")
    print(f"add_all_nums(1,2,3,4,5) = {add_all_nums(1,2,3,4,5)}")
    print(f"25°C = {convert_celsius_to_fahrenheit(25):.1f}°F")
    print(f"3月的季節是：{check_season(3)}")
    
    print("\n=== 測試列表處理函式 ===")
    test_list = ["apple", "banana", "cherry"]
    print(f"原列表：{test_list}")
    print(f"反轉後：{reverse_list(test_list)}")
    print(f"首字母大寫：{capitalize_list_items(test_list)}")
    print(f"添加元素：{add_item(test_list, 'date')}")
    print(f"移除元素：{remove_item(test_list, 'banana')}")
    
    print("\n=== 測試數列計算 ===")
    n = 10
    print(f"1到{n}的總和：{sum_of_numbers(n)}")
    print(f"1到{n}的奇數總和：{sum_of_odds(n)}")
    print(f"1到{n}的偶數總和：{sum_of_even(n)}")
    
    print("\n=== 測試統計函式 ===")
    numbers = [1, 2, 2, 3, 4, 5, 5, 6]
    stats = calculate_stats(numbers)
    for key, value in stats.items():
        print(f"{key}: {value:.2f}")
    
    print("\n=== 測試資料分析函式 ===")
    print(f"7是質數嗎？{is_prime(7)}")
    print(f"列表元素是否唯一？{has_unique_elements([1,2,3,4])}")
    print(f"列表元素類型是否相同？{same_data_type([1,2,3])}")
    print(f"'my_var'是有效變數名嗎？{is_valid_variable('my_var')}")

if __name__ == "__main__":
    test_all_functions()