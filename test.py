def simple_generator():
    print('generator starts working')
    yield 42
    print('generator stopped working')


gen = simple_generator()
value = next(gen)
print(value)

# Тут появится исключение StopIteration и генератор закончит свое выполнение, кроме того, если
# захотим снова использовать генератор, то придется создавать новый объект генератора, потому что # прошлый истощился
next(gen)

# Из-за возникновения StopIteration генераторы можно использовать в цикле for и тут 
# StopIteration будет скрыт циклом
for i in simple_generator(): pass