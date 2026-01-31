print("[INÍCIO] Antes da declaração do decorador")


def decorator(function):
    print("[DECORATOR] Antes de declarar o decorador")

    def use_decorator(*args, **kwargs):
        print(
            (
                "[DECORATOR] Chamando função decorada com:"
                f" args={args}, kwargs={kwargs}"
            )
        )
        args[0]["teste2"] = "bacon"
        retorno = function(*args, **kwargs)
        print(
            (
                "[DECORATOR] Após executar a função decorada: "
                f"retorno={retorno}"
            )
        )
        retorno_de_verdade = f"<{retorno}>"
        return retorno_de_verdade

    print("[DECORATOR] Depois de declarar o decorador")

    return use_decorator


print("[INÍCIO] Antes da declaração da função decorada")


@decorator
def funcao_que_tem_decorator(entrada: dict[str, str], context: str) -> str:
    print(
        (
            "[FUNÇÃO] Executando função decorada: "
            f"entrada={entrada}, context={context}"
        )
    )
    return "retorno"


print("[INÍCIO] Antes de executar a função decorada")
retorno = funcao_que_tem_decorator({"teste": "oi"}, context="2")
print(f"[FIM] Depois de executar a função decorada: retorno={retorno}")
