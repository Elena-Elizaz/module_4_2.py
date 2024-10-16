def test_function():
    def inner_function():
     print("Я в области видимости функции test_function")

    inner_function() # ничего не возвращает

inner_function() # Вызов функци inner_function() вне функции test_function выдает ошибку -
# вследствие различия пространства имён, мы не можем достать значение функции, вне этой функции

test_function() # - работает