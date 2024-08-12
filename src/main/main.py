
from src.components.perturbation import Perturbate


def main():
    text = "hello, how are you?"

    perturbate = Perturbate(text)
    perturbated = perturbate.call_by_type('random_char_insertion')
    print(f"Original:: {text}")
    print(f"perturbated:: {perturbated}")
    


if __name__ == "main":
    main()