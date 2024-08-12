from perturbation import Perturbate

text = "hello, how are you?"

perturbate = Perturbate(text)
perturbated = perturbate.call_by_type('random_char_insertion')
print(f"Original:: {text}")
print(f"perturbated:: {perturbated}")