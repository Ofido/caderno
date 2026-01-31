print("em cima da declaração da classe")


class A:
    def __init__(self):
        print("alooo")

    def decorator_input(self, input):
        print("input")

        def decorator(function):
            print("antes de chamar")

            def use_decorator(*args, **kwargs):
                print(f"chamando com {args=} {kwargs=}")
                args[0]["teste2"] = "bacon"
                retorno = function(*args, **kwargs)
                print("após executar")
                return retorno

            return use_decorator

        return decorator


print("em cima da declaração da classe")
a = A()
print("em cima da declaração da função")


@a.decorator_input("input")
def funcao_que_tem_decorator(entrada, context):
    print(f"b inside a {entrada}, {context}")


print("em cima da chamada da função")
funcao_que_tem_decorator({"teste": "olar"}, context="2")
print("depois da chamada da função")
