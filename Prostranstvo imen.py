# Вызов функции inner_function внутри функции test_function
def test_function():
    print('Объемлющаяя область видимости для inner_function')
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()
result = test_function()
print(result)

# Вызов функции inner_function вне функции test_function

def test_function():
    print('Объемлющаяя область видимости для inner_function')
    def inner_function():
        print('Я в области видимости функции test_function')
inner_function()
result = test_function()
print(result)
