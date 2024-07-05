from nada_dsl import *

# Hypothetical telemetry initialization with an identifier
telemetry_id = "your-telemetry-identifier"
initialize_telemetry(telemetry_id)

def nada_main():
    party1 = Party(name="Party1")

    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    new_int = my_int1 + my_int2

    return [Output(new_int, "my_output", party1)]

if __name__ == "__main__":
    environment = Environment()
    program = environment.compile(nada_main)
    result = environment.execute(program)

    for output in result.outputs:
        print(f"{output.name}: {output.value}")
